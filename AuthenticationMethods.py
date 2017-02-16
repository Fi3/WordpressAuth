def isAuthenticated(wpApi):
    """
    Just check if the login details provided are valids login details
    for the wordpress url
    """
    if wpApi._userSession.isAuthenticated() == True:
        return True
    elif wpApi._userSession.isAuthenticated() == False:
        return False
    else:
        raise UnimplementedError

def authenticateWcSubscription(wpApi):
    """
    Check if the user exist and if it has an active woocommwerce subscription
    """
    userId = wpApi.userId();
    subscriptionList = wpApi._adminSession.get('wp-json/wc/v1/subscriptions').json()
    if isAuthenticated(wpApi) and _checkSubscription(subscriptionList, userId):
        return True
    else:
        return False

def _checkSubscription(subscriptionsList, userId):
    """
    Check if the user has an active wc subscription
    """
    activeSubscriptioinForId = list(filter(lambda x: x['status'] == 'active' and
                                      x['customer_id'] == userId, subscriptionsList))
    if len(activeSubscriptioinForId) > 0:
        return True
    else:
        return False
