from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Subject, FlashCard
from .forms import SubjectForm, FlashCardForm
from django.http import JsonResponse

# Home page view
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'home.html')

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Dashboard view (show subjects of logged-in user)
@login_required
def dashboard(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'subjects': subjects})

# Add subject view
@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('dashboard')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})

# Edit subject view
@login_required
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, user=request.user)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form})

# Delete subject view
@login_required
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, user=request.user)
    if request.method == 'POST':
        subject.delete()
        return redirect('dashboard')
    return render(request, 'delete_subject.html', {'subject': subject})

# Subject details view
@login_required
def subject_details(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, user=request.user)
    flashcards = FlashCard.objects.filter(subject=subject)
    return render(request, 'subject_details.html', {'subject': subject, 'flashcards': flashcards})

# Add flashcard view
@login_required
def add_flashcard(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id, user=request.user)
    if request.method == 'POST':
        form = FlashCardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.subject = subject
            flashcard.save()
            return redirect('subject_details', subject_id=subject_id)
    else:
        form = FlashCardForm()
    return render(request, 'add_flashcard.html', {'form': form, 'subject': subject})

# Edit flashcard view
@login_required
def edit_flashcard(request, flashcard_id):
    flashcard = get_object_or_404(FlashCard, id=flashcard_id, subject__user=request.user)
    if request.method == 'POST':
        form = FlashCardForm(request.POST, instance=flashcard)
        if form.is_valid():
            form.save()
            return redirect('subject_details', subject_id=flashcard.subject.id)
    else:
        form = FlashCardForm(instance=flashcard)
    return render(request, 'edit_flashcard.html', {'form': form})

# Delete flashcard view
@login_required
def delete_flashcard(request, flashcard_id):
    flashcard = get_object_or_404(FlashCard, id=flashcard_id, subject__user=request.user)
    if request.method == 'POST':
        flashcard.delete()
        return redirect('subject_details', subject_id=flashcard.subject.id)
    return render(request, 'delete_flashcard.html', {'flashcard': flashcard})

# View for fetching flashcard details for modal
@login_required
def flashcard_detail(request, flashcard_id):
    flashcard = get_object_or_404(FlashCard, id=flashcard_id, subject__user=request.user)
    return JsonResponse({
        'question': flashcard.question,
        'answer': flashcard.answer
    })
