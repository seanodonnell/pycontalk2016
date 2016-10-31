A django app that generates primes and leaks memory, purely to demonstrate pyvmmonitor


Download pyvmmonitor from http://www.pyvmmonitor.com/download.html

Install requirements

pip install -r requirements.txt

Start this django app with:
 python manage.py runserver
Start the locust example to hit it with traffic
 cd ../locustexample
locust -f simpletest.py

Start pyvmmonitor

sudo ./pyvmmonitor-ui

Connect to the runserver process and watch the stats
