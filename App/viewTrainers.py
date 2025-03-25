from django.shortcuts import render, redirect

from App.forms import LoginUserForm, TrainerForm


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