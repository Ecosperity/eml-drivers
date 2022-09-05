web: daphne emlbackend.asgi:application --port $PORT --bind 0.0.0.0 -v2
eml: python manage.py runworker --settings=emlbackend.settings -v2