from django.apps import AppConfig


class BbcscapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bbcscapper'

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()