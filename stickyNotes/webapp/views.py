from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm, NewNoteForm
from webapp.models import Notes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.template import engines

# Returns the Index and Dashboard page
def index(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewNoteForm(request.POST)
            if form.is_valid():
                Notes.objects.create(user=request.user, note=request.POST['note'])
                engine = engines["jinja2"]
                template = engine.from_string("{% extends 'jinjaHeader.html' %}{% block title %}Note{% endblock %}{% block content %}<div class='container'>" + request.POST['note'] + "</div>{% endblock %}")
                return HttpResponse(template.render({}, request))

        form = NewNoteForm()
        query = list(Notes.objects.filter(user=request.user).values('id', 'note'))
        noteIDs = []
        notes = []
        for x in range(0, len(query)):
            noteIDs.append(query[x]['id'])
            notes.append(query[x]['note'][:100] + '...')
        return render(request, 'index.html', context={'form': form, 'notes': zip(noteIDs, notes)})
    else:
        return render(request, 'index.html')


# Returns specified note
def viewNote(request, noteID):
    query = list(Notes.objects.filter(id=noteID).values('note'))
    if len(query) > 0:
        note = query[0]['note']
        return render(request, 'viewNote.html', context={'note': note})
    else:
        return redirect('Index')


# Handles new user registration.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("Registration successful." )
            return redirect("Index")
        print("Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


# Handles login requests
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(f"You are now logged in as {username}.")
                return redirect("Index")
            else:
                print("Invalid username or password.")
        else:
            print("Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


# Handles logout requests
def logout_request(request):
    logout(request)
    print("You have successfully logged out.") 
    return redirect("Index")