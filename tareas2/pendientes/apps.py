from django.apps import AppConfig


class PendientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pendientes'

    def ready(self):
        import pendientes.signals
