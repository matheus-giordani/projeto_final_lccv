from django.apps import AppConfig


class AulaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aula'


    def ready(self) -> None:
        from aula import signals