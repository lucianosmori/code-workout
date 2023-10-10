#!/bin/bash

#read NAME

NAME=6

LIMIT=5

if ((NAME > LIMIT)); then

    echo "$NAME is bigger than $LIMIT"
fi

read NUMBER

# if [[ $NUMBER == "y" || $NUMBER == "Y" ]]; then
#     echo "YES"

# elif [[ $NUMBER == "n" || $NUMBER == "N" ]]; then
#     echo "NO"

# fi

