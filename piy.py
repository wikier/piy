
import sys
import os
import yaml
from huTools.structured import dict2et 
from xml.etree import ElementTree
from xml.dom import minidom

def transform_pom_yaml_to_xml(modelVersion="4.0.0", indent="    ", encoding="utf-8"):
    folder =  os.getcwd()
    with open(folder + "/pom.yaml", "r") as f:
        content = f.read()
    pom = yaml.load(content)
    if not "project" in pom:
        sys.exit("'project' root node not found")
    else:
        if not "modelVersion" in pom["project"]:
            pom["project"]["modelVersion"] = modelVersion
        elif not pom["project"]["modelVersion"] == modelVersion:
            sys.exit("Unsupported modelVersion " + pom["project"]["modelVersion"])
        pom["project"]["@xmlns"] = "http://maven.apache.org/POM/%s" % modelVersion
        pom["project"]["@xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        pom["project"]["@xsi:schemaLocation"] = "http://maven.apache.org/POM/%s http://maven.apache.org/maven-v%s.xsd" % (modelVersion, modelVersion.replace(".", "_"))
        xml = dict2et(pom)
        dom = minidom.parseString(ElementTree.tostring(xml[0], encoding))
        print dom.toprettyxml(indent) #TODO

if __name__ == "__main__":
    transform_pom_yaml_to_xml()

