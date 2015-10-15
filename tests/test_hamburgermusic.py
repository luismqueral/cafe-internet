from unittest import TestCase
import recipe
import tests.config as conf

__author__ = 'elon'


recipes = recipe.RecipeManager('train_vid_bot')

class TestHamburgerMusic(TestCase):

    def test_hamburger_music(self):
        r = next(recipes.hamburgermusic(api_key=conf.GOOGLE_API_KEY).cook())
        print(r)
        self.assertIsInstance(r, str)
        self.assertGreaterEqual(len(r), 3)
