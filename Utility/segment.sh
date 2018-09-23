ffmpeg -i $1 -c copy -map 0 -segment_time 5 -g 15 -sc_threshold 0 -force_key_frames "expr:gte(t,n_forced*4)" -f segment -reset_timestamps 1 -segment_list out.csv in%d.webm
