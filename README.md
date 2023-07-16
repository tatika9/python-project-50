## Hexlet tests and linter status:
[![Actions Status](https://github.com/tatika9/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/tatika9/python-project-50/actions) ![Python CI](https://github.com/tatika9/python-project-50/actions/workflows/pyci.yml/badge.svg) [![Maintainability](https://api.codeclimate.com/v1/badges/8e33bbf7f83d7d73d204/maintainability)](https://codeclimate.com/github/tatika9/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/8e33bbf7f83d7d73d204/test_coverage)](https://codeclimate.com/github/tatika9/python-project-50/test_coverage)

## Описание
«Вычислитель отличий» — программа, которая определяет разницу между двумя древовидными структурами данных. Можно использовать как утилиту командной строки либо как библиотеку.
Поддерживает входные типы файлов: `*.json` `*.yml` `*.yaml`.
Возвращает результат в одном из трех форматов: `stylish` `plain` `json`.
## Требования
* Python ^3.9
* Poetry ^1.4.2
## Зависимости
* PyYAML = ^6.0
## Установка
1. Клонируем гит-репозиторий:
```bash
$ git clone git@github.com:tatika9/python-project-50.git
```
2. Из корня проекта выполняем команду для установки пакета в пользовательское окружение:
```bash
$ make install
```
## Использование
Из командной строки:
* `$ gendiff -h` вывод справки по программе
* `$ gendiff file1.json file2.json` вывод различий в формате `stylish` (используется по умолчанию)
* `$ gendiff file1.json file2.yaml -f plain` вывод различий в формате `plain`
* `$ gendiff file1.yaml file2.yaml -f json` вывод различий в формате `json`

Как библиотеку:
```python
from gendiff import generate_diff


diff = generate_diff(file1, file2)
print(diff)
```
## Пример
[![asciicast](https://asciinema.org/a/zcz7CAsI1IMxVXiF1M9eKiHZN.svg)](https://asciinema.org/a/zcz7CAsI1IMxVXiF1M9eKiHZN)