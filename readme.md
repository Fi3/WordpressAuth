##WordpressAuth

Add to settings.py

    WORDPRESS_URL = 'https://ex.com'
    WORDPRESS_ADMNIN_USER = 'admin'
    WORDPRESS_ADMIN_PASSWORD = 'adminPassword'
    WORDPRESS_SESSION_MANAGER = 'JWT'
    WORDPRESS_AUTHENTICATION_METHOD = 'authenticateWcSubscription' or 'isAuthenticated'

###TEST
    ~mkdir test
    ~cd test
    ~virtualenv -p python3 env
    ~source env/bin/activate
    ~pip install django
    ~pip install requests
    ~django-admin startproject test
    ~cd test
    ~git clone https://github.com/Fi3/WordpressAuth
    ~python manage.py test
