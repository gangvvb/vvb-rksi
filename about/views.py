from django.shortcuts import render
from .models import Awards, Team


def about(request):
    awards = Awards.objects.all()
    team = Team.objects.all()
    return render(request, 'about/about.html', {'awards': awards, 'team': team})
