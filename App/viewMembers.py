from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from App.filter import TrainerNameFilter
from App.forms import LoginUserForm, MemberForm, CommunityForm
from App.models import Trainer, Member, selectStatus, Community

@login_required(login_url='home')
def dashMember(request):
    return render(request, 'Members/dashMembers.html')




def registerMember(request):
    form1 = LoginUserForm()
    form2 = MemberForm()
    if request.method == 'POST':
        form1 = LoginUserForm(request.POST)
        form2 = MemberForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            data = form1.save(commit=False)
            data.is_member = True
            data.save()
            obj = form2.save(commit=False)
            obj.user = data
            obj.save()
            return redirect('/')
    return render(request, 'registerMember.html', {'form1': form1, 'form2': form2})




@login_required(login_url='home')
def ChoiseTrainer(request):
    trainer_data = Trainer.objects.all()
    search_data = TrainerNameFilter(request.GET, queryset=trainer_data)
    trainer_data = search_data.qs
    return render(request, 'Members/ChoiceTrainer.html', {'data': trainer_data,'search_data':search_data})



@login_required(login_url='home')
def trainerPage(request, id):
    trainer_data = Trainer.objects.get(id=id)
    mem_data = Member.objects.get(user=request.user)
    status = selectStatus.objects.filter(trainer=id,member=mem_data)
    return render(request, 'Members/TrainerPage.html',
                  {'data': trainer_data,'status':status})



@login_required(login_url='home')
def selectTrainer(request, id):
    user_data = request.user
    mem_data = Member.objects.get(user=user_data)
    trainer_data = Trainer.objects.get(id=id)
    status = selectStatus()
    status.trainer = trainer_data
    status.member = mem_data
    status.save()
    return redirect('moreinfo',id=id)




@login_required(login_url='home')
def CommunityChatMembers(request):
    form = CommunityForm()
    mem_data = Member.objects.get(user=request.user)
    chat_data = Community.objects.all()
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.member = mem_data
            obj.save()
            return redirect('membercommunity')
        else:
            print(form.errors)
    return render(request, 'Members/communityPageMember.html', {'form': form, 'chat_data': chat_data})

