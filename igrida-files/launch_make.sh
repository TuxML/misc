#!/bin/bash

INPUT="/mnt/temp_dd/igrida-fs1/psaffray/input_files/"
INPUT2="$INPUT/configs/"
CMD="docker run --mount \
type=bind,source=$INPUT,target=/TuxML/mydir \
tuxml/tuxml:dev-v4.15 /TuxML/mydir/time_eval.sh /TuxML/mydir/configs/"
temp=$CMD
for file in $INPUT2*; do
        temp="$CMD${file##*/} results_$1.txt"
        eval $temp
done
