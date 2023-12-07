from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactMessage
from .forms import ContactMessageForm

@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()

    return render(request, 'index.html', {'form': form})

def inbox(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'inbox.html', {'messages': messages})

def home(request):
    return render(request, 'index.html')
