#!/bin/bash

xrandr -s 0
echo "set laptop"
sleep 5s

xrandr --output VGA-1 --mode 1440x900 --left-of LVDS-1
echo "set outside screen"
