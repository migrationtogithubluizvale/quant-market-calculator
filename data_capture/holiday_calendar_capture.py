import asyncio
import os
from playwright.async_api import async_playwright
import pandas as pd

class HolidayCalendarCapture:
    def __init__(self, env):
        self.env = env

    # Handle the file download and save it to the specified path
    async def handle_download(self, download):
        download_path = os.path.join(os.getcwd(), "feriados.xls")
        await download.save_as(download_path)

    # Main asynchronous method that captures the holiday calendar
    async def resolve(self):
        try:
            # Launch the browser using playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                await page.goto(self.env.HOLIDAY_CALENDAR_URL)
                
                # Register the download event handler
                page.on("download", lambda download: self.handle_download(download))
    
                # Click the link to start the download
                await page.click('a.linkinterno:text("feriados_nacionais.xls")')
    
                # Wait for a few seconds to make sure the file has started downloading
                await asyncio.sleep(5)
    
                # Close the browser
                await browser.close()
    
            # Read the 'feriados.xls' file using pandas
            df = pd.read_excel("feriados.xls")

        finally:
            # Remove the downloaded file (optional)
            if os.path.exists("feriados.xls"):
                os.remove("feriados.xls")

        return df

    # Run the asynchronous resolve method and return the resulting DataFrame
    def run(self):
        df = asyncio.run(self.resolve())
        return df
