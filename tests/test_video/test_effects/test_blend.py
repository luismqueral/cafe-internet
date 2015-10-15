from unittest import TestCase
import subprocess

import tests.config as conf

import recipe

recipes = recipe.RecipeManager('train_vid_bot')

__author__ = 'elon'


class TestBlend(TestCase):
    NUMBER_OF_VIDEOS = 3

    def test_cook(self):
        result = next(recipes.video.effects.blend().cook(conf.SAMPLE_VIDEOS[:self.NUMBER_OF_VIDEOS]))
        self.assertEqual(subprocess.call(['ffprobe', result]), 0)
