from django.shortcuts import render


def dashAdmin(request):
    return render(request,'Admin/dashAdmin.html')