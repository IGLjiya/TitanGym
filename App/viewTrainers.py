from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from App.forms import LoginUserForm, TrainerForm, WorkOutPlanForm, CommunityForm
from App.models import selectStatus, Trainer, Member, WorkOutPlan, Community

@login_required(login_url='home')
def dashTrainer(request):
    return render(request,'Trainers/dashTrainers.html')



def registerTrainer(request):
    form1 = LoginUserForm()
    form2 = TrainerForm()
    if request.method == 'POST':
        form1 = LoginUserForm(request.POST)
        form2 = TrainerForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_trainer = True
            data.save()
            obj =  form2.save(commit=False)
            obj.user = data
            obj.save()
            return redirect('/')
    return render(request,'registerTrainer.html',
                  {'form1':form1,'form2':form2})



@login_required(login_url='home')
def selectRequest(request):
    trainer_data = Trainer.objects.get(user=request.user)
    rqst_data = selectStatus.objects.filter(trainer=trainer_data)
    return render(request,'Trainers/selectRequest.html',{'data':rqst_data})




@login_required(login_url='home')
def reqtAccept(request,id):
    status_data = selectStatus.objects.get(id=id)
    status_data.status = 1
    status_data.save()
    return redirect('selectrequest')




@login_required(login_url='home')
def reqtReject(request,id):
    statud_data = selectStatus.objects.get(id=id)
    statud_data.status = 2
    statud_data.save()
    return redirect('selectrequest')





@login_required(login_url='home')
def deletereqt(request,id):
    data = selectStatus.objects.get(id=id)
    data.delete()
    return redirect('selectrequest')



@login_required(login_url='home')
def viewMember(request,id):
    mem_data = Member.objects.get(id=id)
    trainer_data = Trainer.objects.get(user=request.user)
    work_data = WorkOutPlan.objects.filter(member=mem_data,user=trainer_data)
    return render(request,'Trainers/memberPage.html',
                  {'data':mem_data,'work_data':work_data})




@login_required(login_url='home')
def addworkout(request):
    trainer_data = Trainer.objects.get(user=request.user)
    select_data = selectStatus.objects.get(trainer=trainer_data)
    form = WorkOutPlanForm()
    if request.method == 'POST':
        form = WorkOutPlanForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = trainer_data
            obj.member = select_data.member
            obj.save()
            return redirect('viewmember',id=select_data.member.id)
    return render(request,'Trainers/addWorkoutplan.html',{'form':form})




@login_required(login_url='home')
def updateWorkout(request,id):
    workout_data = WorkOutPlan.objects.get(id=id)
    form = WorkOutPlanForm(instance=workout_data)
    if request.method == 'POST':
        form = WorkOutPlanForm(request.POST,instance=workout_data)
        if form.is_valid():
            form.save()
            return redirect('viewmember',id=workout_data.member.id)
    return render(request,'Trainers/updateWorkoutplan.html',{'form':form})





@login_required(login_url='home')
def CommunityChatTrainer(request):
    form = CommunityForm()
    trainer_data = Trainer.objects.get(user=request.user)
    chat_data = Community.objects.all()
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.trainer = trainer_data
            obj.save()
            return redirect('trainercommunity')
        else:
            print(form.errors)
    return render(request, 'Trainers/communityPageTrainer.html', {'form': form, 'chat_data': chat_data})
