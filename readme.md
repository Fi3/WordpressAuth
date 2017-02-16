##WordpressAuth

Add to settings.py

    WORDPRESS_URL = 'https://ex.com'
    WORDPRESS_ADMNIN_USER = 'admin'
    WORDPRESS_ADMIN_PASSWORD = 'adminPassword'
    WORDPRESS_SESSION_MANAGER = 'JWT'
    WORDPRESS_AUTHENTICATION_METHOD = 'authenticateWcSubscription' or 'isAuthenticated'

###TEST
python manage.py test
