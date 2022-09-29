#!/usr/bin/env bash
# Web Servers Setup.

[ ! -d /etc/nginx ] && sudo apt update && sudo apt -y install nginx
[ -d /data ] || mkdir -p /data/web_static/releases /data/web_static/shared
sudo echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
[ -e /data/web_static/current ] && rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sudo service nginx restart
