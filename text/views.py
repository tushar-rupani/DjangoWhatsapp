from django.shortcuts import render, redirect
import pywhatkit as py

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

def hand(request):
	return render(request, 'text/handwriting.html')

def hand_convert(request):
	if request.method == 'POST':
		text = request.POST.get('message')
		print(text)
		py.text_to_handwriting(text, "D:/media")
		return render(request, 'text/handwriting.html')


