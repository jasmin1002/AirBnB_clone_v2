#!/usr/bin/env bash
# Web Servers Setup.

[ ! -d /etc/nginx ] && sudo apt update && sudo apt -y install nginx
[ -d /data ] || mkdir -p /data/web_static/releases /data/web_static/shared /data/web_static/releases/test/
sudo printf "%s <html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
[ -e /data/web_static/current ] && rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo sed -i 's/server_name _;/server_name filess.tech;/' /etc/nginx/sites-available/default
sudo sed -i 's/server_name filess.tech;/&\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
sudo service nginx restart
