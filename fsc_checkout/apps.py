"""

checkout/apps.py: config file for checkout app

"""


# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class FscCheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fsc_checkout'

    def ready(self):
        # pylint: disable=unused-import, import-outside-toplevel
        import fsc_checkout.signals # noqa