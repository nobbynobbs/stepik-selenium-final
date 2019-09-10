# Stepik Selenium Cource Final Project - Page Object Pattern

[ссылко](https://stepik.org/lesson/238819/)

## Комментарии к решению

Структура проекта немного изменена по сравнению с предлагаемой на Степике:
в корневом каталоге отсутствуют файлы с тестами, они перемещены в папку `tests`.
Так мы получаем стандартную для питона структуру проекта.

## Запуск тестов

### Подготовка окружения
в чистом виртуальном окружении нужно выполнить команду
```
pip install -r requirements.txt -c constraints.txt
```

### Запуск pytest

Из корня проекта выполнить команду:

```
python -m pytest -v --tb=line -m need_review --language=en --headless
```

`--headless` и `--language` - необязательные аргументы

**NB! Так как мы убрали файлы из корня проекта
важно запускать тесты именно командой `python -m pytest`
Это нужно чтобы добавить текущий каталог в sys.path**


Если у вас ОС linux, то доступны команды:

```
make review-tests  # запуск тестов, помеченных как need_review
make all-tests-headless  # запуск всех тестов с использованием headless браузера
make all-tests  # запуск всех тестов
```
