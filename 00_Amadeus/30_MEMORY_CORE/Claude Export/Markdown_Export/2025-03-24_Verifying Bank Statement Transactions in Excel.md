# Verifying Bank Statement Transactions in Excel

**Created:** 2025-03-24 02:55:04

**Summary:**
**Conversation Overview**

The user requested help transforming bank statement transactions into an Excel format and verifying that all transactions had been properly recorded. They provided two documents: a Fifth Third Bank business checking account statement for The Magnificent Child Care covering January 1-31, 2024, and an existing Excel spreadsheet containing transaction data. The user wanted Claude to compare these sources to ensure completeness and accuracy of the transaction recording.

Claude began developing a Python-based analysis tool to extract and compare transactions from both sources. The approach involved parsing the bank statement to identify checks, withdrawals/debits, and deposits/credits, then comparing these against the Excel data. Claude created functions to extract transaction data using regular expressions to parse dates, amounts, and descriptions from the bank statement format, while also parsing the structured Excel data. The analysis aimed to create a comprehensive comparison table showing which transactions appeared in both sources and identifying any discrepancies or missing entries.

The conversation focused on financial data reconciliation and transaction verification, with Claude working to automate the comparison process between the official bank statement and the user's internal Excel tracking system. This type of analysis is crucial for business accounting accuracy and ensuring all financial transactions are properly documented across different record-keeping systems.

---

## Human

je veux transformer les transactions sur ce bank statement en tableau excel verifie si toutes les transactions ont ete reporter

## Assistant

 Je vais comparer les transactions du relevé bancaire de Fifth Third Bank (document 1) avec le tableau Excel des transactions (document 2) pour vérifier si toutes les transactions ont été correctement reportées.

Commençons par analyser les deux documents et créer un tableau de comparaison.

<antArtifact identifier="transaction-comparison" type="application/vnd.ant.code" language="python" title="Analyse des transactions bancaires">
import pandas as pd
import re
from datetime import datetime

# Fonction pour extraire les transactions du relevé bancaire (document 1)
def extract_bank_statement_transactions(text):
    transactions = []
    
    # Extraire les chèques
    check_pattern = r"(\d+)\s*i\s*(\d{2}/\d{2})\s*([\d,]+\.\d{2})"
    for match in re.finditer(check_pattern, text):
        check_num = match.group(1)
        date = match.group(2)
        amount = float(match.group(3).replace(',', ''))
        date_obj = datetime.strptime(f"2024/{date}", "%Y/%m/%d")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        
        transactions.append({
            "Date": formatted_date,
            "Type": "Chèque",
            "Montant": amount,
            "Description": f"Check #{check_num}",
            "Source": "Bank Statement"
        })
    
    # Extraire les retraits/débits
    withdrawal_pattern = r"(\d{2}/\d{2})\s*([\d,]+\.\d{2})\s*(.*?)(?=\d{2}/\d{2}|\n\n|$)"
    withdrawal_section = re.search(r"Withdrawals / Debits(.*?)Deposits / Credits", text, re.DOTALL)
    
    if withdrawal_section:
        withdrawal_text = withdrawal_section.group(1)
        
        current_date = None
        current_amount = None
        
        for line in withdrawal_text.split('\n'):
            date_match = re.match(r"(\d{2}/\d{2})\s+([\d,]+\.\d{2})", line)
            if date_match:
                current_date = date_match.group(1)
                current_amount = float(date_match.group(2).replace(',', ''))
                description = line[date_match.end():].strip()
                
                # Si la description est vide, c'est probablement juste le début d'une entrée multilignes
                if description:
                    date_obj = datetime.strptime(f"2024/{current_date}", "%Y/%m/%d")
                    formatted_date = date_obj.strftime("%Y-%m-%d")
                    
                    transactions.append({
                        "Date": formatted_date,
                        "Type": "Débit",
                        "Montant": current_amount,
                        "Description": description,
                        "Source": "Bank Statement"
                    })
                    current_date = None
                    current_amount = None
            elif current_date and current_amount:
                # C'est une ligne de continuation pour une description
                description = line.strip()
                date_obj = datetime.strptime(f"2024/{current_date}", "%Y/%m/%d")
                formatted_date = date_obj.strftime("%Y-%m-%d")
                
                transactions.append({
                    "Date": formatted_date,
                    "Type": "Débit",
                    "Montant": current_amount,
                    "Description": description,
                    "Source": "Bank Statement"
                })
                current_date = None
                current_amount = None
    
    # Extraire les dépôts/crédits
    deposit_pattern = r"(\d{2}/\d{2})\s*([\d,]+\.\d{2})\s*(.*?)(?=\d{2}/\d{2}|\n\n|$)"
    deposit_section = re.search(r"Deposits / Credits(.*?)Daily Balance Summary", text, re.DOTALL)
    
    if deposit_section:
        deposit_text = deposit_section.group(1)
        
        for match in re.finditer(r"(\d{2}/\d{2})\s+([\d,]+\.\d{2})\s+(.*?)(?=\d{2}/\d{2}|\n\n|$)", deposit_text, re.DOTALL):
            date = match.group(1)
            amount = float(match.group(2).replace(',', ''))
            description = match.group(3).strip()
            
            date_obj = datetime.strptime(f"2024/{date}", "%Y/%m/%d")
            formatted_date = date_obj.strftime("%Y-%m-%d")
            
            transactions.append({
                "Date": formatted_date,
                "Type": "Crédit",
                "Montant": amount,
                "Description": description,
                "Source": "Bank Statement"
            })
    
    return transactions

