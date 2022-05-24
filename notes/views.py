from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView

from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name: str = 'notes/notes_list.html'  # Can include it or not if the standard naming is followed


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name: str = 'notes/notes_detail.html'
    #  # No template name . . .. standard naming saved us


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})


