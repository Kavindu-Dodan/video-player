#!/bin/sh

for i in {0..COUNT}
do
    ffmpeg -i in$i.mp4 -crf 4 -b:v 10M -b:a 10M -c:v libx264 -c:a aac -movflags frag_keyframe+empty_moov+default_base_moof NAME$i.mp4
done
