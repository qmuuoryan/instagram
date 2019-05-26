from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to Instagram'

    sender = 'ryanmuuo91@gmail.com'

    #passing in the context variables
    text_content = render_to_string('email/gramemail.txt',{"name": name})
    html_content = render_to_string('email/gramemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender[receiver])
    mg.attach_alternative(html_content,'text/html')
    msg.send