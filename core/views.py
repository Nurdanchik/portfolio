from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, Post
from .forms import ContactMessageForm, PostForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactMessageForm()

    return render(request, 'index.html', {'form': form})

@login_required
def inbox(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'inbox.html', {'messages': messages})

def home(request):
    return render(request, 'index.html')


# below must be Daniel's changes

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'index.html', {'form': form})

# daniel's part also