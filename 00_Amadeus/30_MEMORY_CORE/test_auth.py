import sys, os, asyncio, json
sys.path.insert(0, 'C:/Users/amado/AppData/Roaming/Python/Python314/site-packages')

async def main():
    from playwright.async_api import async_playwright
    p = await async_playwright().start()
    browser = await p.chromium.launch(
        headless=True,
        args=["--disable-blink-features=AutomationControlled"]
    )
    
    storage_state = r'C:\Users\amado\.notebooklm\profiles\default\storage_state.json'
    print(f"[*] Utilisation du fichier d'état : {storage_state}")
    
    context = await browser.new_context(
        storage_state=storage_state if os.path.exists(storage_state) else None,
        viewport={"width": 1280, "height": 800}
    )
    
    page = await context.new_page()
    print("[*] Connexion à NotebookLM...")
    await page.goto("https://notebooklm.google.com/", wait_until="networkidle", timeout=45000)
    await asyncio.sleep(5)
    
    url = page.url
    title = await page.title()
    print(f"[+] URL actuelle : {url}")
    print(f"[+] Titre actuel : {title}")
    
    # Prendre un screenshot pour voir si on est connecté ou non
    screenshot_path = r'C:\Users\amado\ASpace_OS_V2\00_Amadeus\30_MEMORY_CORE\notebooklm_test.png'
    await page.screenshot(path=screenshot_path)
    print(f"[+] Capture d'écran sauvegardée à : {screenshot_path}")
    
    # Tenter de trouver les boutons ou textes indiquant si on est sur la grille des notebooks
    try:
        notebook_elements = await page.locator("a").all()
        notebooks = []
        for el in notebook_elements:
            href = await el.get_attribute("href")
            if href and "/notebook/" in href:
                text = await el.inner_text()
                notebooks.append((href, text.strip()))
        print(f"[+] Lignes de notebooks trouvées : {notebooks}")
    except Exception as e:
        print(f"[-] Erreur de recherche d'éléments : {e}")
        
    await context.close()
    await browser.close()
    p.stop()

if __name__ == "__main__":
    asyncio.run(main())
