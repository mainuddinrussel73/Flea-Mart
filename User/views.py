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
        # print('asdfa'+other)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
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
def Notifications(request,username='main'):
    # counter = Notification.objects.all()
    #
    # # print(c.description)
    # return render(request, 'firstapp/notification.html', {'counter': counter})
    if request.is_ajax():
        # username = request.GET.get('user', '')
        u = User.objects.get(username=request.user.username)
        counter = Notification.objects.all()
        # data = serializers.serialize('json', counter)
        result_list = list(counter.values('count', 'to','description'))
        return HttpResponse(json.dumps(result_list))
        # do whatever processing you need
        # user.some_property = whatever
        # print(counter.to)
        # send back whatever properties you have updated


        # return HttpResponse(json.dumps(json_response),
        #     content_type='application/json')

        # return render(request, 'firstapp/notification.html',  {"obj_as_json": simplejson.dumps(data)})


@login_required
def userhome(request,username='main'):
    u = User.objects.get(username=request.user.username)
    counter = Notification.objects.all()
    # print(c.description)
    items = SellItemInfo.objects.all()
    args = {'items' : items,'counter':counter }
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
