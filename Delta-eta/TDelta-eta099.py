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
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          #pt = T_sum.Eta()
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)
  h1.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Scale(0.001245*139*2400000/200000)
  h1.SetLineColor(1)




def read_lhe2(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          #pt = T_sum.Eta()
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)

  h2.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h2.Fill(pt)
  h2.Scale(0.005023*139*666666/200000)
  h2.SetLineColor(2)





def read_lhe3(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      cc = 1
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)

  h3.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h3.Fill(pt)
  h3.Scale(10.98*139*900/200000)
  h3.SetLineColor(3)






def read_lhe4(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          #pt = T_sum.Eta()
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)

  h4.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h4.Fill(pt)
  h4.Scale(2808*139*24/200000)
  h4.SetLineColor(4)






def read_lhe5(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          #pt = T_sum.Eta()
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)

  h5.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h5.Fill(pt)
  h5.Scale(0.002852*139*8570000/50000)
  h5.SetLineColor(7)







def read_lhe6(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      #T_sum = R.TLorentzVector()
      jnum = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      pt = 0
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
                  pt += (-1)**jnum*T[Tnum].Eta()
                  Tnum += 1
                  jnum += 1  
      if jnum == 2:
          #pt = T_sum.Eta()
          data.append(abs(pt)) 
          if abs(pt) > ptmax_middle:
              ptmax = abs(pt)
              ptmax_middle = ptmax
          if abs(pt) < ptmin_middle:
              ptmin = abs(pt)
              ptmin_middle = ptmin
          enum += 1
 

  print (enum)
  h6.SetTitle("Delta-eta;Delta-eta;Yield")
  for i, pt in enumerate(data):
    h6.Fill(pt)
  h6.Scale(2702*139/50000)
  h6.SetLineColor(6)




if __name__ == "__main__":
  myC = R.TCanvas("c")
  myC.cd()
  h1 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)
  h2 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)
  h3 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)
  h4 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)
  h5 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)
  h6 = R.TH1F("Delta-eta","Delta-eta", 25, 0, 9)

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

  leg = R.TLegend(0.7,0.7,1,1)
  #leg.SetHeader("pt","C")
  leg.AddEntry(h1,"off-shell derivative","f")
  leg.AddEntry(h2,"off-shell marginal","f")
  leg.AddEntry(h3,"on-shell marginal","f")
  leg.AddEntry(h4,"on-shell derivative","f")
  leg.AddEntry(h5,"z z v v v v","f")
  leg.AddEntry(h6,"z v v","f") 
  leg.Draw()

  myC.SaveAs("TDelta-etaj099.png")
