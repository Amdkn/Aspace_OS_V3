"""Onglet Contradictions : dump contrôles + body, puis clic sur un item."""
import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1600, "height": 1000})
        await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        await page.locator("button[title*='goulot mesure']").click()
        await page.wait_for_timeout(2500)
        await page.get_by_text("Contradictions (204/204)").click()
        await page.wait_for_timeout(2500)
        ctrls = await page.evaluate("""() => {
            const out = [];
            document.querySelectorAll('select,input,button').forEach(el => {
                const t = (el.textContent||'').trim();
                if (el.tagName !== 'BUTTON' || (t && t.length < 70 && !/^(Agent OS|Fichier|Édition|Affichage|Fenêtre|Observateurs|Mémoires|Agentic|Coach|Life|Corpus|Revue|Passerelles)/.test(t)))
                    out.push({tag: el.tagName, type: el.type||'', ph: el.placeholder||'', txt: t.slice(0,60)});
            });
            return out;
        }""")
        print("== CONTRÔLES (onglet Contradictions) ==")
        print(json.dumps(ctrls, ensure_ascii=False, indent=1))
        body = await page.inner_text("body")
        print("== BODY (excerpt) ==")
        print(body[:3000])
        await browser.close()

asyncio.run(main())
