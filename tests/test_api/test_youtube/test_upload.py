__author__ = 'elon'

from unittest import TestCase

import tests.config as conf
import recipe
from train_vid_bot.api.oauth import OAuth
import recipe.temppath

recipes = recipe.RecipeManager('train_vid_bot')


class TestYoutube(TestCase):
    TITLE = "Test"
    DESCRIPTION = "Foo bar baz"

    def test_upload(self):
        oauth = OAuth(conf.GOOGLE_CLIENT_ID, conf.GOOGLE_CLIENT_SECRET, conf.CREDENTIAL_FILE)
        r = recipes.api.youtube.upload(oauth=oauth,
                                       title=self.TITLE,
                                       description=self.DESCRIPTION).cook(conf.SAMPLE_VIDEOS[0])
        next(r)
