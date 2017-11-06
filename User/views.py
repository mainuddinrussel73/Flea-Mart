from django.shortcuts import render,get_object_or_404
from firstapp.forms import UserForm,UserProfileInform

from firstapp.models import UserProfileInfo,User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from User.forms import SellItemInfoForm
from User.models import SellItemInfo

# Create your views here.

@login_required
def userhome(request,username='main'):
    u = User.objects.get(username=request.user.username)

    return render(request,'firstapp/userhome.html',{})

@login_required
def userprofile(request,username='main',pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        username = user.username


    else:
        user = request.user
        username = user.username

    items = SellItemInfo.objects.filter(uploader=user)
    print(items)
    args = {'user': user,'items' : items}
    return render(request, 'firstapp/profile.html', args,)

@login_required
def sellitem(request):

    isposted = False

    if request.method == "POST":
        # userform = UserForm(data=request.POST)
        selliteminfo = SellItemInfoForm(data=request.POST)

        if selliteminfo.is_valid():
            # user = userform.save()
            # user.set_password(user.password)
            # user.save()

            item = selliteminfo.save(commit=False)
            item.uploader = request.user
            item.save()
            # profile.user = user

            if 'item_pic' in request.FILES:
                item.item_pic = request.FILES['item_pic']

            item.save()
            isposted = True

        else :
            print('Not possible')
    else:
        # userform = UserForm()
        selliteminfo = SellItemInfoForm()  #sett item forms

    return render(request,'firstapp/sellitem.html',
    {

        'selliteminfo':selliteminfo,
        'isposted':isposted
    })
