import httpx
from bs4 import BeautifulSoup

async def main():
    url = "https://jobinja.ir/jobs"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        # Parse HTML content using lxml parser
        soup = BeautifulSoup(response.content, "lxml")

        # Find and extract specific elements using Beautiful Soup
        title = soup.title.text
        paragraphs = [p.text.strip() for p in soup.find_all("a")]

        # Print the title and paragraphs
        print("Title:", title)
        print("Paragraphs:")
        for paragraph in paragraphs:
            print(paragraph)
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

# Run the main coroutine
import asyncio
asyncio.run(main())


    