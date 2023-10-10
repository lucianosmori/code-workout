#!/bin/bash

read NUMBER

LIMIT=6

if ((NUMBER > LIMIT)); then
    echo "$NUMBER is bigger than $LIMIT"

elif ((NUMBER < LIMIT)); then
    echo "$NUMBER is smaller than $LIMIT"

else
    echo "$NUMBER is equal than $LIMIT"
fi