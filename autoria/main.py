import csv
import random
from time import sleep

import requests

from bs4 import BeautifulSoup


def random_sleep():
    sleep(random.randint(2, 5))


def get_page_content(page: int, page_size: int = 100) -> str:
    query_parameters = {
        'indexName': 'auto,order_auto,newauto_search',
        'categories.main.id': '1',
        'country.import.usa.not': '-1',
        'price.currency': '1',
        'abroad.not': '0',
        'custom.not': '1',
        'page': page,
        'size': page_size,
    }
    response = requests.get('https://auto.ria.com/uk/search/', params=query_parameters)
    response.raise_for_status()
    return response.text


class CSVWriter:
    def __init__(self, filename, headers):
        self.filename = filename

        with open(filename, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

    def write(self, data):
        with open(self.filename, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)


class StdOutWriter:
    def write(self, data):
        print(data)


def main():
    headers = ['car_id', 'car_mark_name', 'data_link_to_view']
    writers = (
        CSVWriter('cars1.csv', headers),
        CSVWriter('cars2.csv', headers),
        # StdOutWriter(),
    )

    page = 0

    while True:

        print(f'Page: {page}')
        random_sleep()

        page_content = get_page_content(page)

        page += 1

        soup = BeautifulSoup(page_content, 'html.parser')

        search_results = soup.find('div', {'id': 'searchResults'})
        ticket_items = search_results.find_all('section', {'class': 'ticket-item'})

        if not ticket_items:
            break

        for ticket_item in ticket_items:
            car_details = ticket_item.find('div', {'class': 'hide'})
            car_id = car_details['data-id']
            car_mark_name = car_details['data-mark-name']

            data_link_to_view = car_details['data-link-to-view']

            data = [car_id, car_mark_name, data_link_to_view]

            for writer in writers:
                writer.write(data)


if __name__ == '__main__':
    main()
