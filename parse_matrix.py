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
    size = int(len(nums_list) ** 0.5)
    return np.array(nums_list).reshape(size, size)


def matrix_to_list(matrix: np.array) -> list[int]:
    result = []
    while matrix.size > 0:
        matrix = np.rot90(matrix, -1)
        result.extend(matrix[0][::-1])
        matrix = np.delete(matrix, 0, axis=0)
    return result


async def get_matrix(url: str) -> list[int]:
    text = await get_text(url)
    array = text_to_array(text)
    return matrix_to_list(array)


if __name__ == "__main__":
    asyncio.run(get_matrix(url))
