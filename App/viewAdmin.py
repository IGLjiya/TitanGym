from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App.models import Member, Trainer, Community


@login_required(login_url='home')
def dashAdmin(request):
    return render(request,'Admin/dashAdmin.html')



@login_required(login_url='home')
def allmember(request):
    mem_data = Member.objects.all()
    return render(request,'Admin/allMember.html',{'mem_data':mem_data})



@login_required(login_url='home')
def deletemember(request,id):
    data = Member.objects.get(id=id)
    data.delete()
    return redirect('allmember')



@login_required(login_url='home')
def alltrainer(request):
    trainer_data = Trainer.objects.all()
    return render(request,'Admin/allTrainer.html',{'trainer_data':trainer_data})



@login_required(login_url='home')
def deletetrainer(request,id):
    data = Trainer.objects.get(id=id)
    data.delete()
    return redirect('alltrainer')



@login_required(login_url='home')
def adminCommunityView(request):
    chat_data = Community.objects.all()
    return render(request,'Admin/communityPageAdmin.html',{'chat_data':chat_data})

