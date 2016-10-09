# This file is exec'd from settings.py, so it has access to and can
# modify all the variables in settings.py.

# If this file is changed in development, the development server will
# have to be manually restarted because changes will not be noticed
# immediately.

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "7d$#$qt=*443d&1=j7rq)e=$g58z_r4!!qk%4r-!lcgpa)dho1"
NEVERCACHE_KEY = "*z0ybzkuysk28r+jta-9z#9s_l&m66cd7fksfc8s*cdrd#2a90"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

###################
# DEPLOY SETTINGS #
###################

# Domains for public site
ALLOWED_HOSTS = [
    "blogi.cc",
    "riot.blogi.cc",
    "107.170.2.39",
    "logileifs.pw",
    "riot.logileifs.pw",
    "188.166.168.4",
    "139.59.162.232",
    "139.59.190.55",
    "178.62.5.141",
    "178.62.69.30"
]

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

'''FABRIC = {
 "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
 "SSH_USER": "pi",  # VPS SSH username
 "HOSTS": ["89.160.214.73"],  # The IP address of your VPS
 "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
 "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
 "LOCALE": "en_GB.UTF-8",  # Should end with ".UTF-8"
 "DB_PASS": "riot",  # Live database password
 "ADMIN_PASS": "admin",  # Live admin user password
 "SECRET_KEY": SECRET_KEY,
 "NEVERCACHE_KEY": NEVERCACHE_KEY,
}'''

FABRIC = {
 "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
 "SSH_USER": "riot",  # VPS SSH username
 "HOSTS": ["178.62.69.30"],  # The IP address of your VPS
 "DOMAINS": ALLOWED_HOSTS,  # Edit domains in ALLOWED_HOSTS
 "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
 "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
 "DB_PASS": "riot",  # Live database password
 "ADMIN_PASS": "admin",  # Live admin user password
 "SECRET_KEY": SECRET_KEY,
 "NEVERCACHE_KEY": NEVERCACHE_KEY,
}
