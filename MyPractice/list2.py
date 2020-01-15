#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-27 13:48:45
# @Author  : Flack (flackmaster@163.com)
# @Link    : http://www.cnblogs.com/ching126/
# @Version : $Id$

import os

def FindStr(matchFile):
	f = open(matchFile)
	for line in f:
		if line.startswith('username'):
			print(line)
	f.close()

FindStr('test.txt')
