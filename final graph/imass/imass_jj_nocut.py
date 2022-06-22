 #!/usr/bin/env python

import subprocess
#subprocess.call("source /users/wuxingyu/root/bin/thisroot.sh",shell=True)

import sys, os
sys.path.append("/home/greenhand/download/MG5_aMC_v3_3_2/")
from madgraph.various.lhe_parser import *
import ROOT as R
#R.gROOT.SetStyle("ATLAS")

def read_lhe1(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h1.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Scale(0.001245*139*3800000/200000)
  h1.SetLineColor(1)

def read_lhe2(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h2.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h2.Fill(pt)
  h2.Scale(0.005023*139*666000/200000)
  h2.SetLineColor(2)

def read_lhe3(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h3.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h3.Fill(pt)
  h3.Scale(10.98*139*750/200000)
  h3.SetLineColor(3)


def read_lhe4(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h4.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h4.Fill(pt)
  h4.Scale(2808*139*10/200000)
  h4.SetLineColor(4)


def read_lhe5(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h5.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h5.Fill(pt)
  h5.Scale(0.002852*139*5000000/50000)
  h5.SetLineColor(7)

def read_lhe6(input_file):
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
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
      #make sure the final state of this event has two jets
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
  h6.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h6.Fill(pt)
  h6.Scale(2702*139/50000)
  h6.SetLineColor(6)



if __name__ == "__main__":
  myC = R.TCanvas("c")
  myC.cd()
  h1 = R.TH1F("imass","imass", 25, 0, 3500)
  h2 = R.TH1F("imass","imass", 25, 0, 3500)
  h3 = R.TH1F("imass","imass", 25, 0, 3500)
  h4 = R.TH1F("imass","imass", 25, 0, 3500)
  h5 = R.TH1F("imass","imass", 25, 0, 3500)
  h6 = R.TH1F("imass","imass", 25, 0, 3500)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/h4/Events/run_01/unweighted_events.lhe.gz"
  read_lhe1(input_file=input_file)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/h4/Events/run_02/unweighted_events.lhe.gz"
  read_lhe2(input_file=input_file)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/h4/Events/run_03/unweighted_events.lhe.gz"
  read_lhe3(input_file=input_file)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/h4/Events/run_04/unweighted_events.lhe.gz"
  read_lhe4(input_file=input_file)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/jjvvvv/Events/run_02/unweighted_events.lhe.gz"
  read_lhe5(input_file=input_file)

  input_file="/home/greenhand/download/MG5_aMC_v3_3_2/bin/zvv/Events/run_02/unweighted_events.lhe.gz"
  read_lhe6(input_file=input_file)

  h1.Draw("E")
  h2.Draw("Esame")
  h3.Draw("Esame")
  h4.Draw("Esame")
  h5.Draw("Esame")
  h6.Draw("Esame")
  #Draw the histograms together
  leg = R.TLegend(0.5,0.6,0.9,0.9)
  leg.AddEntry(h1,"off-shell derivative","f")
  leg.AddEntry(h2,"off-shell marginal","f")
  leg.AddEntry(h3,"on-shell marginal","f")
  leg.AddEntry(h4,"on-shell derivative","f")
  leg.AddEntry(h5,"z z v v v v","f")
  leg.AddEntry(h6,"z v v","f") 
  leg.Draw()

  myC.SaveAs("imassall_jj_nocut.png")
