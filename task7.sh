#!/bin/bash

#rm -rf output7

hdfs dfs -rm -r /user/s1579769/data/output7

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /data/assignments/ex1/matrixSmall.txt \
-output /user/s1579769/data/output7 \
-mapper task7mapper.py \
-file task7mapper.py \
-reducer task7reducer.py \
-file task7reducer.py \
-jobconf mapred.job.name="Ozs Job 7"

#mkdir output7

#hdfs dfs -copyToLocal /user/s1579769/data/output7/part-00000 output7/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
