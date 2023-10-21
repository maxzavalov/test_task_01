import asyncio
import aiohttp
import numpy as np
import re


async def get_text(url: str) -> str:
    """Creates async session and get text from response."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except aiohttp.ClientError as ex:
        return f"ClientError {ex}"
    except TimeoutError as ex:
        return f"TimeoutError {ex}"


def text_to_array(text: str) -> np.array:
    """Filter numbers from text and makes square np.matrix."""
    filter_nums = re.findall(r"\d+", text)
    nums_list = [int(num) for num in filter_nums]
    size = int(len(nums_list) ** 0.5)
    return np.array(nums_list).reshape(size, size)


def matrix_to_list(matrix: np.array) -> list[int]:
    """Takes np.array and returns it's numbers in a spiral"""
    result = []
    while matrix.size > 0:
        matrix = np.rot90(matrix, -1)  # Rotate matrix to right.
        result.extend(matrix[0][::-1])  # Collect 1-st line from right to left.
        matrix = np.delete(matrix, 0, axis=0)  # Delete collected line.
    return result


async def get_matrix(url: str) -> list[int]:
    """Takes url, returns list of matrix numbers in a spiral"""
    if type(url) != str:
        raise TypeError("The get_matrix function is waiting for str argument.")
    pattern = r"^https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    if not re.search(pattern, url):
        raise ValueError("Argument of get_matrix() is not website address")
    text = await get_text(url)
    array = text_to_array(text)
    return matrix_to_list(array)


if __name__ == "__main__":
    asyncio.run(get_matrix(url))
