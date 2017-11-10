#!/bin/bash

ACTION=$1
SERVER=$2

# Verify first param exists (action)
if [ -f $ACTION ]
then
  echo "First parameter required (benchmark|build|start|stop|clean)"
  exit
fi

# If first param is benchmark, run it then exit
if [ $ACTION == "benchmark" ]
then
  docker run --rm --net="host" \
    williamyeh/wrk \
    http://127.0.0.1:8888/api/echo/HelloWorld?num=1234567890
  exit
fi

# If action is test, run it then exit
if [ $ACTION == "test" ]
then
  HAPPY_TEST=$(curl -s localhost:8888/api/echo/HelloWorld?num=1234567890)
  if [[ $HAPPY_TEST == "{\"message\":"* ]]
  then
    printf "HappyTest-PASS, "
  else
    printf "HappyTest-FAIL, "
    printf "$HAPPY_TEST, "
  fi

  ERROR_TEST=$(curl -s localhost:8888/api/echo/GoodbyeWorld?num=321)
  if [[ $ERROR_TEST == "{\"error\":\"Invalid parameters\"}" ]]
  then
    printf "ErrorTest-PASS\n"
  else
    printf "ErrorTest-FAIL, "
    printf "$ERROR_TEST\n"
  fi

  exit
fi

# Verify second param exists (server/directory)
if [ -f $SERVER ]
then
  echo "Second parameter required (ex: go/go)"
  exit
fi

# cd to server directory
SOURCE=$(dirname $(readlink -f $0))
cd $SOURCE/servers/$SERVER

# Docker image name
SUFFIX=${SERVER//\//-} # Convert / to -
NAME=httpbenchserver-$SUFFIX

# Run action
case $ACTION in
  "build")
    docker build --rm -t $NAME .
    ;;
  "start")
    docker kill $NAME
    docker rm --force $NAME
    docker run -it --rm --name=$NAME --net="host" -d $NAME
    ;;
  "stop")
    docker kill $NAME
    docker rm --force $NAME
    ;;
  "clean")
    docker rmi --force $NAME
    ;;
esac
