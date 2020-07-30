web: gunicorn carauto.carauto.wsgi:application --log-file - --log-level debug
cd ..
python manage.py collectstatic --noinput
manage.py migrate