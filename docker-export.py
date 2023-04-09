#!/usr/bin/env python3
import sys
import json
from dockerfile_parse import DockerfileParser #pip3 install -U dockerfile_parse

comment='#'
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} path/to/Dockerfile")
    sys.exit(1)
elif len(sys.argv) > 2:
    comment = sys.argv[2]

dfp = DockerfileParser()
with open(sys.argv[1], 'r') as file:
    dfp.content = file.read()

dfp.structure[1]["content"];
js = json.loads(dfp.json)
for e in js:
  for k, v in e.items():
    if k == 'RUN':
      print(v, '\n')
    elif k == 'COMMENT':
      print(comment, v)
    elif k == 'ENV':
      print('export', v)
    else:
      print(comment, k, v)
