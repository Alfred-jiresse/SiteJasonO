from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .send_mail import send_email

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            message = f"Message de : {email}, \n{form.data['message']}"
            nom = form.data['nom']
            sujet = f"contact depuis le site. Nom: {nom}"
            to_email = "glenkig40@gmail.com"
            send_email(sujet, message, to_email)
            form.save()
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
