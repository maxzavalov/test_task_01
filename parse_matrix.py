import asyncio
import aiohttp
import numpy as np
import re


async def get_text(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def text_to_array(text: str) -> np.array:
    filter_nums = re.findall(r'\d+', text)
    nums_list = [int(num) for num in filter_nums]
    size = len(nums_list) ** 0.5
    return np.array(nums_list).reshape(size, size)


url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


async def test_get_text(url):
    text = await get_text(url)
    print(text)
    return text


asyncio.run(test_get_text(url))
