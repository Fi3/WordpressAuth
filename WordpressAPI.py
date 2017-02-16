import requests
from urllib.parse import urljoin

class WordpressAPI:
    """
    Wordpress API, expose several method to authenticate an user in wordpress
    """

    def __init__(self, url, user, password, admin, adminPassword,
                 sessionManager, authMethod):
        self._url = url
        self._user = user
        self._password = password
        self._admin = admin
        self._adminPassword = adminPassword
        self._userSession = getattr(self, '_' + sessionManager,
                                    lambda a, b: 'no auth method')(user, password);
        self._adminSession = getattr(self, '_' + sessionManager,
                                    lambda a, b: 'no auth method')(admin, adminPassword);
        self._authMethod = authMethod;
        self._checkAdminSession();

    def _JWT(self, user, password):
        """
        Authenticate against wordpress JWT AUTH plugin:
        https://github.com/Tmeister/wp-api-jwt-auth
        """
        return JWTAuth(self._url, user, password)

    def isAuthenticated(self):
        return self._authMethod(self)

    def userId(self):
        """
        return the user id, if not authenticated throw error
        """
        endpoint = 'wp-json/wp/v2/users'
        if self._userSession.isAuthenticated() == True:
            return idFromUsers(self._adminSession.get(endpoint).json(), self._user)
        else:
            return 'userNotAuth:WordpressApi.userId'

    def _TestAuth(self, user, password):#TODO name should be testSession
        return '_TestAuth'

    def _checkAdminSession(self):
        if not self._adminSession.isAuthenticated():
            raise UnknownError

class JWTAuth():
    """
    Authenticate against wordpress JWT AUTH plugin:
    https://github.com/Tmeister/wp-api-jwt-auth
    """

    def __init__(self, url, user, password):
        self._url = url
        self._user = user
        self._password = password
        self._session = False
        self._connect()

    def _connect(self):
        """
        Authenticate against wordpress and return a raw requests object
        """
        endpoint = 'wp-json/jwt-auth/v1/token'
        get_token_url = urljoin(self._url, endpoint)
        data = {'password': self._password, 'username': self._user}
        session = requests.post(get_token_url, data)
        # TODO log session and get_token_url
        self._session = session
        return session

    def isAuthenticated(self):
        """
        Return true if _user and _password are ok
        """
        if self._session.status_code == 200:
            return True
        else:
            return False

    def _sessionToken(self):
        return self._session.json()['token']

    def _sessionHeader(self):
        return {'Authorization': 'Bearer ' + self._sessionToken()}

    def get(self, endpoint):
        url = urljoin(self._url, endpoint)
        return requests.get(url, headers=self._sessionHeader())

def idFromUsers(userList, userSlug):
    """
    filter the userLsit for a particular slug, if the slug is in the list return the
    correspondent id, if is not in the list or there is more than one match return an
    error message
    """
    match = list(filter(lambda x: x['slug'] == userSlug, userList))
    if len(match) == 0:
        return 'noSlug:WordpressApi.idFromUser'
    elif len(match) == 1:
        return match[0]['id']
    else:
        raise UnimplementedError
