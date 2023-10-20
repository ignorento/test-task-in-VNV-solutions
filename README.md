# test-task-in-VNV-solutions

## Початок роботи

### 1. Передумови

    Python 3.10
    Django 4.2

### 2. Інсталяція
1. Склонуйте репозиторій:

   ```bash
   git clone https://github.com/ignorento/test-task-in-VNV-solutions.git
   cd test-task-in-VNV-solutions
   
2. Створіть віртуальне оточення(опціонально, але рекомендовано):
    
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate

3. Встановіть залежності проекту:
    
    ```bash
   pip install -r requirements.txt
   
4. Мігруйте базу даних та створіть суперюзера:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser

5. Запустіть сервер для розробки:
    ```bash
   python manage.py runserver
