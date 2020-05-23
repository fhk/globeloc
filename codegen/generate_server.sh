cd ../api
ln -s ../globeloc/server_impl/
cd ../codegen
java -jar swagger-codegen-cli.jar generate  \
-i ../swagger.json \
-l python-flask \
-o ../api
cd ../api/
python3 -m swagger_server
