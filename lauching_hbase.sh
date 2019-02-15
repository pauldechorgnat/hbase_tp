#!/usr/bin/env bash

export HBASE_HOME=/home/hduser/hbase

echo "launching HBase"
${HBASE_HOME}/bin/start-hbase.sh

echo "launching Thrift server"
${HBASE_HOME}/bin/hbase-daemon.sh start thrift -p 9090 -b localhost

echo "running processes:"
jps | sort -k 2