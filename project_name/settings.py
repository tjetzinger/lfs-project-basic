# python imports
import os

# django imports
from django.utils.translation import gettext_lazy as _

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = False

DEFAULT_FROM_EMAIL = 'your_email@example.com'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'webshop.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = "{{ secret_key }}"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'lfs.core.context_processors.main',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'lfs.utils.middleware.RedirectFallbackMiddleware',
    "pagination.middleware.PaginationMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = "{{ project_name }}.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "{{ project_name }}.wsgi.application"

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(PACKAGE_ROOT, "templates"),
)

INSTALLED_APPS = (
    "lfstheme",
    "compressor",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    "django.contrib.flatpages",
    "django.contrib.redirects",
    "django.contrib.sitemaps",
    'django_countries',
    "pagination",
    'reviews',
    "tagging",
    "portlets",
    "lfs",
    "lfs.tests",
    'lfs.core',
    'lfs.caching',
    'lfs.cart',
    'lfs.catalog',
    'lfs.checkout',
    "lfs.criteria",
    "lfs.customer",
    "lfs.discounts",
    "lfs.export",
    'lfs.gross_price',
    'lfs.integrationtests',
    'lfs.mail',
    'lfs.manage',
    'lfs.marketing',
    'lfs.manufacturer',
    'lfs.net_price',
    'lfs.order',
    'lfs.page',
    'lfs.payment',
    'lfs.portlet',
    'lfs.search',
    'lfs.shipping',
    'lfs.supplier',
    'lfs.tagging',
    'lfs.tax',
    "lfs.customer_tax",
    'lfs.utils',
    'lfs.voucher',
    'lfs_contact',
    "lfs_order_numbers",
    'postal',
    'paypal.standard.ipn',
    'paypal.standard.pdt',
    'debug_toolbar',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "fixtures"),
)

FORCE_SCRIPT_NAME=""
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/manage/"

AUTHENTICATION_BACKENDS = (
    'lfs.customer.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# For sql_queries
INTERNAL_IPS = (
    "127.0.0.1",
)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

CACHE_MIDDLEWARE_KEY_PREFIX = "lfs"
# CACHE_BACKEND = 'file:///'
# CACHE_BACKEND = 'locmem:///'
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_BACKEND = 'dummy:///'

EMAIL_HOST = "localhost"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PAYPAL_RECEIVER_EMAIL = "info@yourbusiness.com"
PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

# TODO: Put this into the Shop model
LFS_PAYPAL_REDIRECT = True
LFS_AFTER_ADD_TO_CART = "lfs_added_to_cart"
LFS_RECENT_PRODUCTS_LIMIT = 5

LFS_ORDER_NUMBER_GENERATOR = "lfs_order_numbers.models.OrderNumberGenerator"
LFS_DOCS = "http://docs.getlfs.com/en/latest/"

LFS_INVOICE_COMPANY_NAME_REQUIRED = False
LFS_INVOICE_EMAIL_REQUIRED = True
LFS_INVOICE_PHONE_REQUIRED = True

LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
LFS_SHIPPING_EMAIL_REQUIRED = False
LFS_SHIPPING_PHONE_REQUIRED = False

LFS_PRICE_CALCULATORS = [
    ['lfs.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
    ['lfs.net_price.NetPriceCalculator', _(u'Price excludes tax')],
]

LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
    ["lfs.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
    ["lfs.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
]

LFS_UNITS = [
    u"l",
    u"m",
    u"qm",
    u"cm",
    u"lfm",
    u"Package",
    u"Piece",
]

LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

LFS_LOG_FILE = PROJECT_ROOT + "/lfs.log"
LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
    },
    "handlers": {
         "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LFS_LOG_FILE,
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

REVIEWS_SHOW_PREVIEW = False
REVIEWS_IS_NAME_REQUIRED = False
REVIEWS_IS_EMAIL_REQUIRED = False
REVIEWS_IS_MODERATED = False

try:
    from local_settings import *
except ImportError:
    pass
