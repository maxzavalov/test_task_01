import asyncio
import aiohttp


async def get_text(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


async def test_get_text(url):
    text = await get_text(url)
    print(text)
    return text


asyncio.run(test_get_text(url))
