import requests
from bs4 import BeautifulSoup

link = "https://cbr.ru/"
response = requests.get(link).text
soup = BeautifulSoup(response, "lxml")
block = soup.find('div', class_ = 'main-indicator_rates-table')
block_currency = block.find_all('div', class_ = 'main-indicator_rate')

# Получаем блок с датой
block_date = soup.find('div', class_ = 'main-indicator_rates-head')
date = block_date.find_all('div', class_ = 'col-md-2 col-xs-7 _left')
date1 = date[0].text
date2 = date[1].text

# Получаем блок с курсом CNY
block_cny = block_currency[0]
cny = block_cny.find_all('div', class_ = 'col-md-2 col-xs-9 _left mono-num')
day1 = f'{date1}: {cny[0].text}'
day2 = f'{date2}: {cny[1].text}'
print("Курс CNY на", day1)
print("Курс CNY на", day2)

# Получаем блок с курсом USD
block_cny = block_currency[1]
usd = block_cny.find_all('div', class_ = 'col-md-2 col-xs-9 _left mono-num')
day1 = f'{date1}: {usd[0].text}'
day2 = f'{date2}: {usd[1].text}'
print("Курс USD на", day1)
print("Курс USD на", day2)

# Получаем блок с курсом EUR
block_cny = block_currency[2]
eur = block_cny.find_all('div', class_ = 'col-md-2 col-xs-9 _left mono-num')
day1 = f'{date1}: {eur[0].text}'
day2 = f'{date2}: {eur[1].text}'
print("Курс EUR на", day1)
print("Курс EUR на", day2)

# Создаем HTML-страницу с таблицей
css = """<style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 24px auto;
            padding: 0 16px;
            color: #222;
            background: #f5f7fb;
        }
        h1 {
            font-size: 1.8rem;
            margin-bottom: 0.2rem;
        }
        p {
            margin-top: 0;
            color: #555;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: #fff;
        }
        th, td {
            border: 1px solid #d1d5db;
            padding: 12px 14px;
            text-align: left;
        }
        th {
            background: #f3f4f6;
        }
        tr:nth-child(even) {
            background: #fafafa;
        }
    </style>
    """
html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Курсы ЦБ РФ</title>
    {css}
</head>
<body>
    <h1>Курсы ЦБ РФ</h1>
    <p>Здесь будут отображаться те же значения, что выводит ваш скрипт в консоль:</p>
    <table>
        <thead>
            <tr>
                <th>Валюта</th>
                <th>Дата</th>
                <th>Курс</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>CNY</td>
                <td>{date1}</td>
                <td>{cny[0].text}</td>
            </tr>
            <tr>
                <td>CNY</td>
                <td>{date2}</td>
                <td>{cny[1].text}</td>
            </tr>
            <tr>
                <td>USD</td>
                <td>{date1}</td>
                <td>{usd[0].text}</td>
            </tr>
            <tr>
                <td>USD</td>
                <td>{date2}</td>
                <td>{usd[1].text}</td>
            </tr>
            <tr>
                <td>EUR</td>
                <td>{date1}</td>
                <td>{eur[0].text}</td>
            </tr>
            <tr>
                <td>EUR</td>
                <td>{date2}</td>
                <td>{eur[1].text}</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

with open("rates.html", "w", encoding="utf-8") as f:
    f.write(html)   