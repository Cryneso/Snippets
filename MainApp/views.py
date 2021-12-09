from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def login_page(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       # print("username =", username)
       # print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           pass
   return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')



def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("list_snippet")
        return render(request, 'add_snippet.html', {'form': form})


def delete_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        snippet.delete()

        return redirect("list_snippet")
    except ObjectDoesNotExist:
        raise Http404


def edit_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        if request.method == "POST":
            data = request.POST
            snippet.name = data["name"]
            snippet.lang = data["lang"]
            snippet.code = data["code"]
            snippet.save()
            return redirect("list_snippet")

        context = {
            'pagename': 'Редактирование сниппета',
            'snippet': snippet,
            'edit_mode': True
        }
        return render(request, 'pages/snippet.html', context)
    except ObjectDoesNotExist:
        raise Http404


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets,
        'snippets_count': snippets.count()
    }
    return render(request, 'pages/view_snippets.html', context)


def get_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet
        }
        return render(request, 'pages/snippet.html', context)
    except ObjectDoesNotExist:
        raise Http404
