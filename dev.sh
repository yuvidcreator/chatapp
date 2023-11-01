#! /bin/bash
set -e

# git pull origin main

# Activate the virtualenv for this project
source env/bin/activate
pip3 install --no-cache-dir -r requirements.txt
# sudo mkdir -pv /var/log/angelguides/
sudo mkdir -pv ./static

sudo mkdir -pv /var/www/angelguides/static
# sudo chown -cR ubuntu:ubuntu /var/log/angelguides
sudo chown -cR ubuntu:ubuntu /var/www/angelguides/static
sudo chown -cR ubuntu:ubuntu /var/www/angelguides/media

# Start gunicorn going
python3 manage.py collectstatic --noinput
# python3 manage.py makemigrations --noinput
# python3 manage.py migrate --noinput

sudo service supervisor restart
sudo service nginx restart