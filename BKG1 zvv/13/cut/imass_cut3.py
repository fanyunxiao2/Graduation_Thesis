#!/usr/bin/env python

import subprocess
#subprocess.call("source /users/wuxingyu/root/bin/thisroot.sh",shell=True)

import sys, os
sys.path.append("/home/greenhand/download/MG5_aMC_v3_3_2/")
from madgraph.various.lhe_parser import *
import ROOT as R
#import some modules

def read_lhe(input_file):
  lhe = EventFile(input_file)
  enum = 0
  Tnum = 0
  #define event number and the number of the TLorentzVectors
  data = []
  T = []
  #define a list named data to save the target data and a list named T to save the      TLorentzVectors of two jets
  for event in lhe:
      T_sum = R.TLorentzVector()
      #add the TLorentzVectors of two jets together
      jnum = 0
      #record the number of the jets
      Pt = 0
      cut2 = 0
      #parameters about cut2
      etai = 0
      cut3 = 0
      #parameters about cut3
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      for particle in event:
          if particle.status == 1:
              if particle.pid == 1 or particle.pid == 2 or particle.pid == 3 or particle.pid == 4 or particle.pid == 5 or particle.pid == 6 or particle.pid == -1 or particle.pid == -2 or particle.pid == -3 or particle.pid == -4 or particle.pid == -5 or particle.pid == -6 or particle.pid == 21:
                  #screen out the events if the final state has hadron
                  T.append(R.TLorentzVector())
                  p = FourMomentum(particle)
                  px = p.px
                  py = p.py
                  pz = p.pz
                  E = p.E 
                  T[Tnum].SetPxPyPzE(px,py,pz,E)
                  T_sum += T[Tnum]
                  #add the TLorentzVectors of two jets together
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut3 += 1
                  #cut3
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut2 += 1 
                  #cut2 is related to the pt of two jets 
      if jnum == 2:
      #make sure the final state of this event has two jets
          if T_sum.Et() > 80:
              #cut1
              if cut2 == 2:
                  #cut2
                  if cut3 == 2:
                      #cut3
                      pt = T_sum.M()
                      data.append(pt) 
                      #export the invariant mass and save them to the list named data
                      if abs(pt) > ptmax_middle:
                          ptmax = abs(pt)
                          ptmax_middle = ptmax
                      if abs(pt) < ptmin_middle:
                          ptmin = abs(pt)
                          ptmin_middle = ptmin
                      #find the Max and Min of the invariant mass
                      enum += 1

  #print (enum)
  #if necessary
  myC = R.TCanvas("c")
  myC.cd()  
  hname = "imass"
  h1 = R.TH1F(hname, hname, 100, ptmin, ptmax)
  h1.SetTitle("imass;imass/GeV;fraction")
  #define the histogram
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Scale(2702*139/50000)
  #normalization 
  h1.Draw()
  myC.SaveAs("imass_jj3.png")

if __name__ == "__main__":

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/zvv/Events/run_02/unweighted_events.lhe.gz"
  read_lhe(input_file=input_file)
