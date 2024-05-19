from django.shortcuts import render
from .forms import EmailSubscriptionForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/hpage.html', {'form': form, 'success': True})
    else:
        form = EmailSubscriptionForm()
    return render(request, 'home/hpage.html',{'form': form})


def privacy_policy(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/about.html', {'form': form, 'success': True})
    else:
        form = EmailSubscriptionForm()
    return render(request, 'home/privactplicy.html',{'form': form})

def term_of_service(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/tanc.html', {'form': form, 'success': True})
    else:
        form = EmailSubscriptionForm()
    return render(request, 'home/tanc.html',{'form': form})

def about(request):
    if request.method == 'POST':
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/about.html', {'form': form, 'success': True})
    else:
        form = EmailSubscriptionForm()
    return render(request, 'home/about.html',{'form': form})


