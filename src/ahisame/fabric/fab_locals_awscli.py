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

from ahisame.common import jsonutils

def run(awscli_command):
  with quiet():
    rawjson = local(awscli_command, capture=True)
    return jsonutils.str_to_dict(rawjson)

