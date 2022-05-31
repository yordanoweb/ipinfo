#!/bin/sh

cdir=$(dirname $0)

rofi -location 2 -theme ${cdir}/messages.rasi -e "$(python ${cdir}/ipinfo.py)"
