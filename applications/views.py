from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InternshipApplication
from .forms import InternshipApplicationForm

def home(request):
    domains = [
        ("💻", "Software Development"),
        ("🌐", "Web Development"),
        ("📊", "Data Analytics"),
        ("🔒", "Cybersecurity"),
        ("🎨", "Graphic Design"),
        ("📱", "Digital Marketing"),
        ("🤖", "Artificial Intelligence"),
        ("🔌", "Networking"),
    ]
    return render(request, 'applications/home.html', {'domains': domains})

def about(request):
    benefits = [
        ("🎯", "Real Projects", "Work on actual company projects with measurable impact"),
        ("👨‍🏫", "Expert Mentorship", "Get guided by industry professionals"),
        ("📜", "Official Certificate", "Receive a recognized completion certificate"),
        ("🤝", "Networking", "Connect with professionals across the tech industry"),
        ("💻", "Modern Tools", "Access industry-standard software and technologies"),
        ("📈", "Career Growth", "Build a strong portfolio that employers want to see"),
    ]
    eligibility = [
        "Currently enrolled in a university or college",
        "HND, Bachelor, Master, or PhD level",
        "Any field of study",
        "Must have school recommendation letter",
        "Passion for learning and innovation",
    ]
    return render(request, 'applications/about.html', {'benefits': benefits, 'eligibility': eligibility})

@login_required
def apply(request):
    existing = InternshipApplication.objects.filter(applicant=request.user).first()
    if existing:
        messages.info(request, 'You already have an application submitted.')
        return redirect('application_status')
    form = InternshipApplicationForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        app = form.save(commit=False)
        app.applicant = request.user
        app.save()
        messages.success(request, 'Application submitted successfully!')
        return redirect('application_status')
    return render(request, 'applications/apply.html', {'form': form})

@login_required
def applicant_dashboard(request):
    application = InternshipApplication.objects.filter(applicant=request.user).first()
    return render(request, 'applications/applicant_dashboard.html', {'application': application})

@login_required
def application_status(request):
    application = InternshipApplication.objects.filter(applicant=request.user).first()
    if application:
        submitted = ('done', 'Submitted')
        reviewing = ('done' if application.status != 'Pending' else 'active', 'Under Review')
        if application.status == 'Approved':
            decision = ('done', 'Approved')
        elif application.status == 'Rejected':
            decision = ('active', 'Rejected')
        else:
            decision = ('pending', 'Decision')
        steps = [submitted, reviewing, decision]
    else:
        steps = []
    return render(request, 'applications/status.html', {'application': application, 'steps': steps})