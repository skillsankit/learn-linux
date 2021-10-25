#!/usr/bin/bash

for i in `seq -w 1 50`
do
  touch `date +%Y%m%d`-$i.txt
done
