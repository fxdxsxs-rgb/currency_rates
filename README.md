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
    source .venv/bin/activate (Активация в Linux)
    
    python -m pip install --upgrade pip
    pip install -r requirements.txt

3. **Переименуйте файл .env.example в .env**
    ```
   Далее в переменную EXCHANGE_RATE_API_KEY нужно вставить API key,
   полученный на сайте https://www.exchangerate-api.com

4. **Запуск и тестирование**
    ```
    В главной папке(корне проекта) - python main.py для запуска приложения.
   
    Опционально:
    В главной папке(корне проекта) - python -m unittest tests/test_validator.py
   
5. **Структура проекта**
    ```
   currency_rates/           # Корень проекта
    ├── data/                # Сохраняемые файлы (создаётся при первом запуске)
    │   ├── rates.csv - Создастся после запуска скрипта.
    │   ├── rates.json - Создастся после запуска скрипта.
    │   └── rates.xlsx - Создастся после запуска скрипта.
    ├── logs/                # Логи работы (создаётся при первом запуске)
    │   └── app.log
    ├── tests/               # Тесты
    │   ├── __init__.py
    │   └── test_validator.py
    ├── .env.example         # Шаблон для .env
    ├── .gitignore           # Исключения для Git
    ├── api.py               # Работа с внешним API
    ├── exporter.py          # Экспорт в CSV/JSON/XLSX
    ├── logger.py            # Настройка логирования
    ├── main.py              # Точка входа(главный файл откуда всё запускается)
    ├── README.md
    ├── requirements.txt     # Зависимости
    └── validator.py         # Валидация ответа API