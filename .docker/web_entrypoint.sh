pip install -r /code/requirements.txt
python /code/manage.py migrate --all --noinput
python /code/manage.py collectstatic --noinput
python /code/manage.py runserver 0.0.0.0:8000
