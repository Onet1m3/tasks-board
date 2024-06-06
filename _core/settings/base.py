from pathlib import Path

from split_settings.tools import include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

components_settings = [
    'components/db.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/templates.py',
    'components/password_validators.py',
    'components/internationalization.py',
    'components/static.py',
    'components/rest_framework.py',
    'components/spectacular.py',
    'components/general.py',
]


include(*components_settings)