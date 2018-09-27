import os

lines = open('triggers.txt').readlines()

cmd = 'brilcalc lumi -u /pb --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt --hltpath '

for line in lines:

  if "#" in line:
    continue

  line = line.strip('\n')

  os.system(cmd+line+'* > log_'+line+'.log')
