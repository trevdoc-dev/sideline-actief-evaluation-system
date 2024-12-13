from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userauth.models import User
from userauth.models import Question
from userauth.forms import QuestionForm


# MAIN PAGE
def main_page(request):
    return render(request, "main_page.html")

    
# USERS PAGE
def user_page(request):
    users = User.objects.all()
    return render(request, "user_page.html", {"users": users})
    
# EVALUATION PAGE
def evaluation_page(request):
    evaluation = Question.objects.all()
    return render(request, "evaluation_page.html", {"evaluation": evaluation})



# LOGIN PAGE
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("question_list")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login_page.html")


# EDIT PROFILE
@login_required
def edit_page(request, pk):
    user = get_object_or_404(User, pk=pk)  # Fetch user by ID

    if request.method == "POST":
        # Update user details from POST data
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)
        user.save()
        return render(request, "edit_page.html", {"user": user, "success": True})

    return render(request, "edit_page.html", {"user": user})









# -------------------------- 
#           CRUD PAGE 
# --------------------------


# CREATE
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("question_list")
    else:
        form = QuestionForm()
    return render(request, "questions/create_question.html", {"form": form})

# RETRIEVE
def question_list(request):
    questions = Question.objects.all()
    return render(request, "questions/question_list.html", {"questions": questions})

# UPDATE
def update_question(request, pk):
    post = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("question_list")
    else:
        form = QuestionForm(instance=post)
    return render(request, "questions/update_question.html", {"form": form, "post": post})

# DELETE
def delete_question(request, pk):
    post = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("question_list")
    return render(request, "questions/delete_question.html", {"post": post})
