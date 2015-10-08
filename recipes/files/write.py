import shutil

from recipe.rcp import BaseRecipe


class Recipe(BaseRecipe):

    def run(self, input, path):
        shutil.copy(input, path)

        yield input
