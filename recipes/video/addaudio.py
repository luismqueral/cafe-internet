import subprocess
import recipe.rcp
import recipe.temppath


class Recipe(recipe.rcp.BaseRecipe):
    CONTAINER_FORMAT = 'mp4'

    def run(self, input, audio):
        processedvideo = recipe.temppath.tempfilepath()
        subprocess.call(
            ['ffmpeg', '-i', input, '-i', audio, '-map', '0:v', '-c', 'copy', '-map', '1:a', '-c', 'copy',
             '-shortest', '-f', self.CONTAINER_FORMAT, processedvideo])

        yield processedvideo
