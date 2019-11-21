#!/bin/bash

docker run \
    --rm -it \
    --publish 3306:3306 \
    --env MYSQL_DATABASE='askdjango_db' \
    --env MYSQL_ROOT_PASSWORD='qwer1234' \
    --volume 'pwd'/data_mysql:/var/lib/mysql \
    mysql:5