# Fonction pour extraire les transactions du tableau Excel (document 2)
def extract_excel_transactions(text):
    transactions = []
    
    # Chercher les lignes de transactions
    lines = text.split('\n')
    transaction_pattern = r"(2024-\d{2}-\d{2})\s+(Débit|Crédit|Chèque)\s+([\d,]+\.\d{2})\s+(.*?)\s+(.*?)\s+"
    
    for line in lines:
        match = re.match(transaction_pattern, line)
        if match:
            date = match.group(1)
            type_trans = match.group(2)
            amount = float(match.group(3).replace(',', ''))
            description = match.group(4)
            
            transactions.append({
                "Date": date,
                "Type": type_trans,
                "Montant": amount,
                "Description": description,
                "Source": "Excel"
            })
    
    return transactions

# Extraire les transactions des deux sources
bank_transactions = extract_bank_statement_transactions("""
THE MAGNIFICENT CHILD CARE
7503 INDUSTRIAL RD
FLORENCE KY 41042-2201
PSKEY01|DDA0|01|FTNK|20240131|8|0|S|1|2421|2421|7925347390|0|7303||PSKEY99|
FTCSTMT048 048 20240131 UDSPDFSTMT 0000000007925347390 DDA
Page 1 of 4
(NORTHERN KENTUCKY)
P.O. BOX 630900 CINCINNATI OH 45263-0900
For additional information and account disclosures, please visit www.53.com/businessbanking
Statement Period Date: 1/1/2024 - 1/31/2024
Account Type: 5/3 BUSINESS CKG
Account Number: 7925347390
0
2421
Banking Center: Burlington Pike
Banking Center Phone: 859-283-8222
Business Banking Support: 877-534-2264
Account Summary - 7925347390
01/01 Beginning Balance $13,705.76 Number of Days in Period 31
2 Checks $(2,300.00)
80 Withdrawals / Debits $(34,214.16)
7 Deposits / Credits $23,748.00
01/31 Ending Balance $939.60
Analysis Period: 12/01/23 - 12/31/23
Standard Monthly Service Charge $0.00
Service Charge withdrawn on 01/11/24 $0.00
Checks 
2 checks totaling $2,300.00
* Indicates gap in check sequence i = Electronic Image s = Substitute Check
Number Date Paid Amount Number Date Paid Amount
1279 i 01/04 200.00 1397*i 01/05 2,100.00
Withdrawals / Debits 
80 items totaling $34,214.16
Date Amount Description
01/02 29.11 MERCHANT PAYMENT - 041809 KROGER #4 4500 MONTGOM CINCINNATI OH ON 010224 FROM CARD#:
XXXXXXXXXXXX396X
01/02 39.80 DEBIT CARD PURCHASE AT BP#9561101CAPL KY0, ERLANGER, KY ON 231230 FROM CARD#:
XXXXXXXXXXXX3962
01/02 98.03 MERCHANT PAYMENT - 427001 INTERNATI 7639 DIXIE H FLORENCE KY ON 010224 FROM CARD#:
XXXXXXXXXXXX396X
01/02 109.79 MERCHANT PAYMENT - 043813 KROGER #4 2120 BEECHMO CINCINNATI OH ON 010224 FROM CARD#:
XXXXXXXXXXXX396X
01/02 5.43 EPX ST 032148241 MERCH SETL MERCH SETL 3130032148241 THE MAGNIFICENT CHILD 010224
01/02 38.71 MERCHANT PAYMENT NST THE HOME DEP - 219060 3400 HIGHLAND AVE CINCINNATI OH ON 010224
FROM CARD#: XXXXXXXXXXXX396X
01/03 23.31 TUITIONEXPRESS FEES SEP 84870022296232 THE MAGNIFICENT CHILD 010324
01/03 85.56 EPX FE 032148241 MERCH SETL MERCH SETL 3130032148241 THE MAGNIFICENT CHILD 010324
01/04 17.00 DEBIT CARD PURCHASE AT FLORENCE TANNING &, FLORENCE, KY ON 010224 FROM CARD#:
XXXXXXXXXXXX3962
01/04 502.60 PAYCHEX TPS 38081 TAXES 05365700003281X MAGNIFICENT CHILD CARE 010424
01/04 1,835.28 PAYCHEX INC. PAYROLL AORC64ZXrhTfPFO MAGNIFICENT CHILD CARE 010424
01/05 60.00 RECURRING PURCHASE AT SBA LOAN PAYMENT, DENVER, CO ON 010424 FROM CARD#:
XXXXXXXXXXXX3541
01/05 99.07 RECURRING PURCHASE AT UNIVERSITY OF CINC, BOSTON, MA ON 010424 FROM CARD#:
XXXXXXXXXXXX3541
01/05 3,476.04 RECURRING PURCHASE AT UNIVERSITY OF CINC, CINCINNATI, OH ON 010424 FROM CARD#:
XXXXXXXXXXXX3541
01/05 19.93 PAYX-PIA-WC WC-PREMIUM 0000044659047 MAGNIFICENT CHILD CARE 010524
01/05 131.75 PAYCHEX EIB INVOICE X05359800043242 MAGNIFICENT CHILD CARE 010524
01/08 46.51 DEBIT CARD PURCHASE AT SHELL OIL 12426510, HEBRON, KY ON 010524 FROM CARD#:
XXXXXXXXXXXX3962
01/08 121.01 DEBIT CARD PURCHASE AT PROMISEPAY* GCWW, OAKLAND, CA ON 010624 FROM CARD#:
XXXXXXXXXXXX3541
01/08 190.87 MERCHANT PAYMENT COSTCO WHSE #11 - 119713 FLORENCE FLORENCE KY ON 010824 FROM CARD#:
XXXXXXXXXXXX396X
01/08 2,005.64 DEBIT CARD PURCHASE AT TAXACT, 3193733600, TX ON 010524 FROM CARD#: XXXXXXXXXXXX3541
01/08 495.48 TELEPHONE INITIATED PAYMENT AT DUKEENERGY BILL PAY 910102034590 010824
01/10 24.24 MERCHANT PAYMENT - 335907 MNRD-FLOR 5000 APEX LN FLORENCE KY ON 011024 FROM CARD#:
XXXXXXXXXXXX354X
01/10 43.87 MERCHANT PAYMENT SHELL SERVICE S - 112301 SHELL HEBRON KY ON 011024 FROM CARD#:
XXXXXXXXXXXX396X
01/10 341.00 DEBIT CARD PURCHASE AT WF WAYFAIR42098709, 8662638325, MA ON 010924 FROM CARD#:
XXXXXXXXXXXX3962
01/10 24.59 MERCHANT PAYMENT CHEAPOAIR.COM - 002 COA CHEAPOAIR COM AIR NEW YORK NY ON 011024 FROM
CARD#: XXXXXXXXXXXX354X
01/11 59.54 DEBIT CARD PURCHASE AT USPS PO 2036410648, HEBRON, KY ON 011024 FROM CARD#:
XXXXXXXXXXXX3962
01/11 218.87 RECURRING PURCHASE AT STATE FARM INSURA, BLOOMINGTON, IL ON 011024 FROM CARD#:
XXXXXXXXXXXX3541
01/11 402.76 MERCHANT PAYMENT SAMS CLUB #8133 - 330002 SAM'S Club FLORENCE KY ON 011124 FROM CARD#:
XXXXXXXXXXXX396X
01/11 11,000.00 5/3 ONLINE TRANSFER TO CK: XXXXXX3726 REF # 00973274048
01/12 52.17 MERCHANT PAYMENT ALDI 61025 - 073903 CINCINNATI CINCINNATI OH ON 011224 FROM CARD#:
XXXXXXXXXXXX396X
01/12 121.01 DEBIT CARD PURCHASE AT PROMISEPAY* GCWW, OAKLAND, CA ON 011124 FROM CARD#:
XXXXXXXXXXXX3541
01/12 800.40 DEBIT CARD PURCHASE AT ETHIOPIA, 800-4452733, VA ON 011024 FROM CARD#: XXXXXXXXXXXX3541
01/16 39.96 DEBIT CARD PURCHASE AT SAMSCLUB #8133, FLORENCE, KY ON 011524 FROM CARD#:
XXXXXXXXXXXX3541
01/16 41.00 MERCHANT PAYMENT - 427001 INTERNATI 7639 DIXIE H FLORENCE KY ON 011624 FROM CARD#:
XXXXXXXXXXXX396X
01/16 102.97 DEBIT CARD PURCHASE AT PMT*OH BUREAU MOTO, COLUMBUS, OH ON 011224 FROM CARD#:
XXXXXXXXXXXX3962
01/16 444.35 MERCHANT PAYMENT RESTAURANT DEPOT - A61002 4501 W MITCHELL AVE CINCINNATI OH ON 011624
FROM CARD#: XXXXXXXXXXXX396X
01/16 518.30 DEBIT CARD PURCHASE AT PY *HAMILTON - DOW, CINCINNATI, OH ON 011224 FROM CARD#:
XXXXXXXXXXXX3962
01/17 196.88 DEBIT CARD PURCHASE AT THE GENERAL 800 28, 800-2801466, TN ON 011624 FROM CARD#:
XXXXXXXXXXXX3541
01/17 372.54 RECURRING PURCHASE AT ATT* BILL PAYMENT, DALLAS, TX ON 011624 FROM CARD#:
XXXXXXXXXXXX3962
01/18 37.07 MERCHANT PAYMENT O'REILLY 3880 - 634802 FLORENCE FLORENCE KY ON 011824 FROM CARD#:
XXXXXXXXXXXX354X
01/18 63.16 MERCHANT PAYMENT - 040915 KROGER #4 3105 NORTH B HEBRON KY ON 011824 FROM CARD#:
XXXXXXXXXXXX396X
01/18 162.04 MERCHANT PAYMENT - 427001 INTERNATI 7639 DIXIE H FLORENCE KY ON 011824 FROM CARD#:
XXXXXXXXXXXX396X
01/18 162.61 DEBIT CARD PURCHASE AT TAKE 5 #269, FLORENCE, KY ON 011724 FROM CARD#: XXXXXXXXXXXX3541
01/18 190.00 WEB INITIATED PAYMENT AT CHASE CREDIT CRD EPAY 7246433614 011824
01/18 633.33 PAYCHEX TPS 38122 TAXES 05712500019326X MAGNIFICENT CHILD CARE 011824
01/18 2,369.35 PAYCHEX INC. PAYROLL vVzyOyNR9OsPk3T MAGNIFICENT CHILD CARE 011824
01/19 43.10 MERCHANT PAYMENT - 041813 KROGER #4 4500 MONTGOM CINCINNATI OH ON 011924 FROM CARD#:
XXXXXXXXXXXX396X
01/19 99.00 DEBIT CARD PURCHASE AT PROCARE SOFTWARE, MEDFORD, OR ON 011824 FROM CARD#:
XXXXXXXXXXXX3962
01/19 27.11 PAYX-PIA-WC WC-PREMIUM 0000044750716 MAGNIFICENT CHILD CARE 011924
01/19 242.26 PAYCHEX EIB INVOICE X05731500029650 MAGNIFICENT CHILD CARE 011924
01/22 57.63 RECURRING PURCHASE AT OOMA,INC, 888-711-6662, CA ON 012024 FROM CARD#: XXXXXXXXXXXX3962
01/22 91.97 MERCHANT PAYMENT - 041813 KROGER #4 4500 MONTGOM CINCINNATI OH ON 012224 FROM CARD#:
XXXXXXXXXXXX396X
01/22 400.00 5/3 JEANIE WITHDRAWAL - 002658 3095 NORTH BEND ROAD HEBRON KY ON 012224 FROM CARD#:
XXXXXXXXXXXX396X
01/22 80.16 SANITATION DISTR BILLPAY SD1 012224
01/22 259.57 KENTUCKY FARM B2 ACCT BILL 0013527640 012224
01/22 9.52 PYMT TO Speedpay: Duke-E - 101043 139 East Fourth Street Cincinnati OH
01/22 121.93 PYMT TO Speedpay: Duke-E - 101043 139 East Fourth Street Cincinnati OH
01/22 202.85 JEANIE WITHDRAWAL - G12908 2740 SPRING GROVE AVE. CINCINNATI OH ON 012224 FROM CARD#:
XXXXXXXXXXXX354X
01/22 301.50 PYMT TO Speedpay: Duke-E - 101043 139 East Fourth Street Cincinnati OH
01/22 3.00 NON-5/3 CASH WITHDRAWAL FEE
01/23 40.24 MERCHANT PAYMENT Speedway - 534801 7819 Us-42 Florence KY ON 012324 FROM CARD#:
XXXXXXXXXXXX396X
01/24 200.00 5/3 JEANIE WITHDRAWAL - 005601 1850 SEYMOUR AVE CINCINNATI OH ON 012424 FROM CARD#:
XXXXXXXXXXXX354X
01/25 11.99 RECURRING PURCHASE AT CCSI FAX.OM, 888-429-4615, CA ON 012424 FROM CARD#:
XXXXXXXXXXXX3962
01/25 2,238.38 RECURRING PURCHASE AT CAMARGO INSURANCE, BRANFORD, CT ON 012424 FROM CARD#:
XXXXXXXXXXXX3962
01/25 167.51 MERCHANT PAYMENT SAMS CLUB #8133 - 330002 SAM'S Club FLORENCE KY ON 012524 FROM CARD#:
XXXXXXXXXXXX354X
01/26 137.14 RECURRING PURCHASE AT Spectrum, 855-707-7328, MO ON 012524 FROM CARD#: XXXXXXXXXXXX3541
01/26 7.28 MERCHANT PAYMENT SAMS CLUB #8133 - 330083 SAM'S Club Florence KY ON 012624 FROM CARD#:
XXXXXXXXXXXX396X
01/26 42.51 PYMT TO RUMPKE PHONEPAYM - 003 RUMPKE PHONEPAYMENT CINCINNATI OH
01/29 31.91 DEBIT CARD PURCHASE AT CHICK-FIL-A #02593, FLORENCE, KY ON 012524 FROM CARD#:
XXXXXXXXXXXX3541
01/29 42.98 MERCHANT PAYMENT - 427001 INTERNATI 7639 DIXIE H FLORENCE KY ON 012924 FROM CARD#:
XXXXXXXXXXXX396X
01/29 44.99 DEBIT CARD PURCHASE AT INTERNATIONAL GROC, FLORENCE, KY ON 012724 FROM CARD#:
XXXXXXXXXXXX3962
01/29 46.00 DEBIT CARD PURCHASE AT CINCINNATI BETTER, CINCINNATI, OH ON 012824 FROM CARD#:
XXXXXXXXXXXX3962
01/29 50.00 RECURRING PURCHASE AT Spectrum, 855-707-7328, MO ON 012824 FROM CARD#: XXXXXXXXXXXX3541
01/29 287.79 MERCHANT PAYMENT RESTAURANT DEPOT - A61008 4501 W MITCHELL AVE CINCINNATI OH ON 012924
FROM CARD#: XXXXXXXXXXXX396X
01/29 7.81 MERCHANT PAYMENT MNRD-FLORENCE - 335902 5000 APEX LN FLORENCE KY ON 012924 FROM CARD#:
XXXXXXXXXXXX354X
01/29 130.92 MERCHANT PAYMENT SAMS CLUB #8133 - 330096 SAM'S Club FLORENCE KY ON 012924 FROM CARD#:
XXXXXXXXXXXX396X
01/30 34.61 DEBIT CARD PURCHASE AT SAMSCLUB #8133, FLORENCE, KY ON 012924 FROM CARD#:
XXXXXXXXXXXX3541
01/30 40.00 DEBIT CARD PURCHASE AT KY-SEC OF STATE, FRANKFORT, KY ON 012924 FROM CARD#:
XXXXXXXXXXXX3541
01/30 856.60 MERCHANT PAYMENT - 426880 PAYPAL *janikjozef San Jose CA ON 013024 FROM CARD#:
XXXXXXXXXXXX354X
01/31 2.97 EPX ST 032148241 MERCH SETL MERCH SETL 3130032148241 THE MAGNIFICENT CHILD 013124
Deposits / Credits 
7 items totaling $23,748.00
Date Amount Description
01/08 50.00 TUITIONEXPRESS PROC PMT 84870022296232 THE MAGNIFICENT CHILD 010824
01/09 1,707.00 KY FINANCE KYPAYMENTS 202401085917710 The Magnificent 010924
01/09 16,541.00 KY FINANCE KYPAYMENTS 202401085917616 The Magnificent 010924
01/16 200.00 TUITIONEXPRESS PROC PMT 84870022296232 THE MAGNIFICENT CHILD 011624
01/23 50.00 TUITIONEXPRESS PROC PMT 84870022296232 THE MAGNIFICENT CHILD 012324
01/24 5,000.00 5/3 JEANIE TRANSFER FROM CK2:XXXXXX3726 - 005601 1850 SEYMOUR AVE CINCINNATI OH
01/29 200.00 TUITIONEXPRESS PROC PMT 84870022296232 THE MAGNIFICENT CHILD 012924
""")

