#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Please precise a number of jobs: ./oar_script.sh number <tuxml>"
    exit -1
fi

for i in $(seq $1);do
	oarsub -S "./launch_compilations.sh $2" -p "cluster='bermuda' AND virt='YES'"

done
echo "$1 jobs created"
