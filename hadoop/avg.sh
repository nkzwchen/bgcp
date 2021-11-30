javac -classpath ${HADOOP_HOME}/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.0.jar -classpath ${HADOOP_HOME}/share/hadoop/client/hadoop-client-api-3.3.0.jar hadoop/Avg.java
jar -cf Avg.jar hadoop
hadoop jar Avg.jar hadoop.Avg  /data /output
