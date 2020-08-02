#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request
from datetime import datetime
import json
import subprocess
from flask_misaka import markdown
from config import LOGFILE, enabled_cmd
app = Flask(__name__)

show_cmd = """
cmd: 

```bash
%s

```
"""

result = """

result: 

```
$s
```
"""

@app.route('/<string:cmd>', methods=['GET', 'POST'])
def flcmd(cmd):
    if cmd == 'all' or cmd == '':
        return 'Cmds: \n' + '; '.join(enabled_cmd)
    if cmd not in enabled_cmd:
        return "Not a valid command: "+cmd, 403
    if request.method == 'GET':
        with open('cmds/%s.sh'%cmd, 'r') as f:
            pagemd = show_cmd % f.read()
        output = subprocess.run(["./cmds/%s.sh" %cmd], 
                                stderr=subprocess.STDOUT, 
                                stdout=subprocess.PIPE, 
                                text=True)
        pagemd += result % output
        return markdown(pagemd, fenced_code=True)
    if request.method == 'POST':
        pass
        
# vim: ts=4 sw=4 sts=4 expandtab
