#!/bin/bash

echo "enter name:"
read NAME

for VARIABLE in {1..10}

do
    echo "hello $NAME $VARIABLE times"
done