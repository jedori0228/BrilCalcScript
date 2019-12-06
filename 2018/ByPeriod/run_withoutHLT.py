import os

cmd = 'brilcalc lumi -u /pb --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/ReReco/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt '

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


for i in range(0,len(Period_Starts)):
  this_cmd = cmd+' --begin '+str( Period_Starts[i] )+' --end '+str( Period_Ends[i] )+' &> log_period'+Periods[i]+'_'+str(Period_Starts[i])+'_'+str(Period_Ends[i])+'.log'
  print this_cmd
  os.system(this_cmd)
