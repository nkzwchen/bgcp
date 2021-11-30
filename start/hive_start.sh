echo "hadoop"|sudo -S service mysqld start
schematool -initSchema -dbType mysql -verbose
hive --service metastore &
