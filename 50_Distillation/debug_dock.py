"""Debug : dump le DOM du dock pour trouver le vrai sélecteur de Revue."""
import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(1500)
        html = await page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('[title],[data-app],[data-id],button,[role=button],[role=tab]').forEach(el => {
                out.push({tag: el.tagName, title: el.getAttribute('title'), cls: (el.className||'').toString().slice(0,80), txt: (el.textContent||'').trim().slice(0,40)});
            });
            return out.slice(0, 60);
        }""")
        print(json.dumps(html, ensure_ascii=False, indent=1))
        await browser.close()

asyncio.run(main())
