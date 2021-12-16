import urllib.request as url
import bs4

for num in range(1,3):
    response = url.urlopen(f"https://www.flipkart.com/u-i-alarm-series-40hrs-music-time-wireless-neckband-earphone-bluetooth-headset/product-reviews/itmcd4643541e5b7?pid=ACCG6XTJTVPKCRJX&lid=LSTACCG6XTJTVPKCRJXHCJNUE&marketplace=FLIPKART&page={num}")
    page_html = bs4.BeautifulSoup(response, "lxml")
    # review = page_html.find('p', class_='_2-N8zT')
    # print(review.text)

    reviewList = page_html.find_all('p', class_='_2-N8zT')
    ratingList = page_html.find_all('div', class_='_3LWZlK _1BLPMq')
    for i in range(len(reviewList)):
        print(ratingList[i].text, reviewList[i].text)
