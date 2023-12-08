#!/bin/bash

padded=$(printf "Day%02d" $1)
mkdir $padded -p
touch $padded/input.txt
touch $padded/README.md
cp template.py $padded/$padded.py -n
