"""Test final Revue : cliquer une contradiction (filter 'ouvertes' pour badge A SOURCER) et verifier le panneau detail + proposerReponse."""
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
        await page.wait_for_timeout(2000)
        await page.get_by_text("Contradictions (204/204)").click()
        await page.wait_for_timeout(2000)
        # filtre 'ouvertes' pour tenter d'attraper un badge A SOURCER
        await page.get_by_role("button", name="ouvertes", exact=True).click()
        await page.wait_for_timeout(2000)
        body = await page.inner_text("body")
        R["badge_A_SOURCER_ouvertes"] = "A SOURCER" in body
        R["nb_ouvertes_extrait"] = body[body.find("FILTRER"):body.find("FILTRER")+300] if "FILTRER" in body else ""
        # revenir a toutes et cliquer la premiere contradiction
        await page.get_by_role("button", name="toutes").first.click()
        await page.wait_for_timeout(1500)
        items = page.locator("button:has-text('Arbitré')").first
        await items.click()
        await page.wait_for_timeout(2000)
        body2 = await page.inner_text("body")
        R["detail_ouvert"] = len(body2) > len(body)
        R["badge_A_SOURCER_apres_clic"] = "A SOURCER" in body2
        R["detail_extrait"] = body2[-1000:]
        R["erreurs"] = errs[:5]
        print(json.dumps(R, ensure_ascii=False, indent=1))
        await browser.close()

asyncio.run(main())
