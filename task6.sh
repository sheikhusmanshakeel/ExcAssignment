#!/bin/bash

#rm -rf output6

hdfs dfs -rm -r /user/s1579769/data/output6

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /data/assignments/ex1/webLarge.txt \
-output /user/s1579769/data/output6 \
-mapper task6mapper.py \
-file task6mapper.py \
-reducer task6reducer.py \
-file task6reducer.py \
-jobconf mapred.job.name="Ozs Job 6"

#mkdir output6

#hdfs dfs -copyToLocal /user/s1579769/data/output6/part-00000 output6/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
