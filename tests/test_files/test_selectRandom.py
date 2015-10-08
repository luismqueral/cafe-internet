from unittest import TestCase
import os

import tests.config as conf

import recipe

__author__ = 'elon'

recipes = recipe.RecipeManager()


class TestSelectRandom(TestCase):
    def test_valid(self):
        result = recipes.files.selectrandom(number_of_files=3).cook(conf.SAMPLE_VIDEO_FOLDER)
        self.assertEqual(len(set(result)), 3)
        for filepath in result:
            self.assertTrue(os.path.isfile(filepath))

    def test_random(self):
        files = set()
        for _ in range(25):
            result = recipes.files.selectrandom(number_of_files=3).cook(conf.SAMPLE_VIDEO_FOLDER)
            files.update(result)
        self.assertGreater(len(files), 3)
