#!/bin/bash

INPUT="/mnt/temp_dd/igrida-fs1/psaffray/input_files/configs/"
CMD="/root/kernel_generator.py --local --dev --linux4_version 15 --config $INPUT"
temp=$CMD
for file in $INPUT*; do
  temp="$CMD${file##*/}"
  eval $temp
done

