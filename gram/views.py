from django.shortcuts import render,redirect
from .forms import NewsLetterForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.



# def news_today(request):
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']
#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             HttpResponseRedirect('news_today')
#     else:
#         form = NewsLetterForm()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})