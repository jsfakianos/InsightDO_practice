#!/usr/bin/env bash

INI_file=$(pwd)"/../data/inifile.ini"

awk 'BEGIN {
            FS = "=";
            }
     {      if ($0 ~ "\[") {sub(/^ +| +$/, "", $1); array_name = substr($1,2,length($0)-2)}
            else if ($0 ~ "=") {sub(/^ +| +$/, "",$1);  sub(/^ +| +$/, "",$2); array[array_name,$1] = $2}
     }
     END {
            for (key in array) {split(key, sep, SUBSEP); print sep[1], sep[2], array[sep[1], sep[2]]}
     }
     ' $INI_file
     
     
