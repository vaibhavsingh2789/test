#!/bin/bash
#to find occurrence of 404 error code
a=0
for l in `cut -f 10 -d ' ' log`
do 
if [ $l = '404' ]
then
a=$(($a+1))
fi
done 
echo "occurrence of 404:"$a

#number of occurence of each error code
declare -A errcode
for l in `cut -f 10 -d ' ' log`
do
errcode[$l]=0
done
for K in `cut -f 10 -d ' ' log`
do errcode[$K]=$((${errcode[$K]}+1))
done
for K in "${!errcode[@]}"
do
echo "occurrence of "$K":"${errcode[$K]}
done
