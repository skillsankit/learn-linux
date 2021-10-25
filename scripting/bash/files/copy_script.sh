#!/usr/bin/bash

files="/home/hari-skills/Desktop/Scripting/Bash/files"

for file in $(ls /home/hari-skills/Desktop/Scripting/Bash/files/)
  do
    #mv ${file} /home/hari-skills/Desktop/Scripting/Bash/files_copy/
    echo "completed copying file ${file}"
    #sleep 5s
done
