#!/usr/bin/env bash

set -e
IFS=$'\n'

for page_dir in $(ls | grep 'part');
do
    cd ${page_dir}
    for ipnb in $(ls | grep .ipynb); do
        echo ${ipnb}
        jupyter nbconvert ${ipnb} --to slides --SlidesExporter.reveal_scroll=True --SlidesExporter.reveal_transition=none --stdout > ./slides_${ipnb}.html
        jupyter nbconvert ${ipnb} --to html --stdout > ./page_${ipnb}.html
    done
    mv *.html ../docs
    if [ -d ./img ];then
        cp ./img/* ../docs/img
    fi
    cd ..
done