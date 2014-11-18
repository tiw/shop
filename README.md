export DATABASE_URI='mysql://root:@localhost:3308/system-interface'
export FLASK_CONFIG=production
python manage.py db init
python manage.py db migrate
python manage.py db upgrade