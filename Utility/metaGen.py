import json
import csv
import os

# Utility to generate metadata

csv_data = "out.csv"
out_json = "meta.json"
title = 'cartoon'
format = ".webm"
mime = 'video/webm; codecs="vorbis, vp8"'

quality = ["high", "low"]

print("CSV file : [%s], JSON file : [%s], Video title : [%s], Format : [%s], Mime : [%s]" %  (csv_data, out_json, title, format, mime))

csv_file = os.path.join(os.path.dirname(__file__), csv_data)
json_file = os.path.join(os.path.dirname(__file__), out_json)

meta = {}

meta['title'] = title
meta['mime'] = mime
meta['segments'] = []

with open(csv_file, 'r') as csv_data:
    reader = csv.reader(csv_data, delimiter=',')

    final_length = 0
    index = 0
    for row in reader:
        data = {}
        data['segment'] = title + str(index) + format
        data['start'] = row[1]
        data['end'] = row[2]
        final_length = row[2]

        meta['segments'].append(data)
        index += 1

    meta['length'] = final_length

    meta['quality'] = quality

with open(json_file, 'w') as output:
    output.write(json.dumps(meta))