from unittest import TestCase

import tests.config as conf
import recipe

__author__ = 'elon'

recipes = recipe.RecipeManager()


class TestAddAudio(TestCase):
    def test_cook(self):
        recipes.video.addaudio(audio=conf.SAMPLE_AUDIOS[0]).cook(conf.SAMPLE_VIDEOS[0])
