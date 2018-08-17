from django.shortcuts import render,redirect
from django.contrib import messages
from contact.forms import ContactForm
from django.core.mail import send_mail


def success(request):
    return render(request,'contact/success.html')

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            message = contact_form.cleaned_data['message']
            sender = contact_form.cleaned_data['sender']


            recipients = ['emailforportfolio00@gmail.com']

            send_mail(name, message, sender, recipients)
            contact_form.save()

            messages.success(request, 'Message sent successfully')
            return redirect('contact:success')
        else:
            messages.error(request, 'Error sending your Message')

    else:
        contact_form = ContactForm()

    context = {
        "contact_form": contact_form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)
