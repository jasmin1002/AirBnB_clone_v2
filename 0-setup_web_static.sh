#!/usr/bin/env bash
# Web Servers Setup.

[ ! -d /etc/nginx ] && sudo apt-get update && sudo apt-get -y install nginx
[ -d /data ] || mkdir -p /data/web_static/shared /data/web_static/releases/test/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
#[ -e /data/web_static/current ] && rm /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
printf %s "server {
	listen 80;
	listen [::]:80;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name filess.tech;

	location / {
		try_files \$uri \$uri/ =404;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4\ permanent;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
	}

	error_page 404 /custom_404.html;
	location = /custom_404.html {
		root /usr/share/nginx/html;
		internal;
	}
}" > /etc/nginx/sites-available/default
#sudo sed -i 's/server_name _;/server_name filess.tech;/' /etc/nginx/sites-available/default
#sudo sed -i 's.\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}..' /etc/nginx/sites-available/default
#sudo sed -i 's/server_name filess.tech;/&\n\n\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}/' /etc/nginx/sites-available/default
sudo service nginx restart
