from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Creating View
class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# Listing View
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name: str = 'notes/notes_list.html'  # Can include it or not if the standard naming is followed
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

# Updating View
class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name: str = 'notes/notes_delete.html'




class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name: str = 'notes/notes_detail.html'
    #  # No template name . . .. standard naming saved us
    
def Cofused(request):
    all_notes = Notes.objects.all()
    
    context = {
        'all_notes': all_notes
    }
    return render(request, 'confused.html', context=context)
