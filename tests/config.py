###############################################################################################
SAMPLE_VIDEO_FOLDER = '/path/sampledata/video'
SAMPLE_AUDIO_FOLDER = '/path/sampledata/audio'

SAMPLE_VIDEO_AND_DURATION = ('/path/sampledata/video/1.mp4', 5)
CROP_LENGTH = 3

GOOGLE_CLIENT_ID = "####"
GOOGLE_CLIENT_SECRET = "####"
GOOGLE_API_KEY = "####"

CREDENTIAL_FILE = "/path/to/credentials.oauth"  # Comment out to always reauthenticate
###############################################################################################

import os
import recipe.temppath

SAMPLE_VIDEOS = [os.path.join(SAMPLE_VIDEO_FOLDER, entry) for entry in os.listdir(SAMPLE_VIDEO_FOLDER)]
SAMPLE_AUDIOS = [os.path.join(SAMPLE_AUDIO_FOLDER, entry) for entry in os.listdir(SAMPLE_AUDIO_FOLDER)]

if not 'CREDENTIAL_FILE' in globals():
    CREDENTIAL_FILE = recipe.temppath.TempFilePath()
