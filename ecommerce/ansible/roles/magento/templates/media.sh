#!/bin/bash

cont=media
root=/srv/magento/$cont

inotifywait -mr --timefmt '%d/%m/%y %H:%M' --format '%T %w %f' -e close_write $root | while read date time dir file; do
  rdir=${dir#$root}
  cmd="turbolift -u {{ username }} -a {{ api_key }} --os-rax-auth {{ rs_region | lower }} upload -c $cont -s $dir$file -d ${rdir:1:-1}"
  echo "$cmd"
  eval $cmd
done
