import hamburger_music.libpoetry
import recipe.rcp

__author__ = 'elon'


class Recipe(recipe.rcp.BaseRecipe):
    def run(self, input, api_key, number_of_lines=1, max_lines_per_video=2, randomness=2, minimum_length=3,
            wordrange=range(3, 6), capitalize=True, whitelist=(), blacklist=(), languages=("en",)):

        p = hamburger_music.libpoetry.Poet(api_key, wordrange, capitalize, whitelist, blacklist,
                                           randomness=max_lines_per_video, languages=languages,
                                           minsublength=minimum_length)

        yield p.makePoem(number_of_lines)
