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

Path = "/home/pinLiang/"
ErrorPath = "/home/pinliang/error.log"
#Apachecmd = "service apache2 restart"
#Tomcatcmd = "service tomcat7 restart"
#Activemqcmd = "service activemq restart"
#Nginxcmd = "service nginx restart"
#Activemqcmd2 = "/home/pinliang/ChatChat/apache-activemq-5.8.0/bin/./activemq restart"

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
			if "(70007)" in lineList[-1]:
				#os.system(Activemqcmd2)
				print "Hello World!"
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
