#!/bin/bash

#rm -rf output8

hdfs dfs -rm -r /user/s1579769/data/output8

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /data/assignments/ex1/uniSmall.txt \
-output /user/s1579769/data/output8 \
-mapper task8mapper.py \
-file task8mapper.py \
-reducer task8reducer.py \
-file task8reducer.py \
-jobconf mapred.job.name="Ozs Job 8" \
-jobconf mapred.reduce.tasks=5

#mkdir output8

#hdfs dfs -copyToLocal /user/s1579769/data/output8/part-00000 output8/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
