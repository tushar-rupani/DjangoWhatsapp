from django.shortcuts import render, redirect
import pywhatkit as py
from django.core.mail import EmailMultiAlternatives, EmailMessage
from .models import SendEmail
from email.mime.image import MIMEImage
import os
from django.http import JsonResponse

# Create your views here.
def home(request):
	return render(request, 'text/home.html')

def send_message(request):
	if request.method == 'POST':
		phone = request.POST.get('phone')
		messgae = request.POST.get('message')
		minute = request.POST.get('minute')
		hour = request.POST.get('hour')

		print(type(minute))
		mins = int(minute)
		print(type(minute))
		hr = int(hour)

		context = {
		'phone': phone,
		'minute': minute,
		'hour': hour
		}
		
		py.sendwhatmsg(phone, messgae, hr, mins)
		return render(request, 'send.html', context)
		print("sent message")

	
		

def hand(request):
	return render(request, 'text/handwriting.html')

def hand_convert(request):
	if request.method == 'POST':
		text = request.POST.get('message')
		print(text)
		py.text_to_handwriting(text, "D:/media")
		return render(request, 'text/handwriting.html')

def email_page(request):
	return render(request, "text/email.html")

def sending_email(request):
	if request.method == 'POST':
		se = SendEmail.objects.all()
		email_list = []
		for email in se:
			email_list.append(email.email)
			print(email.email)

			print(email_list)
		subject = request.POST.get('subject')
		text_content = ""
		print(text_content)
		html_content = request.POST.get('html_content')
		#subject = "hey, how are you!"
		from_email = "tushar24081@gmail.com"
		to = email_list
		#text_content = "Hello, happy friday!"
		#html_content = "<h3>This is shit, asshole!</h3> <img src='{% static 'post.jpg' %}' width='100px' height='100px'>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, to)
		msg.attach_alternative(html_content, "text/html")
		
		print("sending mail...")
		msg.attach_file('img/resume.pdf')
		msg.attach_file('img/post.jpg')
		print("file attched")
		msg.send()
		return render(request, "text/send_email.html")

def subscribe(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		print(email)
		
		if SendEmail.objects.filter(email = email).exists():
			exists = True
		else:
			se = SendEmail.objects.create(email = email)
			se.save()
			exists = False

		print(exists)
		context = {
		'exists': exists
		}
		print("created")
		return render(request, "subscribed.html", context)


