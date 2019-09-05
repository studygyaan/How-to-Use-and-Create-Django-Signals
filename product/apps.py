from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class ProductConfig(AppConfig):
    name = 'product'

    def ready(self):
        import product.signals  # noqa