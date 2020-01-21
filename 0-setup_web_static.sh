#!/usr/bin/env bash
# Bash script to set up web servers for the deployment of web_static
sudo -i
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo 'temp file' | /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "42i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx reload
sudo service nginx restart
