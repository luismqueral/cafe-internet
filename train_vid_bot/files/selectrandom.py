import os
from random import sample

import recipe.rcp


class Recipe(recipe.rcp.BaseRecipe):

    def run(self, input, number_of_files=1):
        filelist = []
        for filename in os.listdir(input):
            filepath = os.path.join(input, filename)
            if os.path.isfile(filepath):
                filelist.append(filepath)

        for s in sample(filelist, number_of_files):
            yield s

