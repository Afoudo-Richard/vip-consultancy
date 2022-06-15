from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def book_consultation(request):
    msg_html = render_to_string('custom-email.html', {'name': "Richard Arc"})
    # send_mail(
    #     subject='Hello from ArcTest on VIP consultanc cameroon',
    #     message='A stunning message',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=['richardafoudo07@gmail.com'],
    #     html_message=msg_html,
    #     )

    email = EmailMessage("Test from my Arc", msg_html, settings.EMAIL_HOST_USER, ['richardafoudo07@gmail.com'])
    email.fail_silently = True
    email.content_subtype = "html"
    #email.send()
    return render(request, 'book-consultation.html')
