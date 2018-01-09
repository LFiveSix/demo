#! /bin/sh

cd /www/mcld/
git stash
git pull

cd /etc/supervisor/
supervisorctl restart all
