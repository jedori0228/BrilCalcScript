import os

Periods = [
"A",
"B",
"C",
"D",
]

Period_Starts = [
315252,
317080,
319337,
320673,
]

Period_Ends = [
316995,
319310,
320065,
325175,
]



for k in range(0,len(Period_Starts)):

  lines = open('log_period'+Periods[k]+'_'+str(Period_Starts[k])+'_'+str(Period_Ends[k])+'.log').readlines()

  '''
#Summary: 
+-------+------+-------+-------+-------------------+------------------+
| nfill | nrun | nls   | ncms  | totdelivered(/pb) | totrecorded(/pb) |
+-------+------+-------+-------+-------------------+------------------+
| 34    | 103  | 52721 | 52716 | 5991.078137866    | 5750.490644035   |
+-------+------+-------+-------+-------------------+------------------+
'''

  for i in range(0,len(lines)):
    j = len(lines)-1-i

    if "Summary" in lines[j]:

      lumiline = lines[j+4]
      words = lumiline.split('|')

      print Periods[k]+'\t'+str(Period_Starts[k])+"\t"+str(Period_Ends[k])+'\t'+words[6]
      break
