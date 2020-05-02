from django.contrib import admin
from django.apps import apps

admin.site.site_header = 'python-3v4l'

# auto-register all models
app = apps.get_app_config('core')

for model_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass