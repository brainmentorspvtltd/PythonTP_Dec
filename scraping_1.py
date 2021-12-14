import urllib.request as url
import bs4

response = url.urlopen("https://www.flipkart.com/u-i-alarm-series-40hrs-music-time-wireless-neckband-earphone-bluetooth-headset/product-reviews/itmcd4643541e5b7?pid=ACCG6XTJTVPKCRJX&lid=LSTACCG6XTJTVPKCRJXHCJNUE&marketplace=FLIPKART")
page_html = bs4.BeautifulSoup(response, "lxml")
page_html.find('p', class_='_2-N8zT')
# review = page_html.find('p', class_='_2-N8zT')
# print(review.text)

reviewList = page_html.find_all('p', class_='_2-N8zT')
for i in range(len(reviewList)):
    print(reviewList[i].text)
