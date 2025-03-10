# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка
Вам понадобится установленный Python 3.7.1+ и git.

Склонируйте репозиторий:
```bash
$ git clone https://github.com/valeriy131100/wine
```

Создайте в этой папке виртуальное окружение:
```bash
$ cd wine
$ python3 -m venv venv
```

Активируйте виртуальное окружение и установите зависимости:
```bash
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Использование
Заполните файл .env.example и переименуйте его в .env или иным образом задайте переменную среды WINES_PATH - путь до .xlsx-файла содержащего информацию о винах. Информация о винах должна быть представлена в формате:

Категория | Название | Сорт | Цена | Картинка | Акция
--- | --- | --- | --- | --- | ---
Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
Напитки | Коньяк классический | | 499 | rkaciteli.png |

Из акций в настоящий момент доступна лишь "Выгодное предложение". Файл картинки должен находится в папке images.

Находясь в директории wine исполните:
```bash
$ venv/bin/python main.py
```

Перейдите на сайт по адресу http://127.0.0.1:8000/
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
