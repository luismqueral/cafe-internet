import subprocess
import recipe.rcp
import recipe.temppath


class Recipe(recipe.rcp.BaseRecipe):
    input_handler = staticmethod(recipe.rcp.all_inputs_handler)
    ingredient_handlers = {'opacity': recipe.rcp.all_ingredients_handler, 'blend_mode': recipe.rcp.all_ingredients_handler}
    CONTAINER_FORMAT = 'mp4'

    def run(self, input, opacity=recipe.rcp.single_ingredient_handler(0.7), blend_mode=recipe.rcp.single_ingredient_handler('overlay')):
        command = ['ffmpeg']
        input = list(input)
        number_of_inputs = len(input)

        for index, path in enumerate(input):
            command.append('-i')
            command.append(path)

        filter_complex = ""

        for i in range(number_of_inputs):
            filter_complex += "[{index}:v]format=rgba[in{index}];".format(index=i)

        filter_complex += "[in0]null"

        for i in range(1, number_of_inputs):
            filter_complex += ",[in{index}]blend=all_mode='{blend_mode}':all_opacity={opacity}".format(index=i,
                                                                                                       blend_mode=next(blend_mode),
                                                                                                       opacity=next(opacity))

        filter_complex += "[out]"

        blendedvideo = recipe.temppath.tempfilepath()
        command.extend(['-filter_complex', filter_complex, '-map', '[out]', '-f', self.CONTAINER_FORMAT, blendedvideo])
        subprocess.call(command)

        yield blendedvideo

