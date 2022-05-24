from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import Notes
from .forms import NotesForm

# Creating View
class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

# Listing View
class NotesListView(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name: str = 'notes/notes_list.html'  # Can include it or not if the standard naming is followed

# Updating View
class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name: str = 'notes/notes_detail.html'
    #  # No template name . . .. standard naming saved us