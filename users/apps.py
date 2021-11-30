from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        print(f'users.signal ready on UsersAppConfig')
        import users.signals
