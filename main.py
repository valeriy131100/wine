from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime


def format_winery_age(age):
    str_age = str(age)

    if len(str_age) > 1:
        penultimate_number = int(str_age[-2])
    else:
        penultimate_number = 0

    if penultimate_number == 1:
        return f'{age} лет'

    last_number = int(str_age[-1])

    if last_number == 1:
        return f'{age} год'
    elif 1 < last_number < 5:
        return f'{age} года'
    else:
        return f'{age} лет'


if __name__ == '__main__':
    wines = read_excel('wine.xlsx').rename(
        columns={
            'Название': 'name',
            'Сорт': 'sort',
            'Цена': 'price',
            'Картинка': 'image'
        }
    )

    print(wines)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    now_year = datetime.now().year
    foundation_year = 1920
    winery_age = now_year - foundation_year

    rendered_page = template.render(
        formatted_age=format_winery_age(winery_age),
        wines=wines.to_dict('records')
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
