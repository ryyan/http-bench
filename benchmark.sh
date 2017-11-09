#!/bin/bash

# Source directory path
SOURCE=$(dirname $(readlink -f $0))

# Run script path
RUN=$SOURCE/run.sh

# Results output file
RESULTS=$SOURCE/RESULTS.md
touch $RESULTS
> $RESULTS # Clear file

cd $SOURCE/servers
for d in $(ls -dR */**); do
  $RUN build $d
  $RUN start $d
  $RUN benchmark | tee -a $RESULTS
  $RUN stop $d
  $RUN clean $d
done
