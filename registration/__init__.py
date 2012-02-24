from django.conf import settings
#from django.core.exceptions import ImproperlyConfigured

#def checkconf(name, msg):
#    """check django.conf.settings is proprely configured"""
#    if not hasattr(settings, name):
#        raise ImproperlyConfigured(msg)

def setconf(name, default_value):
    """set default value to django.conf.settings"""
    value = getattr(settings, name, default_value)
    setattr(settings, name, value)

setconf('ACCOUNT_ACTIVATION_DAYS', 7)
setconf('REGISTRATION_DEFAULT_PASSWORD_LENGTH', 10)
setconf('REGISTRATION_BACKEND_CLASS', 'registration.backends.default.DefaultBackend')
setconf('REGISTRATION_ADDITION_CLASS', 'registration.additions.default.DefaultAddition')
setconf('REGISTRATION_OPEN', True)
