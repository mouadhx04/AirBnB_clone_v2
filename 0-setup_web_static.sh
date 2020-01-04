#!/usr/bin/env bash
# Bash script to set up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo -e '<html>\n<head>\n</head>\n<body>\nHolberton fake file\n</body>\n</html>' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "42i location /hbnb_static {\nalias /data/web_static/current;\n}" /etc/nginx/sites-available/default
sudo service nginx restart
