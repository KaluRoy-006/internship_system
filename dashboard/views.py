from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from applications.models import InternshipApplication

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin, login_url='/accounts/login/')
def admin_dashboard(request):
    apps = InternshipApplication.objects.all()
    context = {
        'total': apps.count(),
        'pending': apps.filter(status='Pending').count(),
        'approved': apps.filter(status='Approved').count(),
        'rejected': apps.filter(status='Rejected').count(),
        'recent': apps[:5],
    }
    return render(request, 'dashboard/dashboard.html', context)

@user_passes_test(is_admin, login_url='/accounts/login/')
def all_applications(request):
    apps = InternshipApplication.objects.all()
    search = request.GET.get('search', '')
    domain = request.GET.get('domain', '')
    status = request.GET.get('status', '')
    if search:
        apps = apps.filter(Q(full_name__icontains=search) | Q(applicant__email__icontains=search))
    if domain:
        apps = apps.filter(internship_domain=domain)
    if status:
        apps = apps.filter(status=status)
    domains = InternshipApplication.DOMAIN_CHOICES
    return render(request, 'dashboard/all_applications.html', {
        'applications': apps, 'domains': domains,
        'search': search, 'selected_domain': domain, 'selected_status': status,
    })

@user_passes_test(is_admin, login_url='/accounts/login/')
def application_detail(request, pk):
    app = get_object_or_404(InternshipApplication, pk=pk)
    return render(request, 'dashboard/application_detail.html', {'application': app})

@user_passes_test(is_admin, login_url='/accounts/login/')
def approve_application(request, pk):
    app = get_object_or_404(InternshipApplication, pk=pk)
    app.status = 'Approved'
    app.save()
    messages.success(request, f'Application for {app.full_name} approved.')
    return redirect('application_detail', pk=pk)

@user_passes_test(is_admin, login_url='/accounts/login/')
def reject_application(request, pk):
    app = get_object_or_404(InternshipApplication, pk=pk)
    app.status = 'Rejected'
    app.save()
    messages.warning(request, f'Application for {app.full_name} rejected.')
    return redirect('application_detail', pk=pk)

@user_passes_test(is_admin, login_url='/accounts/login/')
def delete_application(request, pk):
    app = get_object_or_404(InternshipApplication, pk=pk)
    if request.method == 'POST':
        app.delete()
        messages.success(request, 'Application deleted.')
        return redirect('all_applications')
    return render(request, 'dashboard/confirm_delete.html', {'application': app})

@user_passes_test(is_admin, login_url='/accounts/login/')
def approved_applications(request):
    apps = InternshipApplication.objects.filter(status='Approved')
    return render(request, 'dashboard/filtered_applications.html', {
        'applications': apps, 'filter_title': 'Approved Applications'
    })

@user_passes_test(is_admin, login_url='/accounts/login/')
def rejected_applications(request):
    apps = InternshipApplication.objects.filter(status='Rejected')
    return render(request, 'dashboard/filtered_applications.html', {
        'applications': apps, 'filter_title': 'Rejected Applications'
    })
