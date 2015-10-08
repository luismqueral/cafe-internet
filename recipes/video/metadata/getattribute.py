import subprocess
import json
import io

import recipe.rcp

__author__ = 'elon'

def ffprobe(target, options):
    command = ['ffprobe', '-print_format', 'json'] + options + [target]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
    data = json.loads(result)
    return data

def get_duration(target):

    return float(ffprobe(target, ['-show_format'])['format']['duration'])


attribute_mapping = {'duration': get_duration}


class Recipe(recipe.rcp.BaseRecipe):
    def run(self, input, attribute):

        yield attribute_mapping[attribute](input)