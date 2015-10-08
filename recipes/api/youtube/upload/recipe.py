import httplib2
import oauth2client.client
import googleapiclient.discovery
import googleapiclient.http

import recipe.rcp
from .resumable_upload import resumable_upload

__author__ = 'elon'


class Recipe(recipe.rcp.BaseRecipe):
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"

    def run(self, input, oauth, title, description, category=22, privacy_status="public", tags=[]):
        credentials = oauth.get(self.YOUTUBE_UPLOAD_SCOPE)
        youtube = googleapiclient.discovery.build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION,
                                                  http=credentials.authorize(httplib2.Http()))

        body = {"snippet":
                    {"title": title,
                     "description": description,
                     "tags": tags,
                     "categoryId": category},
                "status": {
                    "privacyStatus": privacy_status
                }
                }

        insert_request = youtube.videos().insert(part=",".join(list(body.keys())), body=body,
                                                 media_body=googleapiclient.http.MediaFileUpload(input, chunksize=-1,
                                                                                                 resumable=True))

        resumable_upload(insert_request)
        yield input