#!/usr/bin/env bash
# 0. Prepare your web servers
sudo apt update && sudo apt install nginx -y
# allow port 80
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sample="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
sudo chown -R ubuntu:ubuntu /data/
echo "$sample" >> /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
  rm -f "/data/web_static/current"
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "/server_name _;/c\ \tserver_name _;\n\tlocation /hbnb_static{\n\t  alias /data/web_static/current/;\n\t  autoindex off;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
