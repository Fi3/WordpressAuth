from django.test import TestCase
from .WordpressAPI import WordpressAPI
from .AuthenticationMethods import isAuthenticated
from .AuthenticationMethods import _checkSubscription
from WordpressAuth.testData.fakeResponse import listSubscription

class TestWordpressAPI(TestCase):

    def test_isAuthenticated_for_a_authenticated_userSession(self):
        """
        isAuthenticated should return true if userSession is authenticated
        """
        userSession = type('obj', (object,), {'isAuthenticated': lambda: True})
        WpApi = type('obj', (object,), {'_userSession': userSession})

        actual = isAuthenticated(WpApi)
        expected = True

        self.assertEqual(actual, expected)

    def test_checkSubscription_for_an_active_user(self):
        """
        checkSubscription should return true if userId has at least one activive subscription
        """
        actual = _checkSubscription(listSubscription, 5)
        expected = True

        self.assertEqual(actual, expected)

    def test_checkSubscription_for_an_inactive_user(self):
        """
        checkSubscription should return false if userId has no active subscriptions
        """
        actual = _checkSubscription(listSubscription, 7)
        expected = False

        self.assertEqual(actual, expected)

    def test_checkSubscription_for_an_user_without_subscriptions(self):
        """
        checkSubscription should return false if userId has not subscriptions
        """
        actual = _checkSubscription(listSubscription, 7)
        expected = False

        self.assertEqual(actual, expected)
