from unittest import TestCase
import random

import tests.config as conf
import recipe
import recipe.pipe
import recipe.rcp

__author__ = 'elon'

recipes = recipe.RecipeManager()


class TestSampleRecipe(TestCase):
    def test_sample_recipe(self):
        r = recipe.pipe.Pipe(
            items=[
                recipes.files.selectrandom(
                    number_of_files=3
                ),
                recipes.video.transformations.crop(
                    duration=random.randint(15, 45)
                ),
                recipes.video.effects.blend(
                    opacity=0.7
                ),
                recipes.video.addaudio(
                    audio=recipes.files.selectrandom(
                        number_of_files=1

                    ).cook(conf.SAMPLE_AUDIO_FOLDER)
                )
            ]
        ).cook(conf.SAMPLE_VIDEO_FOLDER)

        recipe.rcp.start_and_print_results(r)

        # Generate poetry
        # Upload video to YouTube
