#!/bin/sh

# current dir
cdir=$(dirname $0)

# rofi theme
rofi_theme=${cdir}/rofi/messages.rasi

# top screen border and centered
rofi_pos=2

# message to show inside rofi box
msg="$(python ${cdir}/py/ipinfo.py)"

rofi -location ${rofi_pos} -theme ${rofi_theme} -e "${msg}"
