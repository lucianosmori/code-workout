#!/bin/bash

NUMBER=6
TWO=6
THREE=7

if [[ $NUMBER == $TWO && $NUMBER == $THREE && $NUMBER == $THREE ]]; then
    echo "EQUILATERAL"

elif [[ $NUMBER == $TWO || $NUMBER == $THREE || $TWO == $THREE ]]; then
    echo "ISOSCELES"

elif [[ $NUMBER != $TWO && $NUMBER != $THREE && $TWO != $THREE ]]; then
    echo "SCALENE"

fi

