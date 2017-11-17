#!/bin/bash

#rm -rf output1

hdfs dfs -rm -r /user/s1579769/data/output1

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /data/assignments/ex1/webSmall.txt \
-output /user/s1579769/data/s1579769_task1.out \
-mapper task1mapper.py \
-file task1mapper.py \
-reducer task1reducer.py \
-file task1reducer.py \
-jobconf mapred.reduce.tasks=5


hdfs dfs -rm /user/s1579769/data/output1/_SUCCESS

hdfs dfs -mkdir /user/s1579769/data/output1merged

hdfs dfs -getmerge -nl  /user/s1579769/data/output1 /user/s1579769/data/output1merged/mergedfile



#mkdir output1

#hdfs dfs -copyToLocal /user/s1579769/data/output1/part-00000 output1/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
