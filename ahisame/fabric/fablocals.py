#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Fabric Local Utilites.

'''

import sys
import os
import json
import codecs
import traceback

from fabric.api import *
from fabric.contrib.files import exists
from fabric.contrib.project import rsync_project

def contains_regex(filename, regex):
  '''
  Return the file that names *filename* contains line that matches *regex*.
  
  '''
  with quiet():
    result = int(local('grep -c -E "{0}" {1}'.format(regex, filename), capture=True))
    return result > 0


def contains(filename, expression):
  '''
  Return the file that names *filename* contains *expression* line.
  
  '''
  with quiet():
    result = int(local('grep -c -F "{0}" {1}'.format(expression, filename), capture=True))
    return result > 0


def exists(filename):
  '''
  Return the file that names *filename* exists on local computer.
  
  '''
  return os.path.exists(filename)

