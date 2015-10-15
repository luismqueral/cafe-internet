#########################################
import random
import recipe, recipe.pipe, recipe.rcp
from train_vid_bot.api.oauth import OAuth
#########################################

tvbrecipes = recipe.RecipeManager('train_vid_bot')

r = recipe.pipe.Pipe(
    items=[
        tvbrecipes.files.selectrandom(
            number_of_files=3
        ),
        tvbrecipes.video.transformations.crop(
            duration=random.randint(15, 45)
        ),
        tvbrecipes.video.effects.blend(
            opacity=0.7
        ),
        tvbrecipes.video.addaudio(
            audio=tvbrecipes.files.selectrandom(
                number_of_files=1

            ).cook('/path/to/audiofolder/')
        ),
        tvbrecipes.api.youtube.upload( oauth = OAuth(
                                        client_id='####',
                                        client_secret='####',
                                        storage_path='/path/to/credentials_storage.oauth'
                                        ),

                                    title = tvbrecipes.hamburgermusic(
                                        api_key='###',
                                        number_of_lines=1,
                                        minimum_length=5,
                                        capitalize=False
                                        ).cook(),

                                    description = tvbrecipes.hamburgermusic(
                                        api_key='###',
                                        number_of_lines=5,
                                        minimum_length=3,
                                        capitalize=True
                                        ).cook()
                                    ),
        ]
).cook('/path/to/videofolder/')

recipe.rcp.start_and_print_results(r)
