from django.shortcuts import render
from django.views.generic.detail import DetailView

from gamelibrary.models import Game


class GameDetailView(DetailView):
    model = Game
