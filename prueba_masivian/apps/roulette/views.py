from django.shortcuts import render,redirect
from .models import *
from django.template import Library
from .forms import *

register = Library()


def index(request):
    roulettes=Roulette.objects.all()    
    players=Player.objects.all()
    bets=Bet.objects.all()
    context={
        'players':players,
        'roulettes':roulettes,
        'bets':bets,
    }
    return render(request,'index.html',context)

def createPlayer(request):
    if request.method == 'GET':
        form=playerForm()
        context={
            'form':form
        }
    else:
        form=playerForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'create_player.html',context)

def updatePlayer(request,id):
    player=Player.objects.get(id=id)
    if request.method == 'GET':
        form=playerForm(instance=player)
        context={
            'form':form
        }
    else:
        form=playerForm(request.POST,instance=player)
        context={
            'form':form
        }
        if form.is_valid() and player.funds>=0:
            form.save()
            return redirect('index')
    return render(request,'create_player.html',context)
        
def deletePlayer(request,id):
    player=Player.objects.get(id=id)
    player.delete()
    return redirect('index')

def createRoulette(request):
    if request.method == 'GET':
        form=rouletteForm()
        context={
            'form':form
        }
    else:
        form=rouletteForm(request.POST)
        context={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'create_player.html',context)

def placeBet(request,id_roulette,id_player):
    roulette=Roulette.objects.get(id=id_roulette)
    player=Player.objects.get(id=id_player)
    if request.method == 'GET':
        formRoulette=rouletteForm(instance=roulette)
        formPlayer=playerForm(instance=player)
        context={
            'formRoulette':formRoulette,
            'formPlayer':formPlayer
        }
    else:
        formPlayer=playerForm(request.POST,instance=player)
        formRoulette=rouletteForm(request.POST,instance=player)
        context={
            'formRoulette':formRoulette,
            'formPlayer':formPlayer
        }
        if formRoulette.is_valid() and formPlayer.is_valid () and roulette.Bets<10000 and player.funds>=0:
            formRoulette.save()
            formPlayer.save()
            return redirect('index')
    return render(request,'place_bet.html',context)
