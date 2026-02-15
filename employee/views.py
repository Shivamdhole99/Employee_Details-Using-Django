
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import employee
from django.contrib import messages
from .forms import EmployeeForm

@login_required
def add_show(request):
    if request.method == "POST":
        email = request.POST.get('email')

        if employee.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('/')

        employee.objects.create(
            name=request.POST.get('name'),
            email=email,
            department=request.POST.get('department'),
            salary=request.POST.get('salary') or 0
        )

        messages.success(request, "Employee added successfully!")
        return redirect('/')

    employees = employee.objects.all()
    return render(request, "addandshow.html", {"employees": employees})

@login_required
def update_data(request, id):
    emp = employee.objects.get(pk=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm(instance=emp)

    return render(request, 'update.html', {'form': form})

@login_required
def delete_data(request, id):
    emp = employee.objects.get(pk=id)
    emp.delete()
    return redirect('/')
