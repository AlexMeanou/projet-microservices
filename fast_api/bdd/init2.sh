wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-debian92-x86_64-100.3.1.deb
sudo apt install ./mongodb-database-tools-*.deb 
rm -f mongodb-database-tools-*.deb
python mongo-init.py