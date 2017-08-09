from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from gamelibrary.models import (Game,
                                GameDevelopper,
                                GameEditor,
                                GameGenre)


class GameDetailView(DetailView):
    model = Game


class DevelopperRelatedListView(ListView):

    def get_queryset(self):
        """
        Fetches Games related to a developper defined in the "slug" url kwarg
        """

        developper = get_object_or_404(GameDevelopper,
                                       slug=self.kwargs["slug"])

        return developper.developped_games.all()


class EditorRelatedListView(ListView):
    """
    View listing all Game objects related to a specific editor
    """

    def get_queryset(self):
        """
        Fetches Games related to an editor defined in the "slug" url kwarg
        """

        editor = get_object_or_404(GameEditor, slug=self.kwargs["slug"])

        return editor.edited_games.all()


class GenreRelatedListView(ListView):
    """
    View listing all game objects related to a specific genre
    """

    def get_queryset(self):
        """
        Fetches Games related to a genre defined in the "slug" url kwarg
        """

        genre = get_object_or_404(GameGenre, slug=self.kwargs["slug"])

        return genre.related_games.all()
