import os

cmd = 'brilcalc lumi -u /pb --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt '

Periods = [
"B",
"C",
"D",
"E",
"F",
]

Period_Starts = [
297046,
299368,
302030,
303824,
305040,
]

Period_Ends = [
299329,
302029,
303434,
304797,
306462,
]


for i in range(0,len(Period_Starts)):
  this_cmd = cmd+' --begin '+str( Period_Starts[i] )+' --end '+str( Period_Ends[i] )+' &> log_period'+Periods[i]+'_'+str(Period_Starts[i])+'_'+str(Period_Ends[i])+'.log'
  print this_cmd
  os.system(this_cmd)
