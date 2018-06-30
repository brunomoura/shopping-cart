#!/usr/bin/env python
import os
import sys

from decouple import config

if __name__ == "__main__":
    settings_module = config('DJANGO_SETTINGS_MODULE', default=None)
    
    if sys.argv[1] == 'test':
        if settings_module:
            print("Ignoring config('DJANGO_SETTINGS_MODULE') because it's test. "
                  "Using 'ecommerce.settings.test'")
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings.test")
    
    else:
        if settings_module is None:
            print("Error: no DJANGO_SETTINGS_MODULE found. Will NOT start devserver. "
                "Remember to create .env file at project root. " 
                "Check README for more info.")
            sys.exit(1)
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
        
    execute_from_command_line(sys.argv)