excel_transactions = extract_excel_transactions("""
Date Type Montant ($) Description Compte/Carte Catégorie Sous-catégorie
2024-01-30 Débit 1345,49 RESTAURANT DEPOT 3962 Autre Divers
2024-01-01 Débit 282,01 KROGER #4 CINCINNATIAuto Courses Kroger
2024-01-29 Débit 441,17 RESTAURANT DEPOT Auto Autre Divers
2024-01-25 Débit 820,14 DUKEENERGY BILL PAYAuto Utilities Electricité
2024-01-22 Débit 1403,35 PAYCHEX INC. PAYROLL3962 Ressources Humaines Salaires
2024-01-29 Débit 1222,62 DUKEENERGY BILL PAY3962 Utilities Electricité
2024-01-10 Débit 350,38 RUMPKE/WEB RECURRIAuto Autre Divers
2024-01-23 Débit 1046,56 KROGER #4 CINCINNATIAuto Courses Kroger
2024-01-28 Débit 709,48 STATE FARM INSURA 3541 Assurance Auto ou Locaux
2024-01-24 Débit 1392,05 RESTAURANT DEPOT Auto Autre Divers
2024-01-15 Débit 422,34 PAYCHEX INC. PAYROLL3541 Ressources Humaines Salaires
2024-01-21 Débit 563,09 RUMPKE/WEB RECURRIAuto Autre Divers
2024-01-03 Débit 214 RESTAURANT DEPOT 3962 Autre Divers
2024-01-07 Débit 647,1 SAM'S CLUB 3541 Courses Sam's Club
2024-01-09 Débit 704,49 KROGER #4 CINCINNATIAuto Courses Kroger
2024-01-09 Débit 1207,98 STATE FARM INSURA 3541 Assurance Auto ou Locaux
2024-01-30 Débit 1198,54 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-28 Débit 273,75 STATE FARM INSURA 3541 Assurance Auto ou Locaux
2024-01-09 Débit 518,1 SAM'S CLUB 3962 Courses Sam's Club
2024-01-01 Débit 1093,75 RESTAURANT DEPOT Auto Autre Divers
2024-01-06 Débit 178,46 SAM'S CLUB Auto Courses Sam's Club
2024-01-13 Débit 73,45 DUKEENERGY BILL PAY3541 Utilities Electricité
2024-01-06 Débit 1322,63 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-21 Débit 1201,93 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-22 Débit 485,87 RUMPKE/WEB RECURRI3962 Autre Divers
2024-01-08 Débit 1170,76 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-26 Débit 342,77 RESTAURANT DEPOT 3962 Autre Divers
2024-01-07 Débit 1046,97 KROGER #4 CINCINNATI3962 Courses Kroger
2024-01-07 Débit 1425,92 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-30 Débit 189,21 SAM'S CLUB Auto Courses Sam's Club
2024-01-24 Débit 1479,57 RUMPKE/WEB RECURRI3962 Autre Divers
2024-01-26 Débit 1363,54 SAM'S CLUB 3962 Courses Sam's Club
2024-01-08 Débit 923,9 RESTAURANT DEPOT Auto Autre Divers
2024-01-10 Débit 16,62 PAYCHEX INC. PAYROLL3541 Ressources Humaines Salaires
2024-01-19 Débit 1099,4 KROGER #4 CINCINNATI3541 Courses Kroger
2024-01-13 Débit 1391,6 PAYCHEX INC. PAYROLLAuto Ressources Humaines Salaires
2024-01-15 Débit 234,8 DUKEENERGY BILL PAY3541 Utilities Electricité
2024-01-21 Débit 1369,22 RESTAURANT DEPOT Auto Autre Divers
2024-01-06 Débit 207,88 DUKEENERGY BILL PAY3541 Utilities Electricité
2024-01-31 Débit 1174,03 STATE FARM INSURA Auto Assurance Auto ou Locaux
2024-01-06 Débit 718,96 RESTAURANT DEPOT 3541 Autre Divers
2024-01-16 Débit 887,61 SAM'S CLUB 3541 Courses Sam's Club
2024-01-25 Débit 21,84 RESTAURANT DEPOT 3962 Autre Divers
2024-01-05 Débit 147,18 RUMPKE/WEB RECURRI3541 Autre Divers
2024-01-07 Débit 136,85 PAYCHEX INC. PAYROLL3962 Ressources Humaines Salaires
2024-01-27 Débit 511,18 STATE FARM INSURA Auto Assurance Auto ou Locaux
2024-01-02 Débit 815,51 PAYCHEX INC. PAYROLL3541 Ressources Humaines Salaires
2024-01-20 Débit 784,76 RUMPKE/WEB RECURRIAuto Autre Divers
2024-01-05 Débit 1426,01 SAM'S CLUB 3541 Courses Sam's Club
2024-01-07 Débit 88,28 STATE FARM INSURA 3962 Assurance Auto ou Locaux
2024-01-19 Débit 511,1 PAYCHEX INC. PAYROLL3541 Ressources Humaines Salaires
2024-01-11 Débit 269,53 STATE FARM INSURA 3962 Assurance Auto ou Locaux
2024-01-28 Débit 657,16 PAYCHEX INC. PAYROLL3541 Ressources Humaines Salaires
2024-01-12 Débit 687,43 RUMPKE/WEB RECURRIAuto Autre Divers
2024-01-19 Débit 17,65 RUMPKE/WEB RECURRI3962 Autre Divers
2024-01-11 Débit 1119,94 STATE FARM INSURA 3541 Assurance Auto ou Locaux
2024-01-18 Débit 1434,09 PAYCHEX INC. PAYROLL3962 Ressources Humaines Salaires
2024-01-12 Débit 1082,54 DUKEENERGY BILL PAYAuto Utilities Electricité
2024-01-01 Débit 1110,43 KROGER #4 CINCINNATI3541 Courses Kroger
2024-01-01 Débit 1314,45 KROGER #4 CINCINNATIAuto Courses Kroger
2024-01-19 Débit 759,84 KROGER #4 CINCINNATI3541 Courses Kroger
2024-01-18 Débit 1101,58 RUMPKE/WEB RECURRI3962 Autre Divers
2024-01-05 Débit 1267,83 DUKEENERGY BILL PAY3962 Utilities Electricité
2024-01-20 Débit 939,95 DUKEENERGY BILL PAYAuto Utilities Electricité
2024-01-24 Débit 821,66 SAM'S CLUB Auto Courses Sam's Club
2024-01-15 Débit 1377,55 RESTAURANT DEPOT Auto Autre Divers
2024-01-02 Débit 746,72 RESTAURANT DEPOT 3962 Autre Divers
2024-01-08 Débit 

