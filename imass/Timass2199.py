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
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      Pt = 0
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum == 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
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

  #hname = "imass"
  #nbins, xmin, xmax = 100, ptmin, ptmax
  h1.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h1.Fill(pt)
  h1.Scale(0.001245*139*500000*0.7/200000)
  h1.SetLineColor(1)

def read_lhe2(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      Pt = 0
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum == 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
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

  #hname = "imass"
  #nbins, xmin, xmax = 100, ptmin, ptmax
  
  h2.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h2.Fill(pt)
  h2.Scale(0.005023*139*100000*0.7/200000)
  h2.SetLineColor(2)

def read_lhe3(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      Pt = 0
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum == 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
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

  h3.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h3.Fill(pt)
  h3.Scale(10.98*139*170*0.7/200000)
  h3.SetLineColor(3)


def read_lhe4(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      Pt = 0
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum == 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
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

  h4.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h4.Fill(pt)
  h4.Scale(2808*139*6*0.35/200000)
  h4.SetLineColor(4)


def read_lhe5(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      lnum = 0
      Pt = 0
      ptmax = 0
      ptmin = 10000000
      ptmax_middle = 0
      ptmin_middle = 0
      #for particle in event: 
          #if particle.pid == 11 or particle.pid == 12 or particle.pid == 13 or particle.pid == 14 or particle.pid == 15 or particle.pid == 16 or particle.pid == 17 or particle.pid == 18:
              #lnum += 1
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum >= 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
                              if lnum == 0:
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

  h5.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h5.Fill(pt)
  h5.Scale(0.002852*139*875000/50000)
  h5.SetLineColor(7)

def read_lhe6(input_file):
  lhe = EventFile(input_file)

  enum = 0
  Tnum = 0
  data = []
  T = []
  #T_sum = R.TLorentzVector()
  for event in lhe:
      T_sum = R.TLorentzVector()
      cut1 = 0
      cut2 = 0
      cut3 = 0
      cut31 = 0
      cut4 =0
      cc = 1
      DPhi1 = 0
      etai = 0
      jnum = 0
      Pt = 0
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
                  cut3 += T[Tnum].Eta()
                  cut31 += abs(T[Tnum].Eta())
                  etai = T[Tnum].Eta()
                  if abs(etai) < 4.7:
                      cut2 += 1
                  #if T_sum.DeltaPhi(T[Tnum]) < 2.2:
                      #cut4 += 1
                  DPhi1 += (-1)**cc*T[Tnum].Phi()
                  cc += 1
                  Tnum += 1
                  jnum += 1 
                  pt_square = p.pt2
                  Pt = math.sqrt(pt_square)
                  if Pt > 50:
                      cut1 += 1 
      if jnum >= 2:
          if T_sum.Et() > 80: 
              if cut1 == 2:
                  if cut2 == 2:
                      if abs(cut3) < cut31:
                          if abs(DPhi1) < 2.2:
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


  h6.SetTitle("imass;imass/GeV;Yield")
  for i, pt in enumerate(data):
    h6.Fill(pt)
  h6.Scale(2702*139/50000)
  h6.SetLineColor(6)




if __name__ == "__main__":
  myC = R.TCanvas("c")
  myC.cd()
  #THStack sum_h("hs","hss")
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

  leg = R.TLegend(0.5,0.6,0.9,0.9)
  #leg.SetHeader("pt","C")
  leg.AddEntry(h1,"off-shell derivative","f")
  leg.AddEntry(h2,"off-shell marginal","f")
  leg.AddEntry(h3,"on-shell marginal","f")
  leg.AddEntry(h4,"on-shell derivative","f")
  leg.AddEntry(h5,"z z v v v v","f")
  leg.AddEntry(h6,"z v v","f") 
  leg.Draw()

  myC.SaveAs("Timassj2199.png")
