
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

@login_required
def add_show(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()

    emp = Employee.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': form, 'emp': emp})

@login_required
def update_data(request, id):
    emp = Employee.objects.get(pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm(instance=emp)

    return render(request, 'enroll/update.html', {'form': form})

@login_required
def delete_data(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('/')
