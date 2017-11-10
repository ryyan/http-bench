#!/bin/bash

# Source directory path
SOURCE=$(dirname $(readlink -f $0))

# Run script path
RUN=$SOURCE/run.sh

# Results output file
RESULTS=$SOURCE/RESULTS.md
touch $RESULTS

# Print current date to top of Results
date +"%d %b %G, %R" > $RESULTS
echo '---' >> $RESULTS

# Iterate over subdirectories in /servers and run benchmarks
cd $SOURCE/servers
for d in $(ls -dR */**); do
  $RUN build $d
  $RUN start $d
  sleep 2
  $RUN test | tee -a $RESULTS
  $RUN benchmark | tee -a $RESULTS
  $RUN stop $d
  $RUN clean $d
done
