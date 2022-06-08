 #!/usr/bin/env python

import subprocess
#subprocess.call("source /users/wuxingyu/root/bin/thisroot.sh",shell=True)

import sys, os
sys.path.append("/home/greenhand/download/MG5_aMC_v3_3_2/")
from madgraph.various.lhe_parser import *
import ROOT as R
R.gROOT.SetStyle("ATLAS")

def read_lhe(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      for particle in event:
          if particle.status == 1:
              if particle.pid == 1 or particle.pid == 2 or particle.pid == 3 or particle.pid == 4 or particle.pid == 5 or particle.pid == 6 or particle.pid == -1 or particle.pid == -2 or particle.pid == -3 or particle.pid == -4 or particle.pid == -5 or particle.pid == -6 or particle.pid == 21:
                  T.append(R.TLorentzVector())
                  p = FourMomentum(particle)
                  px = p.px
                  py = p.py
                  pz = p.pz
                  E = p.E 
                  T[Tnum].SetPxPyPzE(px,py,pz,E)
                  T_sum += T[Tnum]
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          pt = T_sum.M()
          data.append(pt) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1


  print (enum)

  myC = R.TCanvas("c")
  myC.cd()  


  hname = "imass"
  #nbins, xmin, xmax = 100, ptmin, ptmax
  h1 = R.TH1F(hname, hname, 100, ptmin, ptmax)
  h1.SetTitle("imass;imass/GeV;fraction")
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Scale(2702*139/50000)
  h1.Draw()
  
  leg = R.TLegend(0.6,0.7,0.9,0.9)
  leg.SetHeader("imass","C")
  leg.AddEntry(h1,"BKG1","f")
  leg.Draw()

  myC.SaveAs("imassj1.png")

  #tfout = R.TFile("pt.root", "RECREATE")
  #tfout.cd()
  #h1.Write()
  #tfout.Close()


if __name__ == "__main__":

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/zvv/Events/run_02/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)
