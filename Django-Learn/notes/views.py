from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Note
from django.views.generic import TemplateView, ListView, DetailView, CreateView,UpdateView
from django.shortcuts import redirect
from .forms import NotesForm
from django.views.generic.edit import DeleteView


class NotesDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = '/smart/notes'


class NoteListView(ListView):
    model = Note
    context_object_name = "notes"  # This is used in templates in for loop
    template_name = "notes/notes_list.html"


# def list_all_entries(request):
#     all_notes = Note.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = "notes/notes_details.html"


# def details(request, pk):
#     try:
#         note = Note.objects.get(pk=pk)
#         return render(request, 'notes/notes_details.html', {'note': note})
#     except Note.DoesNotExist as e:
#         return render(request, 'notes/NoteNotFound.html', {})


class NotFoundView(TemplateView):
    template_name = 'NoteNotFound.html'
