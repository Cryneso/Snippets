from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


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
            form.save()
            return redirect("list_snippet")
        return render(request, 'add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets
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
