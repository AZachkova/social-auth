# Social auth

Social auth - это джанго приложение, разработанное в качестве тестового задания. Оно удовлетворяет заданным условиям:
1) Необходимо сделать регистрацию юзеров с помощью social auth: Google или Github на выбор (я выбрала Github).
2) После регистрации нужно попросить юзера заполнить информацию о себе: ФИО, загрузить аватар и информацию о себе. После заполнения, поля должны быть сохранены и выдаваться при следующих открытиях страницы/авторизациях с возможностью редактирования.

Опционально: сделать страницу со списком всех юзеров, зарегистрированных в системе и информацией о них.



## Installation

Перейдите в директорию, в которой находится requirements.txt. Cоздайте и активируйте виртуальное окружение virtualenv.

```bash
python3 -m venv env
source env/bin/activate
```
Установите все нужные пакеты.
```bash
pip install -r requirements.txt 
```
Создайте файл local_settings.py и поместите в него: SECRET_KEY, SOCIAL_AUTH_GITHUB_KEY и SOCIAL_AUTH_GITHUB_SECRET.
```bash
touch social_auth/local_settings.py 
```
Запустите проект.
```bash
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver 
```


