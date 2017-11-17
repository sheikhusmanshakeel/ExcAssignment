#!/bin/bash

#rm -rf output3

hdfs dfs -rm -r /user/s1579769/data/output3

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /user/s1579769/data/output2/part-00000 \
-output /user/s1579769/data/output3 \
-mapper task3mapper.py \
-file task3mapper.py \
-reducer task3reducer.py \
-file task3reducer.py \
-jobconf mapred.reduce.tasks=1


#mkdir output3

#hdfs dfs -copyToLocal /user/s1579769/data/output3/part-00000 output3/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
