from django.shortcuts import render,redirect
from .forms import NewsLetterForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.



# if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']

#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('news_today')
#             #.................
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})


# @login_required(login_url='/accounts/login/')
# def article(request, article_id):
