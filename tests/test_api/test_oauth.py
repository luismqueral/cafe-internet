from unittest import TestCase

import httplib2

import tests.config as conf
from recipes.api.oauth import OAuth
import recipe.temppath

__author__ = 'elon'


class TestOAuth(TestCase):
    SCOPE = "https://www.googleapis.com/auth/youtube.upload"

    def setUp(self):
        self.temppath = recipe.temppath.TempFilePath()
        self.oauth = OAuth(conf.GOOGLE_CLIENT_ID, conf.GOOGLE_CLIENT_SECRET, self.temppath)

    def test_get_scope(self):
        credentials = self.oauth.get(self.SCOPE)
        authorized_http = credentials.authorize(httplib2.Http())
        credentials.retrieve_scopes(authorized_http)
        self.assertTrue(credentials.has_scopes(self.SCOPE))
