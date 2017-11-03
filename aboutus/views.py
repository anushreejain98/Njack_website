

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Fill

class IndexView(generic.ListView):
    template_name = 'aboutus/aindex.html'
    context_object_name = 'all_details'

    def get_queryset(self):
        return Fill.objects.all()

class DetailView(generic.DetailView):
    model = Fill
    template_name = 'aboutus/detail.html'

class FillCreate(CreateView):
    model = Fill
    fields = ['name','email','message']