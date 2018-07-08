from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.context_processors import csrf

from .models import Book
from .forms import BookForm
 
def index(request):
    books = Book.objects.all()
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
#             instance = form.save(commit=False)
#             instance.title = instance.qtt * instance.rate
#             instance.date = timezone.now()
#             instance.save()  
            return HttpResponseRedirect(reverse('engineering:index'))
    else:
        form = BookForm()
        
    return render(request, 'engineering/index.html', {'form': form })
