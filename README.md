# Scrapy Parser Pep
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)

## Описание
#### Асинхронный парсер позволяет собирать данные обо все документах PEP, сравнивать статусы на страницах PEP, считать общее количество документов PEP и сохранять результаты в табличном виде в csv-файл.

### Автор проекта:

[Артем Куркин](https://github.com/ArtyKurkin)

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/ArtyKurkin/scrapy_parser_pep.git
```
```
cd scrapy_parser_pep
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate 
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Запуск парсера:
```
scrapy crawl pep
```
После запуска парсера в директории `'results/'` формируется два файла с результатами работы:
1. 'Номер', 'Название' и 'Статус' PEP
2. 'Статус', 'Количество' и 'Общее число документов' PEP
