hdfs dfs -put customer_feedback_satisfaction.csv /input
hadoop jar /home/student/Downloads/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar \
    -input /input \
    -output /output \
    -mapper "python3 mapper.py" \
    -combiner "python3 combiner.py" \
    -reducer "python3 reducer.py"
hdfs dfs -cat /output/part-00000 > reducer_output.csv
python3 validate_statistics.py
