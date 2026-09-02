"""Test UI Revue : onglet Contradictions (filtres statut/date, badge A SOURCER) + clic item -> panneau detail."""
import asyncio, json
from playwright.async_api import async_playwright

R = {}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1600, "height": 1000})
        errs = []
        page.on("pageerror", lambda e: errs.append(f"pageerror: {e}"))
        await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        await page.locator("button[title*='goulot mesure']").click()
        await page.wait_for_timeout(2500)
        # onglet Contradictions
        await page.get_by_text("Contradictions (204/204)").click()
        await page.wait_for_timeout(2500)
        body = await page.inner_text("body")
        R["contradictions"] = {
            "filtre_statut": "statut" in body.lower(),
            "filtre_domaine": "domaine" in body.lower(),
            "filtre_date": "jours" in body.lower() or "90 derniers" in body.lower() or "date" in body.lower(),
            "badge_A_SOURCER": "A SOURCER" in body,
            "progression": "204" in body,
        }
        # clic sur le premier element cliquable de la liste (pas un onglet)
        items = page.locator("button:has-text('•')")
        R["nb_items"] = await items.count()
        if await items.count():
            await items.first.click()
            await page.wait_for_timeout(2000)
            body2 = await page.inner_text("body")
            R["detail_ouvert"] = len(body2) > len(body) + 80
            R["proposer_reponse"] = ("proposer" in body2.lower()) or ("réponse" in body2.lower()) or ("reponse" in body2.lower())
            R["detail_extrait"] = body2[-800:]
        R["erreurs"] = errs[:5]
        print(json.dumps(R, ensure_ascii=False, indent=1))
        await browser.close()

asyncio.run(main())
