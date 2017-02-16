##WordpressAuth

Add to settings.py

1. WORDPRESS_URL
2. WORDPRESS_ADMNIN_USER
3. WORDPRESS_ADMIN_PASSWORD
4. WORDPRESS_SESSION_MANAGER = 'JWT'
5. WORDPRESS_AUTHENTICATION_METHOD = 'authenticateWcSubscription' or 'isAuthenticated'

###TEST
python manage.py test
