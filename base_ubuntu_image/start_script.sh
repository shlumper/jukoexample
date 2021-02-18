#!/bin/bash

source ~/.bashrc
retries=1
max_retries=10
# this code implemented since bitbucket close connections when to many clones running in parallel
>&2 echo "-- trying to clone repo [$retries..$max_retries]"
git clone --branch $1 $4

cd $2
echo ""
echo "------------- std --------------"
bash -c "$3"
rt="$(echo $?)"
echo ""
echo "--------------------------------"
printf "exit code $rt"
exit $rt