"""Test UI live 5555 — ouvre Revue via le bouton dock (title exact) et vérifie les 4 mods du work 13."""
import asyncio, json, re
from playwright.async_api import async_playwright

R = {}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda m: errors.append(f"console.error: {m.text}") if m.type == "error" else None)
        await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        btn = page.locator("button[title*='goulot mesure']")
        await btn.click()
        await page.wait_for_timeout(3000)
        body = await page.inner_text("body")
        R["body_len"] = len(body)
        R["badge_A_SOURCER"] = "A SOURCER" in body
        R["filtre_statut"] = "statut" in body.lower()
        R["filtre_domaine"] = "domaine" in body.lower()
        R["filtre_date"] = "jours" in body.lower() or "90" in body
        m = re.search(r"\b(\d+)\s*/\s*(\d+)\b", body)
        R["progression_X_N"] = m.group(0) if m else None
        R["arbitrer"] = "arbitr" in body.lower()
        items = page.locator("[class*='cursor-pointer']")
        R["items_clicables"] = await items.count()
        R["erreurs"] = errors[:10]
        await page.screenshot(path="C:/Users/amado/ASpace_OS_V3/50_Distillation/ui-revue-5555.png", full_page=True)
        # clic sur le premier item -> panneau détail
        if await items.count():
            await items.first.click()
            await page.wait_for_timeout(2000)
            body2 = await page.inner_text("body")
            R["panneau_detail_ouvert"] = len(body2) > len(body) + 80
            R["detail_extrait"] = body2[-600:]
            await page.screenshot(path="C:/Users/amado/ASpace_OS_V3/50_Distillation/ui-revue-detail.png", full_page=True)
        print(json.dumps(R, ensure_ascii=False, indent=1))
        await browser.close()

asyncio.run(main())
