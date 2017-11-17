#!/bin/bash

#rm -rf output5

hdfs dfs -rm -r /user/s1579769/data/output5

hadoop jar /opt/hadoop/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-input /user/s1579769/data/output2/part-00000 \
-output /user/s1579769/data/output5 \
-mapper task4mapper.py \
-file task4mapper.py \
-combiner task4reducer.py \
-file task4reducer.py \
-reducer task4reducer.py \
-file task4reducer.py \
-jobconf mapred.job.name="Ozs Job 5"

#mkdir output5

#hdfs dfs -copyToLocal /user/s1579769/data/output5/part-00000 output5/part-00000

# delete output folders(both local and hadoop) so that sh can run always
# haddop jar command -file (will automatically upload to hdfs from the location this sheel is being run)
# go to hadoop output and copy it to local output
