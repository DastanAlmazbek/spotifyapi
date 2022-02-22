from ast import Return
from django.core.mail import send_mail

from spotifyapi.celery import app

@app.task
def notify_user(email):
    send_mail(
        'Вы добавили отзыв на песню!',
        'Спасибо за использование нашего сайта!',
        'test@gmail.com',
        [email]
    )
    return 'Sucess'
