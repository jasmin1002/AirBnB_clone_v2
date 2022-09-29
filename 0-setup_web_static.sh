#!/usr/bin/env bash
# Web Servers Setup.

[ -d /data ] || mkdir /data/
[ -d /data/web_static/ ] || mkdir -p /data/web_static/
[ -d /data/web_static/releases/ ] || mkdir -p /data/web_static/releases/
[ -d /data/web_static/shared/ ] || mkdir -p /data/web_static/shared/
[ -d /data/web_static/releases/test/ ] || mkdir -p /data/web_static/releases/test/
[ -e /data/web_static/releases/test/index.html ] || touch /data/web_static/releases/test/index.html
sed -i "$ i <html>\\\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" /data/web_static/releases/test/index.html
[ -e /data/web_static/current ] && rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
