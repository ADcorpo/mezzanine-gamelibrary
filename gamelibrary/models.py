from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.utils.models import AdminThumbMixin
from mezzanine.core.models import Displayable, RichText, Slugged


class AbsoluteURLFromSlugMixin(object):
    """
    Provides a default get_absolute_url implementation
    for items that have a slug.

    Associated Models must have an url_name property defined.
    """

    # Would it be useful to define a base url_name here?

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}

        return reverse(self.url_name, kwargs=kwargs)


class Game(AbsoluteURLFromSlugMixin, Displayable, RichText, AdminThumbMixin):
    cover = models.ImageField(verbose_name=_("Cover"),
                              blank=True,
                              null=True)

    developper = models.ForeignKey("GameDevelopper",
                                   verbose_name=_("Developper"),
                                   blank=True,
                                   null=True,
                                   related_name="developped_games")
    editor = models.ForeignKey("GameEditor",
                               verbose_name=_("Editor"),
                               blank=True,
                               null=True,
                               related_name="edited_games")

    genres = models.ManyToManyField("GameGenre",
                                    verbose_name=_("Genre(s)"),
                                    blank=True,
                                    related_name="related_games")

    url_name = "game-detail"


class GameRelease(models.Model):
    """
    Represents a game release by his date and a short informative text
    """

    # It makes sense to have the release pointing to the game
    # as a single release won't ever be used for two different games
    game = models.ForeignKey("Game",
                             related_name="releases")

    date = models.DateField()
    info = models.CharField(max_length=256)

    def __str__(self):
        return str(self.date) + " " + self.game.title


class GameDevelopper(Slugged, AbsoluteURLFromSlugMixin):
    """
    Represents a game developper or a game development studio.
    """

    url_name = "game-list-dev"


class GameEditor(Slugged, AbsoluteURLFromSlugMixin):
    """
    Represents a game editor.
    """

    url_name = "game-list-editor"


class GameGenre(Slugged, AbsoluteURLFromSlugMixin):
    """
    Represents a game genra.
    """

    url_name = "game-list-genre"
