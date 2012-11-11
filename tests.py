#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
from piy import transform_pom_yaml_to_xml

if __name__ == "__main__":
    root = os.getcwd() + os.sep + "tests"
    tests = [ name for name in os.listdir(root) if os.path.isdir(os.path.join(root, name)) ]
    tests.sort()
    sys.path.append(os.getcwd())
    for test in tests:
        path = root + os.sep + test
        print
        print "Running tests with file '%s/pom.yaml'" % path
        print "---------------------------------------------------------------------"
        transform_pom_yaml_to_xml(path=path)
        print

