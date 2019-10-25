import requests
from bs4 import BeautifulSoup

ratings_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}


def get_products_from_page(url):
    r = requests.get(url)
    html = ''
    result = []

    if r.ok:
        html = r.content

    soup = BeautifulSoup(html, 'lxml')
    books = soup.find_all('article', class_="product_pod")

    for book in books:
        try:
            image = 'http://books.toscrape.com/' + book.find('img').get('src')
        except:
            image = ''

        try:
            in_stock = book.find(
                'p', class_="instock").text.strip() == 'In stock'
        except:
            in_stock = False

        try:
            name = book.find('h3').find('a').text.strip()
        except:
            name = ''

        try:
            price = book.find('div', class_="product_price").find(
                'p', class_="price_color").text.strip()
        except:
            price = ''

        try:
            rating_class_list = book.find(
                'p', class_="star-rating").get('class')
            rating = ratings_dict[rating_class_list[1]]
        except:
            rating = None

        result.append({
            'image': image,
            'in_stock': in_stock,
            'name': name,
            'price': price,
            'rating': rating
        })

    return result
