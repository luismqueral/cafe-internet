import oauth2client.client
import oauth2client.file

__author__ = 'elon'

def consolecallback(authorize_url):
    print("\n" * 5)
    print("Please navigate to {authorize_url} and authorize this application".format(authorize_url=authorize_url))
    code = input("Code: ")
    return code


class OAuth:
    REDIRECT_URL = 'urn:ietf:wg:oauth:2.0:oob'

    def __init__(self, client_id, client_secret, storage_path, callback=consolecallback):
        self.client_id = client_id
        self.client_secret = client_secret
        self.storage = oauth2client.file.Storage(storage_path)
        self.callback = callback

    def get(self, scopes):
        self.storage.acquire_lock()
        credentials = self.storage.locked_get()

        if credentials is None or not credentials.has_scopes(scopes):
            try:
                new_scopes = credentials.scopes + scopes
            except AttributeError:
                new_scopes = scopes

            credentials = self._generate_credentials(new_scopes)
            credentials.set_store(self.storage)
            self.storage.locked_put(credentials)

        self.storage.release_lock()
        return credentials

    def _generate_credentials(self, scopes):
        flow = oauth2client.client.OAuth2WebServerFlow(self.client_id, self.client_secret, scope=scopes,
                                                       redirect_uri=self.REDIRECT_URL)
        authorize_url = flow.step1_get_authorize_url()
        code = self.callback(authorize_url)
        credentials = flow.step2_exchange(code)
        return credentials