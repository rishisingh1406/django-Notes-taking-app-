from django.shortcuts import render,redirect ,get_object_or_404
from .forms import NoteForm
from .models import Notes
from django.contrib import messages


# Create your views here.

def home(request): 
    return render(request,'home.html')

def add(request):
    if request.method =='POST':
       form = NoteForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect('read')
    else: 
      form = NoteForm()
    
    return render(request,'add.html',{'form':form})
    



def delete(request):
    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        try:
            note = Notes.objects.get(ID=note_id)  # Use "ID" since your model uses capitalized field
            note.delete()
            messages.success(request, f"Note with ID {note_id} deleted successfully.")
        except Notes.DoesNotExist:
            messages.error(request, f"No note found with ID {note_id}.")
        
        return redirect('delete')  # reload delete page

    return render(request, 'delete.html')



def update(request):
    message = ""
    if request.method == 'POST':
        note_id = request.POST.get('id')
        new_message = request.POST.get('message')

        if note_id and new_message:
            note = get_object_or_404(Notes, ID=note_id)
            note.message = new_message
            note.save()
            message = "Note updated successfully!"
        else:
            message = "Please provide both ID and Message."

    return render(request, 'update.html', {'message': message})



def read(request): 
    notes = Notes.objects.all().order_by('-ID')
    return render(request, 'Read.html', {'notes': notes})