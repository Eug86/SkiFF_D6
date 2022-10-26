from django.apps import AppConfig


class SimpleappConfig(AppConfig):
    name = 'simpleapp'

    def ready(self):
        import simpleapp.signals
