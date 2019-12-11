import requests
from django.shortcuts import render, redirect
from .models import Hero
from .forms import HeroForm
from django.http import HttpResponseRedirect


def index(request):
    url = 'https://gateway.marvel.com/v1/public/characters?name={}&ts=1575049124.7812767&apikey=6015ebfe6c6849dd6d84f80fca211911&hash=e9a66a3fbfc4ee6aacb16e24004d8634'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = HeroForm(request.POST)

        if form.is_valid():
            new_hero = form.cleaned_data['name']
            existing_hero_count = Hero.objects.filter(
                name=new_hero.title()).count()

            if existing_hero_count == 0:
                r = requests.get(url.format(new_hero)).json()
                # print(r)
                if r['data']['total'] == 1:
                    form.save()
                else:
                    err_msg = 'Hero does not exist in the world!'

            else:
                err_msg = 'Hero already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'Hero added successfully!'
            message_class = 'is-success'

    form = HeroForm()

    heroes = Hero.objects.all()

    heroes_data = []

    for hero in heroes:
        r = requests.get(url.format(hero)).json()

        hero = {
            'name': hero.name,
            'description': r['data']['results'][0]['description'],
            'thumbnail': r['data']['results'][0]['thumbnail']['path'],
            'comics': r['data']['results'][0]['comics']['items'],
            'stories': r['data']['results'][0]['stories']['items'],
        }

        heroes_data.append(hero)
    context = {
        'heroes_data': heroes_data,
        'form': form,
        'message': message,
        'message_class': message_class
    }
    return render(request, 'project_m/project_m.html', context)


def delete_hero(request, hero):
    Hero.objects.get(name=hero).delete()
    return redirect('index')
