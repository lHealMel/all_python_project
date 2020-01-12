from bs4 import BeautifulSoup
from urllib.request import urlopen

url = open("C:/Users/mtn20/Desktop/imgfind.txt", 'a')

html = urlopen(
    "http://sscoach.kr/xe/?mid=board_gLSI95&document_srl=36339&order_type=asc&sort_index=regdate&listStyle=viewer")

bsObject = BeautifulSoup(html, "html.parser")

file_found = bsObject.find_all('img')

print(bsObject)
print('--------------------')
print((file_found))
print('--------------------')
bs = BeautifulSoup(html, 'html.parser')