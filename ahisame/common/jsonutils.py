#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
JSON Operation Utilities.

'''

import sys
import json
import codecs
import traceback


def read(filename, charset='utf_8', traceback_file=sys.stderr):
  '''
  Try to read json file and convert to python's dict structure.
  Return dict if successed.
  Return None if any error has caused.
  
  '''
  try:
    with codecs.open(filename, 'r', charset) as jsonfile:
      return json.load(jsonfile)
  except:
    traceback.print_exc(sys.exc_info()[0], file=traceback_file)
    return None


def str_to_dict(rawjsonstr):
  '''
  Simple wrapper of json.loads
  
  '''
  return json.loads(rawjsonstr)

