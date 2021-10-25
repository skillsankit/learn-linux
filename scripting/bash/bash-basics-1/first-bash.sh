#!/usr/bin/bash

# who="Hari Krishna"

# echo -e "Who is working on this script ?? \n${who}!"

# echo -e "Who is working on this script ?? \n$(whoami)!"

# echo 'Who are you ?'

# read who

# echo "Hello, $who !"

# echo "How old are you ??"
# read age
# if [ $age -ge 18 ]
# then
#     echo "You are eleigble to vote"
# else
#     echo "You are not eligible to vote"
# fi


# files=/home/hari-skills/Desktop/Scripting/Bash/*

# for file in $files
#     do
#         echo $(basename $file)
#     done

beatles=('John' 'Paul' 'George' 'Ringo')

echo ${beatles[1]}