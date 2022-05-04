#!/bin/sh -l

echo "$1"
time=$(date)
echo "::set-output name=time::$time"
