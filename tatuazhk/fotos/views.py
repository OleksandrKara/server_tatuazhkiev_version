from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def xhr_test(request):
	name = request.POST.get('name')
	email = request.POST.get('email')
	subject = request.POST.get('subject')
	message = request.POST.get('message')
	phone = request.POST.get('phone')
    
	if not request.POST.get('email'):
		send_mail(
		"Please call me back!",
		"Name: "+ name + "\nPhone: " + phone,
		request.POST.get('olexandr.kara@gmail.com'),
			['kiev.tatuazh@gmail.com'],
		)
	
	if not request.POST.get('phone'):
		send_mail(
			"Please write me back!",
			"Name: "+ name + "\nE-mail: " + email + "\nSubject: " + subject + "\nMessage: " + message,
			request.POST.get('olexandr.kara@gmail.com'),
					['kiev.tatuazh@gmail.com'],
		)
	
	message = True
	return HttpResponse(message)

def kontakti_handler(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if not request.POST.get('phone', ''):
            errors.append('Please enter phone.')
        if not errors:
            send_mail(
                "Please read the letter and call me back!",
                "Name:\t "+ request.POST['subject']+"\nPhone:\t "+request.POST['phone']+"\nMessage: "+request.POST['message'],
                request.POST.get('olexandr.kara@gmail.com'),
                ['kiev.tatuazh@gmail.com'],
            )
            return HttpResponseRedirect('/thanks/')
    return render_to_response('kontakti.html/', {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')