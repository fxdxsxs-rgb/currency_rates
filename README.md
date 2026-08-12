# Currency Rates

Скрипт для получения курсов валют через внешнее API и сохранения их в JSON, CSV и XLSX форматах.

## Установка и запуск

### Требования
- Python 3.13

1. **Клонируйте репозиторий** и перейдите в папку проекта:
   ```
   git clone https://github.com/fxdxsxs-rgb/currency_rates.git
   cd currency_rates
2. **Создайте виртуальное окружение, установите зависимости**
    ```
    py -3.13 -m venv .venv
    .venv\Scripts\Activate.ps1 (Активация в Windows)
    source .venv/bin/activate (Активация в Linux
    
    python -m pip install --upgrade pip
    pip install -r requirements.txt

3. **Переименуйте файл .env.example в .env**
    ```
   Далее в переменную EXCHANGE_RATE_API_KEY нужно вставить API key,
   полученный на сайте https://www.exchangerate-api.com

4. **Запуск и тестирование**
    ```
    В главной папке(корне проекта) - python main.py для запуска приложения.
    В глайной папке(корне проекта) - python -m unittest tests/test_validator.py
   
5. **Структура проекта**
    ```
   currency_rates/           # Корень проекта
    ├── data/                # сохраняемые файлы (создаётся при первом запуске)
    │   ├── rates.csv - Создатся после запуска скрипта.
    │   ├── rates.json - Создатся после запуска скрипта.
    │   └── rates.xlsx - Создатся после запуска скрипта.
    ├── logs/                # логи работы (создаётся при первом запуске)
    │   └── app.log
    ├── tests/               # Тесты
    │   ├── __init__.py
    │   └── test_validator.py
    ├── .env.example         # шаблон для .env
    ├── .gitignore           # исключения для Git
    ├── api.py               # работа с внешним API
    ├── exporter.py          # экспорт в CSV/JSON/XLSX
    ├── logger.py            # настройка логирования
    ├── main.py              # точка входа(главный файл откуда всё запускается)
    ├── README.md
    ├── requirements.txt     # зависимости
    └── validator.py         # валидация ответа API