#!/bin/bash

#rm -rf output9

hdfs dfs -rm -r /user/s1579769/data/output9

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /data/assignments/ex1/uniSmall.txt \
-output /user/s1579769/data/output9 \
-mapper task9mapper.py \
-file task9mapper.py \
-reducer task9reducer.py \
-file task9reducer.py \
-jobconf mapred.job.name="Ozs Job 9" \
-jobconf mapred.reduce.tasks=3

#-jobconf mapred.reduce.tasks=3

#mkdir output9

#hdfs dfs -copyToLocal /user/s1579769/data/output9/part-00000 output9/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
