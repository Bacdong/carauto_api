web: gunicorn carauto.wsgi --log-file - --log-level debug
python3 manage.py collectstatic --noinput
manage.py migrate