from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseForbidden
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Comment, Snippet
from MainApp.forms import CommentForm, SnippetForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


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
           context = {
               'pagename': 'Главная',
               'errors': ['Неверный логин или пароль']
           }
           return render(request, 'pages/index.html', context)
   return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        context = {
            'pagename': 'Регистрация нового пользователя',
            'form': form
        }
        return render(request, 'pages/register.html', context)
    else:  # POST
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            'pagename': 'Регистрация нового пользователя',
            'form': form
        }
        return render(request, 'pages/register.html', context)


@login_required
def comment_add(request):
    try:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            snippet_id = request.POST.get('snippet_id', 0)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.snippet = Snippet.objects.get(id=snippet_id)
                comment.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except ObjectDoesNotExist:
        raise Http404
    
    
@login_required
def comment_edit(request, id):
    try:
        comment = Comment.objects.get(id=id)
        data = request.POST
        comment.text = data["text"]
        if comment.author == request.user:
            comment.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponseForbidden()
    except ObjectDoesNotExist:
        return Http404
    
@login_required
def comment_delete(request, id):
    try:
        comment = Comment.objects.get(id=id)
        if request.user.id == 1:
            comment.delete()
        else:
            return HttpResponseForbidden()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except ObjectDoesNotExist:
        raise Http404
    

@login_required
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


@login_required
def delete_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        if snippet.user == request.user:
            snippet.delete()
        else:
            return HttpResponseForbidden()

        return redirect("list_snippet")
    except ObjectDoesNotExist:
        raise Http404


@login_required
def edit_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        comments = Comment.objects.filter(snippet=id)
        if request.method == "POST":
            data = request.POST
            snippet.id = id
            snippet.name = data["name"]
            snippet.lang = data["lang"]
            snippet.code = data["code"]
            snippet.public = request.POST.get('public', False)
            if snippet.user == request.user:
                snippet.save()
            else:
                return HttpResponseForbidden()
            
            try:
                if snippet.user.id == request.user.id:
                    return redirect("my_list_snippet")
            except:
                return redirect("list_snippet")

        context = {
            'pagename': 'Редактирование сниппета',
            'snippet': snippet,
            'comments': comments,
            'edit_mode': True,
            'comment_form': CommentForm()
        }
        return render(request, 'pages/snippet.html', context)
    except ObjectDoesNotExist:
        return Http404


def get_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        comments = Comment.objects.filter(snippet=id)
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet,
            'comments': comments,
        }
        return render(request, 'pages/snippet.html', context)
    except ObjectDoesNotExist:
        raise Http404
    
    
def snippets_page(request):
    snippets = Snippet.objects.filter(public=1)
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets,
        'snippets_count': snippets.count()
    }
    return render(request, 'pages/view_snippets.html', context)


def my_snippets_page(request):
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(user_id=request.user.id)
        context = {
            'pagename': 'Просмотр моих сниппетов',
            "snippets": snippets,
            'snippets_count': snippets.count()
        }
        return render(request, 'pages/view_snippets.html', context)
    raise Http404
