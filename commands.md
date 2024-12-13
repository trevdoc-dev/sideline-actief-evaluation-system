<!-- reset the database -->

rm db.sqlite3

<!-- recreate migrations and apply them -->

python manage.py makemigrations
python manage.py migrate

<!-- run the server -->

python manage.py runserver

<!-- create super user -->

python manage.py createsuperuser
