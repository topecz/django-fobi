__title__ = 'fobi.contrib.apps.djangocms_integration.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.apps.djangocms_integration'
        label = 'fobi_contrib_apps_djangocms_integration'

except ImportError:
    pass
