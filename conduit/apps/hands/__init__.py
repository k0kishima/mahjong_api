from django.apps import AppConfig


class HandsAppConfig(AppConfig):
    name = 'conduit.apps.hands'
    label = 'hands'
    verbose_name = 'Hands'

default_app_config = 'conduit.apps.hands.HandsAppConfig'
