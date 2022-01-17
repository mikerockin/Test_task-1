from django.shortcuts import render, get_object_or_404, redirect
from .models import Employe, Subdivision, Position, Department
from .forms import SubvisionForm, EmployeForm
from django.contrib.auth.decorators import login_required
from datetime import date


@login_required
def index(request):
    num_employees = Employe.objects.all().count()
    num_departments = Department.objects.all().count()
    num_subdivisions = Subdivision.objects.all().count()
    num_positions = Position.objects.all().count()
    return render(request, 'index.html', context={
                                         'num_employees': num_employees,
                                         'num_departments': num_departments,
                                         'num_subdivisions': num_subdivisions,
                                         'num_positions': num_positions},
                  )
@login_required
def employees_list(request):
    employees = Employe.objects.order_by('first_name')
    return render(request, 'employees_list.html',
                  context={'employees': employees})
@login_required
def employe_detail(request, id):
    employe = get_object_or_404(Employe, id=id)
    date_of_employment = Employe.objects.get(id=id)
    current_date_of_employment = date.fromisoformat(str(date_of_employment))
    date_now = date.today()
    delta = date_now - current_date_of_employment
    current_delta = round(delta.days/365)
    return render(request, 'employe_detail.html',
                  context={'employe': employe,'current_delta': current_delta},)
@login_required
def positions_list(request):
    positions = Position.objects.order_by('name')
    return render(request, 'positions_list.html',
                  context={'positions': positions})
@login_required
def departments_list(request):
    departments = Department.objects.order_by('name')
    return render(request, 'departments_list.html',
                  context={'departments': departments})
@login_required
def subdivisions_list(request):
    subdivisions = Subdivision.objects.order_by('name')
    return render(request, 'subdivisions_list.html',
                  context={'subdivisions': subdivisions})

@login_required
def subdivisions_new(request):
    if request.method == 'POST':
        form = SubvisionForm(request.POST)
        if form.is_valid():
            subdivision = form.save(commit=False)
            subdivision.save()
            return redirect('/subdivisions/', id=subdivision.id)
    else:
        form = SubvisionForm()
    return render(request, 'subdivisions_add.html', {'form': form})

@login_required
def subdivisions_delete(request, id):
    subdivision = Subdivision.objects.get(id=id)
    subdivision.delete()
    return redirect('/subdivisions/')


@login_required
def employees_delete(request, id):
    employe = Employe.objects.get(id=id)
    employe.delete()
    return redirect('/employees/')


@login_required
def employees_new(request):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            employe = form.save(commit=False)
            employe.save()
            return redirect('/employees/', id=employe.id)
    else:
        form = EmployeForm()
    return render(request, 'employees_add.html', {'form': form})

@login_required
def employe_edit(request, id):
    employe = get_object_or_404(Employe, id=id)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            employe = form.save(commit=False)
            employe.save()
            return redirect('/employees/', id=employe.id)
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'employe_edit.html', {'form': form})

