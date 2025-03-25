from django.urls import path

from App import views, viewAdmin, viewMembers, viewTrainers

urlpatterns =[
    path('',views.home,name='home'),
    path('login',views.Login,name='login'),



    # admin
    path('dashadmin',viewAdmin.dashAdmin,name='dashAdmin'),


    # members
    path('dashmember',viewMembers.dashMember,name='dashMember'),
    path('regiMember',viewMembers.registerMember,name='regiMember'),


    # trainers
    path('dashtrainer',viewTrainers.dashTrainer,name='dashTrainer'),
    path('regiTrainer',viewTrainers.registerTrainer,name='regiTrainer'),


]