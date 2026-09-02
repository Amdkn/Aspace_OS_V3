"""Test UI live port 5555 — app Revue (Agent OS desktop).
Vérifie : page chargée, root React rendu, app Revue présente, erreurs console.
"""
import asyncio, json
from playwright.async_api import async_playwright

RESULTS = {}

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
        resp = await page.goto("http://127.0.0.1:5555/", wait_until="networkidle", timeout=30000)
        RESULTS["http_status"] = resp.status
        RESULTS["title"] = await page.title()
        RESULTS["root_children"] = await page.evaluate("document.getElementById('root').children.length")
        body = await page.inner_text("body")
        RESULTS["body_len"] = len(body)
        RESULTS["body_head"] = body[:500]
        RESULTS["revue_mention"] = "Revue" in body
        RESULTS["asourcer_badge"] = "A SOURCER" in body
        RESULTS["progression"] = ("/" in body)
        await page.screenshot(path="C:/Users/amado/ASpace_OS_V3/50_Distillation/ui-5555.png")
        RESULTS["page_errors"] = errors[:10]
        await browser.close()

asyncio.run(main())
print(json.dumps(RESULTS, ensure_ascii=False, indent=1))
