import recipe.rcp
import recipe.temppath
import subprocess


class Recipe(recipe.rcp.BaseRecipe):
    CONTAINER_FORMAT = 'mp4'

    def run(self, input, duration):
        croppedvideo = recipe.temppath.tempfilepath()
        subprocess.call(['ffmpeg', '-i', input, '-t', str(duration), '-c:v', 'copy', '-c:a', 'copy', '-f',
                         self.CONTAINER_FORMAT, croppedvideo])
        yield croppedvideo
