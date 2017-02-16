from django.test import TestCase
from .WordpressAPI import WordpressAPI
from .WordpressAPI import idFromUsers
from WordpressAuth.testData.fakeResponse import listUser

class TestWordpressAPI(TestCase):

    def test_userSession_returned_value_for_not_impl_method(self):
        """
        self._userSession should return 'no auth method' for an session_manager
        not implemented
        """
        session_manager = 'oAUTH'
        myWordPressAuth = WordpressAPI('url','user','password','a','p',session_manager,
                                        lambda x: x)

        actual = myWordPressAuth._userSession
        expected = 'no auth method'

        self.assertEqual(actual, expected)

    def test_userSession_returned_value_for_impl_method(self):
        """
        self._userSession should call the session_manager for an
        implemented session_manager
        """
        session_manager = 'TestAuth'
        myWordPressAuth = WordpressAPI('url','user','password','a','p',session_manager,
                                        lambda x: x)

        actual = myWordPressAuth._userSession
        expected = '_TestAuth'

        self.assertEqual(actual, expected)

    def test_adminSession_returned_value_for_not_impl_method(self):
        """
        self._adminSession should return 'no auth method' for an session_manager
        not implemented
        """
        session_manager = 'oAUTH'
        myWordPressAuth = WordpressAPI('url','user','password','a','p',session_manager,
                                        lambda x: x)

        actual = myWordPressAuth._adminSession
        expected = 'no auth method'

        self.assertEqual(actual, expected)

    def test_adminSession_returned_value_for_impl_method(self):
        """
        self._adminSession should call the session_manager for an
        implemented session_manager
        """
        session_manager = 'TestAuth'
        myWordPressAuth = WordpressAPI('url','user','password','a','p',session_manager,
                                        lambda x: x)

        actual = myWordPressAuth._adminSession
        expected = '_TestAuth'

        self.assertEqual(actual, expected)

    def test_userId_returned_value(self):
        """
        userId() should return `userNotAuth` if the user is not authenticated
        """
        myWordPressAuth = WordpressAPI('url','user','password','a','p','no',lambda x: x)
        myWordPressAuth._userSession = type('obj', (object,), {'isAuthenticated':
                                             lambda: False})

        actual = myWordPressAuth.userId()
        expected = 'userNotAuth:WordpressApi.userId'

        self.assertEqual(actual, expected)

    def test_idFromUser_returned_value_for_user_in_list(self):
        """
        idFromUsers(userList, user) should return the user id for an user in userList
        """

        actual = idFromUsers(listUser, 'pippo')
        expected = 6

        self.assertEqual(actual, expected)

    def test_idFromUser_returned_value_for_user_not_in_list(self):
        """
        idFromUser(userList, user) should return `noSlug` for an user noty present in the list
        """

        actual = idFromUsers(listUser, 'canicanibauabu')
        expected = 'noSlug:WordpressApi.idFromUser'

        self.assertEqual(actual, expected)
