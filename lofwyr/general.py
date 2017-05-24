#!/usr/bin/python

import re
import lofwyr.report

ruleset = []
ruleset.append( ("RSA Private Key in Commit", re.compile("BEGIN RSA PRIVATE KEY",re.MULTILINE),True) )
ruleset.append( ("Password in Commit", re.compile("Password:", re.MULTILINE),True) )
ruleset.append( ("Non-Critical AWS Token in Commit", re.compile("AKIA", re.MULTILINE),False) )

class ScanEngine:
  def __init__(self):
    print " [>] general scan engine initializing"
    self.amazon_key = re.compile("")
    pass

  # slow as balls
  def getLine(self,data,match):
    line = 0
    for i in range(0,match):
      if data[i] == '\n':
        line += 1
    return line

  def scan(self,data):
    findings = []
    for (ruletext, rule,criticality) in ruleset:
      lenrules = len(rule.findall(data))
      result = rule.search(data)
      if result is not None:
        for i in range(0,lenrules):
          lineno = self.getLine(data,result.start(i))
          linetxt = ruletext + " in line %d" % lineno
          findings.append(lofwyr.report.Finding(linetxt,critical=criticality))
    return findings
