sudo docker network create sphere
sudo docker run --name sphere-mysql --network sphere -v /opt/sphere-data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=sphere_secret -d mysql/mysql-server
sudo docker run --network sphere --name sphere-gunicorn -p 2000:5000 -d sphere2017
