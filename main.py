from flask import Flask
import random
app = Flask(__name__)
moneta = ['Орел', 'Решка']
facts_list = ['Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс когда они находятся вне зоны покрытия сети или не могут использовать свои устройства',
              'Согласно исследованию, проведенному в 2018 году,более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов',
              'Изучение технологической зависимости является одной из наиболее актуальных областей научныхисследований в настоящее время']
@app.route("/")
def hello_world():
    return f"""Привет! <br> <a href=/random_fact>Посмотреть случайный факт! </a> <br> <a href=/brosok_monety>Бросить монету! </a>"""

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/brosok_monety")
def brosok_monety():
    return f'<p>{random.choice(moneta)}</p>'
app.run(debug=True)
