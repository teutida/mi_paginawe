from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post_articulo
# para chequiar
#from django.http import HttpResponse

# Create your views here.

# def index(request):
# return render(request, 'index.html')


class postdetalle(DetailView):
    model = Post_articulo
    template_name = 'mamon.html'
    context_object_name = 'info'


class index(ListView):
    context_object_name = 'blog'
    model = Post_articulo
    template_name = 'blog.html'
