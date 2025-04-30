from django.urls import path

from App import views, viewAdmin, viewMembers, viewTrainers

urlpatterns =[
    path('',views.home,name='home'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),



    # admin
    path('dashadmin',viewAdmin.dashAdmin,name='dashAdmin'),
    path('allmember',viewAdmin.allmember,name='allmember'),
    path('alltrainer',viewAdmin.alltrainer,name='alltrainer'),
    path('deletemem/<int:id>/',viewAdmin.deletemember,name='deletemem'),
    path('deletetrai/<int:id>/',viewAdmin.deletetrainer,name='deletetrai'),
    path('admincommunity',viewAdmin.adminCommunityView,name='admincommunity'),
    path('chatdeleteA/<int:id>/',viewAdmin.chatDeleteAdmin,name='chatdeleteA'),


    # members
    path('dashmember',viewMembers.dashMember,name='dashMember'),
    path('regiMember',viewMembers.registerMember,name='regiMember'),
    path('ChoiseTrainer',viewMembers.ChoiseTrainer,name='ChoiseTrainer'),
    path('moreinfo/<int:id>/',viewMembers.trainerPage,name='moreinfo'),
    path('select/<int:id>/',viewMembers.selectTrainer,name='select'),
    path('membercommunity',viewMembers.CommunityChatMembers,name='membercommunity'),



    # trainers
    path('dashtrainer',viewTrainers.dashTrainer,name='dashTrainer'),
    path('regiTrainer',viewTrainers.registerTrainer,name='regiTrainer'),
    path('selectrequest',viewTrainers.selectRequest,name='selectrequest'),
    path('accept/<int:id>/',viewTrainers.reqtAccept,name='accept'),
    path('reject/<int:id>/',viewTrainers.reqtReject,name='reject'),
    path('deletereqt/<int:id>/',viewTrainers.deletereqt,name='deletereqt'),
    path('viewmember/<int:id>/',viewTrainers.viewMember,name='viewmember'),
    path('addworkout',viewTrainers.addworkout,name='addworkout'),
    path('updateworkout/<int:id>/',viewTrainers.updateWorkout,name='updateworkout'),
    path('trainercommunity',viewTrainers.CommunityChatTrainer,name='trainercommunity'),




]