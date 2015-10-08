from unittest import TestCase

import tests.config as conf
import recipe
from recipes.video.metadata import getattribute

__author__ = 'elon'

recipes = recipe.RecipeManager()


class TestCrop(TestCase):
    def test_run(self):
        result = next(recipes.video.transformations.crop(duration=conf.CROP_LENGTH).cook([conf.SAMPLE_VIDEO_AND_DURATION[0]]))
        duration = getattribute.get_duration(result)
        self.assertEqual(int(duration), conf.CROP_LENGTH)
