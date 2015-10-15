from unittest import TestCase

import tests.config as conf
import recipe

__author__ = 'elon'

recipes = recipe.RecipeManager('train_vid_bot')


class TestGet(TestCase):
    def test_duration(self):
        result = next(recipes.video.metadata.getattribute(attribute='duration').cook(conf.SAMPLE_VIDEO_AND_DURATION[0]))
        self.assertEqual(int(result), conf.SAMPLE_VIDEO_AND_DURATION[1])
