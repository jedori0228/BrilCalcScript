import os

cmd = 'brilcalc lumi -u /pb --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt '

Periods = [
"B_ver2",
"C",
"D",
"E",
"F",
"G",
"H",
]

Period_Starts = [
272007,
275657,
276315,
276831,
277772,
278820,
280919,
]

Period_Ends = [
275376,
276283,
276811,
277420,
278808,
280385,
284044,
]


for i in range(0,len(Period_Starts)):
  this_cmd = cmd+' --begin '+str( Period_Starts[i] )+' --end '+str( Period_Ends[i] )+' &> log_period'+Periods[i]+'_'+str(Period_Starts[i])+'_'+str(Period_Ends[i])+'.log'
  print this_cmd
  os.system(this_cmd)
