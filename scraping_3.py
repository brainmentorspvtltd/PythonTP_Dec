import bs4
import urllib.request as url

product = input("Enter Product Name : ")
product = product.replace(" ", "+")
for num in range(1,4):
    path = f"https://www.flipkart.com/search?q={product}&page={num}"
    response = url.urlopen(path)
    html = bs4.BeautifulSoup(response, 'lxml')
    productNames = html.find_all('div', class_='_4rR01T')
    productPrice = html.find_all('div', class_='_30jeq3 _1_WHN1')

    for i in range(len(productNames)):
        print(productNames[i].text)
        print(productPrice[i].text)