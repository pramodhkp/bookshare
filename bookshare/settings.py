from os.path import abspath, dirname, basename, join

try:
    import social_auth
except ImportError:
    import sys
    sys.path.insert(0, "..")

import dj_database_url
# DATABASES = {'default': dj_database_url.config()}
DATABASES = {'default': dj_database_url.parse('postgres://localhost')}

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ROOT_PATH = abspath(dirname(__file__))
PROJECT_NAME = basename(ROOT_PATH)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',              
        'USER': 'postgres',
        'PASSWORD': 'praday',
        'HOST': 'localhost',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = '/home/u/bookshare/bookshare/assets/'
ADMIN_MEDIA_PREFIX = '/media/'
MEDIA_URL = '/assets/'

SECRET_KEY = 't2eo^kd%k+-##ml3@_x__$j0(ps4p0q6eg*c4ttp9d2n(t!iol'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (    
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',   
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'bookshare.urls'

TEMPLATE_DIRS = (
    join(ROOT_PATH, 'templates'),
    join(ROOT_PATH, '/django-postman/postman/templates'),
    join(ROOT_PATH, '/disqus/templates'),
    join(ROOT_PATH, '/submitbook/templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    #'django.contrib.staticfiles',
    'social_auth',
    'app',
    'postman',
    'pagination',
    'disqus',
    'actstream',
    'submitbook', 
    
)

DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''


TWITTER_CONSUMER_KEY         = ''
TWITTER_CONSUMER_SECRET      = ''
FACEBOOK_APP_ID              = ''
FACEBOOK_API_SECRET          = ''
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID = ''
LIVE_CLIENT_SECRET = ''
SKYROCK_CONSUMER_KEY      = ''
SKYROCK_CONSUMER_SECRET   = ''
YAHOO_CONSUMER_KEY        = ''
YAHOO_CONSUMER_SECRET     = ''

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in'
LOGIN_ERROR_URL    = '/login-error/'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.flickr.FlickrBackend',
    'social_auth.backends.contrib.instagram.InstagramBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.yandex.YandexBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.OpenIDBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.douban.DoubanBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'social_auth.backends.contrib.yandex.YandexOAuth2Backend',
    'social_auth.backends.contrib.yandex.YaruBackend',
    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteOAuth2Backend',
    'social_auth.backends.contrib.mailru.MailruBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_type_backends',
    'postman.context_processors.inbox',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
)

POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True


LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'app.pipeline.redirect_to_form',
    'app.pipeline.username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'app.pipeline.redirect_to_form2',
    'app.pipeline.first_name',
)

try:
    from local_settings import *
except:
    pass
