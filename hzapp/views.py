from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# from django.core.paginator import Paginator, EmptyPage,InvalidPage,PageNotAnInteger
# from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse



def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('homepage'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request,'login1.html',content)

@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

def MainPage(request):
    return HttpResponseRedirect(reverse('homepage'))


@login_required()
def index(request):

    user = request.user if request.user.is_authenticated() else None
    
    return render(request, 'index.html')
