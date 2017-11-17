from django.shortcuts import render,get_object_or_404
from firstapp.forms import UserForm,UserProfileInform
import json
from firstapp.models import UserProfileInfo,User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from User.forms import SellItemInfoForm
from User.models import SellItemInfo,Chat,Notification
from django.core import serializers
from django.forms.models import model_to_dict
from itertools import chain,cycle
from itertools import izip_longest
import re
from collections import Counter
import string


# from django.core import serializers
# json_serializer = serializers.get_serializer("json")()
# companies = json_serializer.serialize(Notification.objects.all().order_by('id')[:5], ensure_ascii=False)

# Create your views here.

other = None






@login_required
def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)

        global other
        other = request.POST.get('hide', None)
        itemname = request.POST.get('itemname', None)
        # print('asdfa'+itemname)
        c = Chat(user=request.user, message=msg)
        counter = SellItemInfo.objects.get(item_name=itemname)
        n = Notification(user=request.user,to=request.user.username,fromm=other,count=counter.get_slug(),description=msg)
        if msg != '':
            c.save()
            n.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')

@login_required
def Messages(request):
    c = Chat.objects.all()
    # print('otnerr')
    # print(c.user.username)
    return render(request, 'firstapp/messages.html', {'chat': c,'other':other })




@login_required
def Notificationsupdate(request):
    m = []
    text = 'asfa'
    print(text+'asasdf')
    if request.method == "POST":
        text = request.POST['text']
        city = request.POST['city']
        m.append("asdfasdf")
    return JsonResponse(json.dumps(m))

@login_required
def Notifications(request,username='main'):
    # counter = Notification.objects.all()
    #
    # # print(c.description)
    # return render(request, 'firstapp/notification.html', {'counter': counter})
    if request.is_ajax():
        counter = Notification.objects.exclude(to=request.user)
        hhh = list(counter.values('to','description','count','id'))
        bonus = UserProfileInfo.objects.exclude(user=request.user)
        ggg = list(bonus.values('user','profilepic','user_id'))
        items = SellItemInfo.objects.filter(uploader=request.user)
        it = list(items.values('slug','uploader'))
        lll = []
        u = 0
        result = list(counter.values('user','to','description','count','fromm'))


        for f, b in zip(ggg,result):
            for o in it:

                if(b.get('count')==o.get('slug') ):
                    nnn = {
                        'id' : f.get('user'),
                        'profilepic' : f.get('profilepic'),
                        'to' : b.get('to'),
                        'description' : b.get('description'),
                        'count' : b.get('count'),
                        'fromm' : b.get('fromm')
                    }
                    lll.insert(u,nnn)
                    u+=1

        # print(json.dumps(lll))

        return HttpResponse(json.dumps(lll))
def compare(s1, s2):
    remove = string.punctuation + string.whitespace
    return s1.translate(None, remove) == s2.translate(None, remove)
def combine(list1, list2):
    list1 = iter(list1)
    for item2 in list2:
        if item2 == list2[0]:
            item1 = next(list1)
        yield ''.join(map(str, (item1, item2)))

@login_required
def userhome(request,username='main'):
    u = User.objects.get(username=request.user.username)
    counter = Notification.objects.exclude(user=request.user)
    bonus = UserProfileInfo.objects.exclude(user=request.user)
    hhh = list(counter.values('to','description','count','fromm'))
    bbb = list(bonus.values('profilepic'))
    fin = zip(hhh,bbb)
    # print(hhh)
    items = SellItemInfo.objects.all()
    args = {'items' : items,'counter' : fin }
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
def showitem(request,slug=None,id=None):


    instance = get_object_or_404(SellItemInfo,slug=slug);
    # instance = SellItemInfo.objects.get(item_name=item_name)
    c = Chat.objects.all()
    # u = request.get('id')
    # ins = Notification.objects.get(count=slug)
    # print(ins)
    # for r in instance:
        # r.delete()
    print(request.user)
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
