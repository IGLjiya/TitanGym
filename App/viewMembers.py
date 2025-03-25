from django.shortcuts import redirect, render

from App.forms import LoginUserForm, MemberForm


def dashMember(request):
    return render(request,'Members/dashMembers.html')

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
    return render(request,'registerMember.html',{'form1':form1,'form2':form2})