import os

triggers = open('triggers.txt').readlines()

for trigger in triggers:
  trigger = trigger.strip('\n')

  trigger = trigger.replace("#","")

  lines = open('log_'+trigger+'.log').readlines()

#Sum delivered : 2.921
#Sum recorded : 2.605

  for i in range(0,len(lines)):
    j = len(lines)-1-i

    if "Sum recorded" in lines[j]:
      lumi = lines[j].split()[3]
      print trigger+'\t'+lumi
      break
