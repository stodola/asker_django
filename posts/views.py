from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Pytania
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from .forms import UserForm, PytaniaForm
from django.core.urlresolvers import reverse


def home_page(request):
    return render(request, 'base.html')

def logout1(request):
    user = request.user.username
    logout(request)
    context = {'user':user}
    return render (request, 'logout.html', context)

def register_sussess(request):
    return render (request, 'successful_registration.html')

def login1(request):
    form = UserForm ()
    context = {'form':form}
    
    if request.method == 'POST':
        form = UserForm(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cards')
        else:
            context['flag'] = True
    
    return render(request, 'login.html', context)


def register1(request):
    if request.method == 'POST':
        form = UserForm (request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username=username, password=password)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect('/regsuccess/')
    form = UserForm ()
    context =  {'form': form}
    return render(request, 'register.html', context)

@login_required
def user_loged(request):
    user=request.user.username
    quaryset = Pytania.objects.filter(user=user).values('carddeck').distinct()
    context = {'pytania':quaryset,}
    return render (request, 'user_loged.html', context)

@login_required
def test_catch(request, username,cardname, order, odp):
    pytanie =  Pytania.objects.filter(user=username, carddeck=cardname).values('pytanie')

    if odp == 'qq':
        order = int(order)
        try :
            do_zapytania = pytanie[order]
        except IndexError:
            return render (request, 'no_more_questions.html')  
        order +=1
        context = {'pytanie':do_zapytania, 'id':order, 'nazwa_pliku':cardname}
    
    if odp == 'ans':
        odpowiedz =  Pytania.objects.filter(user=username, carddeck=cardname).values('odpowiedz')
        order = int(order)
        to_answer = odpowiedz[order-1] 
        context = {'pytanie':None, 'id':order, 'nazwa_pliku':cardname}
        context['odpowiedz'] =to_answer
        context['pytanie'] = pytanie[order-1]
   
    return render(request, 'questions.html', context)

@login_required
def add_question(request):
    if request.method == 'POST':
        form = PytaniaForm(request.POST)

        if form.is_valid():
            added_question=form.save(commit=False)
            added_question.user = request.user.username
            added_question.save()
            return HttpResponseRedirect('/cards/')
    
    form = PytaniaForm ()
    context = {'form':form}
    return render(request, 'pytania_form.html', context)

@login_required
def delete_card(request, username, cardname):
    Pytania.objects.filter(user=username, carddeck=cardname).delete()
    return HttpResponseRedirect('/cards/')

@login_required
def edit_cards(request, username, cardname):
    qs = Pytania.objects.filter(user=username, carddeck=cardname)
    context = {'qs':qs}
    return render(request, 'edit_cards.html', context)

@login_required
def del_single_card(request, order,username,cardname):
    Pytania.objects.filter(user=username, carddeck=cardname,id=order).delete()
    qs = Pytania.objects.filter(user=username, carddeck=cardname)
    if qs:
        path = '/cards/edit/%s/%s' % (username, cardname)
        return HttpResponseRedirect(path) 
    else:
        return HttpResponseRedirect('/cards/')

@login_required
def edit_single_card(request, order,username,cardname):
    instance = get_object_or_404(Pytania, id=order)
    form = PytaniaForm(request.POST or None, instance=instance)

    if request.method == 'POST':
        pytanie = request.POST.get('pytanie')
        odpowiedz = request.POST.get('odpowiedz')
        username = request.POST.get('user')
        carddeck = request.POST.get('carddeck')

        if form.is_valid():
            edited_question=form.save(commit=False)
            edited_question.user = request.user.username
            edited_question.save()
            username=request.user.username
            path = '/cards/edit/%s/%s' % (username, cardname)
            return HttpResponseRedirect(path)

    else:
        context = {'form':form}
        return render(request, 'edit_single_card.html', context)
