import os
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from itertools import groupby
from operator import itemgetter

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def format_winery_age(age):
    if len(str(age)) > 1:
        penultimate_number = int(str(age)[-2])
    else:
        penultimate_number = 0

    if penultimate_number == 1:
        return f'{age} лет'

    last_number = int(str(age)[-1])

    if last_number == 1:
        return f'{age} год'
    elif 1 < last_number < 5:
        return f'{age} года'
    else:
        return f'{age} лет'


if __name__ == '__main__':
    load_dotenv()
    wines_filepath = os.getenv('WINES_PATH')

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    wines_df = read_excel(wines_filepath).fillna(value='').rename(
        columns={
            'Категория': 'category',
            'Название': 'name',
            'Сорт': 'sort',
            'Цена': 'price',
            'Картинка': 'image',
            'Акция': 'promotion'
        }
    )

    sorted_wines = sorted(
        wines_df.to_dict('records'),
        key=itemgetter('category')
    )
    grouped_wines = groupby(
        sorted_wines,
        key=itemgetter('category')
    )

    now_year = datetime.now().year
    foundation_year = 1920
    winery_age = now_year - foundation_year

    rendered_page = template.render(
        formatted_age=format_winery_age(winery_age),
        grouped_wines=grouped_wines
    )

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
