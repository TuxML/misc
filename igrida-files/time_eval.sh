#!/bin/bash

cd /TuxML/linux-4.15
cp $1 ./.config

RES=$(echo -n "Compiling with $1; nproc=")
RES="$RES$(nproc) "
TIMEFORMAT='USERTIME %U SYSTEMTIME %S ELAPSEDTIME %R'
RES="$RES$({ time make -j$(nproc) 2>/dev/null 1>/dev/null;} 2>&1) "
RES="$RES$(echo -n 'vmlinux size : ')"
RES="$RES$(ls -l vmlinux | awk '{print $5}')"
echo $RES >> /TuxML/mydir/$2
