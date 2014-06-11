#!/usr/bin/env python
# 2014-06-11 17:09:49Z pingliangchenisthebest@gmail.com
# Copyright (c) 2009, PinLiang Chen'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys
import os
import time
import datetime

from datetime import datetime
from daemon import runner
from collections import defaultdict
from collections import Counter
from time import gmtime, strftime
from datetime import datetime, timedelta

Path = "/home/PinLiang/"
ErrorPath = "/home/pinliang/error.log"
Apachecmd = "service apache2 restart"
Tomcatcmd = "service tomcat7 restart"
Activemqcmd = "service activemq restart"

if not os.path.exists(Path):
	os.makedirs(Path)
file = open(Path+"Data", "w")
file.write("abc")
file.close()

def AJPFaile():
	file = open(ErrorPath, "r")
	lineList = file.readlines()
	file.close()
	
	check = open(Path+"Data", "r")
	checklist = check.readlines()
	check.close()

	if (len(lineList) != 0 and len(lineList) > 2):
		if (checklist[-1] != lineList[-1]):
			if ((" ".join((lineList[-1].split("] ")[2]).split()) == "(70007)The timeout specified has expired: proxy: dialog to (null) (localhost) failed") or (" ".join((lineList[-1].split("] ")[2]).split()) == "(70007)The timeout specified has expired: proxy: dialog to 127.0.0.1:8009 (localhost) failed")):
				if (" ".join((lineList[-2].split("] ")[2]).split()) == "ajp_read_header: ajp_ilink_receive failed"):
					if (" ".join((lineList[-3].split("] ")[2]).split()) == "(70007)The timeout specified has expired: ajp_ilink_receive() can't receive header"):
						os.system("service nginx restart")
						file = open(Path+"Data", "w")
						file.write(lineList[-1])
						file.close()

class App():

    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/var/run/AJP.pid'
        self.pidfile_timeout = 5

    def run(self):
	while True:
            AJPFaile()
            time.sleep(10)

app = App()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
