from django.shortcuts import render
from App.models import Post
from App.forms import PostForm

# Create your views here.

def Home(request):
    form = PostForm()
    context = {
        "Form":form,
    }
    return render(request, 'index.html', context)

