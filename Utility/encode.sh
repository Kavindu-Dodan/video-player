#!/bin/sh

for i in {0..COUNT}
do
    ffmpeg -i in$i.webm -crf 4 -b:v 10M -c:v libvpx -c:a libvorbis bunny$i.webm 
done
