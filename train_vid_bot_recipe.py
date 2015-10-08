#########################################
import random
import recipe, recipe.pipe, recipe.rcp
from recipes.api.oauth import OAuth
recipes = recipe.RecipeManager()
#########################################


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

            ).cook('/path/to/audiofolder/')
        ),
        recipes.api.youtube.upload( oauth = OAuth(
                                        client_id='####',
                                        client_secret='####',
                                        storage_path='/path/to/credentials_storage.oauth'
                                        ),

                                    title = recipes.hamburgermusic(
                                        api_key='###',
                                        number_of_lines=1,
                                        minimum_length=5,
                                        capitalize=False
                                        ).cook(),

                                    description = recipes.hamburgermusic(
                                        api_key='###',
                                        number_of_lines=5,
                                        minimum_length=3,
                                        capitalize=True
                                        ).cook()
                                    ),
        ]
).cook('/path/to/videofolder/')

recipe.rcp.start_and_print_results(r)
