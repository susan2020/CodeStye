from xml.dom.minidom import parse
import xml.dom.minidom
import re
import os

from test.test_importlib.extension.util import FILEPATH

class CChangCodeStye():
  #file content 
  strCode = ""
  def __init__(self,CChangCode,CParseStye):
    pass
  def run(self):
    pass
  def readfile(self,filePath):
    try:
      fd = open(filePath, "r+")
      self.strCode = fd.readlines()
    except IOError:
      print("")
    else:
      fd.close()
    
  def findfile(self,directPath):
    for root, dirs, files in os.walk( directPath ):
      for fn in files:
        print (root +"/"+fn)
        
  def writefile(self,filePath):
    try:
      fd = open(filePath, "w")
      fd.writelines(self.strCode)
    except IOError:
      print ("")
    else:
      fd.close()
  

class CChangCode():
  def __init__(self):
    pass
  #use reg to find
  def insert_space_between_empty_brackets(self,strCode):
    pass
  
    
  
#Input parameters for the folder path
class CParseStye():
  dirPath = ''
  dict = {}
  strStye = ''
  def __init__(self,dirPath):
    self.dirPath = dirPath
  def run(self):
    self.ParseDoc()

  def addWord(self,key,value): 
    self.dict.setdefault(key, [ ]).append(value)

  def ParseDoc(self):
    DOMTree = xml.dom.minidom.parse(self.dirPath)
    DocStype = DOMTree.documentElement
    profile = DocStype.getElementsByTagName("profile")
    for profileNode in profile:
      self.strStye = profileNode.getAttribute("name")
      setes = profileNode.getElementsByTagName("setting")
      for seting in setes:
        id = seting.getAttribute("id")
        value = seting.getAttribute("value")
        self.addWord(id,value)
        
  def ShowDict(self):
    print("Stype:%s"% self.strStye )
    #print("Value : %s"%  self.dict.items() )
    i = len(self.dict)
    print("Value : %s"% i  )
    while i > 0:
      i = i - 1;
      print(self.dict.popitem())
      



cParseStye = CParseStye("eclipse-cpp-google-style.xml")
cParseStye.run()
cParseStye.ShowDict()



