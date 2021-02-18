#!/bin/bash

source ~/.bashrc
retries=1
max_retries=10
# this code implemented since bitbucket close connections when to many clones running in parallel
>&2 echo "-- trying to clone repo [$retries..$max_retries]"
git clone $4

cd cl_cifar10
git config --global user.email devops@deep-aitech.com
git checkout $1
cd $2
echo ""
echo "---------- proc sysout ---------"
bash -c "$3"
rt="$(echo $?)"
echo ""
echo "--------------------------------"
printf "execution exit code $rt"
exit $rt