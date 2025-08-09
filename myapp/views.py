from django.shortcuts import render,redirect
from .forms import NoteForm
# Create your views here.

def home(request): 
    return render(request,'home.html')

def add(request):
    if request.method =='POST':
       form = NoteForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('Read.html')
    else: 
      form = NoteForm()
    
    return render(request,'add.html',{'form':form})
    



 
def delete(request):
    return render(request,'delete.html')

def update(request):
    return render(request,'update.html')

def read(request): 
    return render(request,'Read.html')