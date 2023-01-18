

from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render

from templated_mail.mail import BaseEmailMessage

from .tasks import notify_customers


def say_hello(request):

    context = {'name': 'Mosh'}

    notify_customers.delay('hello')

    try:

        message = BaseEmailMessage(template_name='emails/hello.html', context=context)
        message.send(['bob@moshbuy.com'])

        # message = EmailMessage('subject', 'message', 'info@moshbuy.com', ['bob@moshbuy.com'])
        # message.attach_file('playground/static/images/dog.jpeg')
        # message.send()

        # send_mail('subject', 'message', 'info@moshbuy.com', ['bob@moshbuy.com'])

        # mail_admins('subject', 'message', html_message='message')

    except BadHeaderError:
        pass

    return render(request, 'hello.html', context)
