"""Dump textuel complet de l'app Revue + structure des contrôles."""
import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1600, "height": 1000})
        await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        await page.locator("button[title*='goulot mesure']").click()
        await page.wait_for_timeout(3000)
        # tous les éléments select/input/button avec leur libellé
        ctrls = await page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('select,input,button').forEach(el => {
                out.push({tag: el.tagName, type: el.type||'', ph: el.placeholder||'', val: el.value ? String(el.value).slice(0,30) : '', txt: (el.textContent||'').trim().slice(0,60)});
            });
            return out;
        }""")
        print("== CONTRÔLES ==")
        print(json.dumps(ctrls, ensure_ascii=False, indent=1))
        body = await page.inner_text("body")
        print("== BODY COMPLET ==")
        print(body)
        await browser.close()

asyncio.run(main())
