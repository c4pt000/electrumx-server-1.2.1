#!/bin/bash

#change pass:xxxx to unique phrase... 

 openssl genrsa -des3 -passout pass:xxxx -out server.pass.key 2048
 openssl rsa -passin pass:xxxx -in server.pass.key -out server.key
 openssl req -new -key server.key -out server.csr
 rm server.pass.key

openssl x509 -req -days 1825 -in server.csr -signkey server.key -out server.crt

cp -rf server.* /etc/
