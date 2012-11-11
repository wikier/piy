#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import yaml
from huTools.structured import dict2et 
from xml.etree import ElementTree
from xml.dom import minidom

def __preprocess_attributes(node):
    if type(node) == dict:
        node2 = {}
        for k, v in node.items():
            if str(k).startswith("_"):
                k = "@" + str(k)[1:]
            node2[k] = __preprocess_attributes(v) 
        return node2
    else:
        return node

def transform_pom_yaml_to_xml(path=None, fileName="pom.yaml", modelVersion="4.0.0", indent="    ", encoding="utf-8"):
    if path == None:
        path = os.getcwd()
    path = path + os.sep + fileName 
    try:
        with open(path, "r") as f:
            content = f.read()
    except IOError:
        sys.exit("POM not fount at '%s'" % path)
    pom = yaml.load(content)
    if not "project" in pom:
        sys.exit("'project' root node not found")
    else:
        pom = __preprocess_attributes(pom)
        if not "modelVersion" in pom["project"]:
            pom["project"]["modelVersion"] = modelVersion
        elif not pom["project"]["modelVersion"] == modelVersion:
            sys.exit("Unsupported modelVersion " + pom["project"]["modelVersion"])
        pom["project"]["@xmlns"] = "http://maven.apache.org/POM/%s" % modelVersion
        pom["project"]["@xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        pom["project"]["@xsi:schemaLocation"] = "http://maven.apache.org/POM/%s http://maven.apache.org/maven-v%s.xsd" % (modelVersion, modelVersion.replace(".", "_"))
        xml = dict2et(pom)
        dom = minidom.parseString(ElementTree.tostring(xml[0], encoding))
        print dom.toprettyxml(indent)

if __name__ == "__main__":
    transform_pom_yaml_to_xml()

