from parse_matrix import get_matrix

url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
text = await get_matrix(url)
print(text)