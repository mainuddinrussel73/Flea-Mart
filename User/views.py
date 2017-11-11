from django.shortcuts import render,get_object_or_404
from firstapp.forms import UserForm,UserProfileInform

from firstapp.models import UserProfileInfo,User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from User.forms import SellItemInfoForm
from User.models import SellItemInfo,Chat

# Create your views here.

other = None
@login_required
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        global other
        other = request.POST.get('hide', None)
        print('asdfa'+other)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

@login_required
def Messages(request):
    c = Chat.objects.all()
    print(other+'otnerr')
    return render(request, 'firstapp/messages.html', {'chat': c,'other':other })

@login_required
def userhome(request,username='main'):
    u = User.objects.get(username=request.user.username)
    items = SellItemInfo.objects.all()
    args = {'items' : items}
    return render(request,'firstapp/userhome.html',args)

@login_required
def userprofile(request,username='main',pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        username = user.username


    else:
        user = request.user
        username = user.username

    items = SellItemInfo.objects.filter(uploader=user)
    args = {'user': user,'items' : items}
    return render(request, 'firstapp/profile.html', args,)


@login_required
def showitem(request,slug=None):


    instance = get_object_or_404(SellItemInfo,slug=slug);
    # instance = SellItemInfo.objects.get(item_name=item_name)
    c = Chat.objects.all()

    args = {
        "instance" : instance,
        'chat': c
    }
    return render(request, 'firstapp/details.html', args,)

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
