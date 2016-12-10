import sys

sys.path.insert(0,"/var/www/dontbejerkatig")

from web import app
app.secret_key = '1239dasHAUHS123&#L!'
application = app
