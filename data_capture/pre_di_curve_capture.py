import asyncio
from playwright.async_api import async_playwright
from data_capture._basic_capture import Capture

class PreDiCurveCapture(Capture):
    def __init__(self, env):
        self.url = env.TAXA_REFERENCIAL_URL

    # Get data from the table in the iframe using the css_selector, column, and index
    async def get_data_from_table(self, iframe, css_selector, column, index):
        return await iframe.evaluate(f'(index) => document.querySelectorAll("{css_selector}")[index].querySelector("td:nth-child({column})").textContent', index)

    # Process a single row of the table
    async def process_row(self, iframe, index):
        css_selector = "tbody tr"
        day = await self.get_data_from_table(iframe, css_selector, 1, index)
        tax_252 = await self.get_data_from_table(iframe, css_selector, 2, index)
        tax_360 = await self.get_data_from_table(iframe, css_selector, 3, index)
        return {'dc': day, 'Du252': tax_252, 'Du360': tax_360}

    async def resolve(self, date):
        super().resolve()

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(self.url)

            iframe_element = await page.wait_for_selector("#bvmf_iframe")
            iframe = await iframe_element.content_frame()

            element = await iframe.wait_for_selector("#Data")

            await element.fill(date)

            ok_button = iframe.locator('text=OK')
            await ok_button.click()

            await page.wait_for_selector("#bvmf_iframe")

            iframe_element = await page.wait_for_selector("#bvmf_iframe")
            iframe = await iframe_element.content_frame()

            table_selector = "#tb_principal1"

            tbody = iframe.locator(f'{table_selector} tbody tr')
            rows = await tbody.element_handles()

            await asyncio.sleep(3)

            taxes = []
            tasks = []

            # Create tasks to process each row asynchronously
            for index, row in enumerate(rows):
                task = asyncio.create_task(self.process_row(iframe, index))
                tasks.append(task)

            max_tasks = 5
            # Execute tasks in chunks to avoid overloading
            for chunk in range(0, len(tasks), max_tasks):
                completed_tasks = await asyncio.gather(*tasks[chunk:chunk + max_tasks])
                taxes.extend(completed_tasks)

            await browser.close()

            return taxes

    async def run(self, date):

        taxas = await self.resolve(date)

        return taxas
