from django.test import TestCase
from django.urls import reverse

from gamelibrary.models import (Game,
                     GameDevelopper,
                     GameEditor,
                     GameGenre)


class GameModelTests(TestCase):
    def test_expected_absolute_url(self):
        """
        Test model's get_absolute_url for correctness
        """
        
        game = Game(title="Test Game")
        game.save()

        expected_url = reverse(game.url_name,
                               kwargs={"slug": game.slug})

        self.assertEqual(expected_url, game.get_absolute_url())


class GameDevelopperModelTests(TestCase):
    def test_expected_absolute_url(self):
        """
        Test model's get_absolute_url for correctness
        """

        dev = GameDevelopper(title="Test Developper")
        dev.save()

        expected_url = reverse(dev.url_name,
                               kwargs={"slug": dev.slug})

        self.assertEqual(expected_url, dev.get_absolute_url())


class GameEditorModelTests(TestCase):
    def test_expected_absolute_url(self):
        """
        Test model's get_absolute_url for correctness
        """

        editor = GameEditor(title="Test Editor")
        editor.save()

        expected_url = reverse(editor.url_name,
                               kwargs={"slug": editor.slug})

        self.assertEqual(expected_url, editor.get_absolute_url())


class GameGenreModelTests(TestCase):
    def test_expected_absolute_url(self):
        """
        Test model's get_absolute_url for correctness
        """

        genre = GameGenre(title="Test Genre")
        genre.save()

        expected_url = reverse(genre.url_name,
                               kwargs={"slug": genre.slug})

        self.assertEqual(expected_url, genre.get_absolute_url())
