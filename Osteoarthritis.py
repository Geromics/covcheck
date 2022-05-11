## TODO: Scores should be LOD risk ratios I think...
import pathlib
import json
import os
import pandas as pd
class Osteo:

  def __init__(self):
    pass

  def read_json_osteo(self):

  #  filename = pathlib.Path(path).name
    #print(filename)
    with open("/Users/tanvisingh/Documents/Geromics/covcheck/tests/data/Osteoarithritis.json") as f:
        data = json.load(f)

    return data


  def read_json_individual(self):

  #  filename = pathlib.Path(path).name
    #print(filename)
    with open("/Users/tanvisingh/Documents/Geromics/covcheck/tests/data/dan_osteo.json") as f:
        data = json.load(f)

    return data

  def calculate_score(self,count,OR):
    score = float(count*OR)
    return score

  def display_score(self,snp,ORatio,Effect_Allele,Geneotype,scores):
    df = pd.DataFrame()
    df['snp']= snp
    df['Effect_Allele']=Effect_Allele
    df['Geneotype']=Geneotype
    df['ORatio']= ORatio
    df['scores']= scores
    print("Snp details")
    print("-----------------------")
    print(df)

  def score_report(self,snp,scores):
    l=len(snp)
    result=sum(scores)/l
    print()
    if result < 1:
        print("Your score is ", result)
        print("You are at less risk of developing Osteoarthritis")
    else:
        print("Your score is " , result)
        print("You are at high risk of developing Osteoarthritis")




  def parse_data_json(self,data,data1):
    scores = []
    snp = []
    ORatio = []
    Effect_Allele = []
    Geneotype = []
   # data = read_json_osteo()
   # data1 = read_json_individual()

    k = 0
    for i in data['groups']:

         if i['group_id'] == "44" and data1['age'] == 44:
               #print("Hello", list(data1['snps'].keys())[0])
               #print("Bye", list(i['snps'].keys())[0])
               l=len(list(i['snps'].keys()))
               l1=len(list(data1['snps'].keys()))
               #print(l1)
               for k in range(l):
                   for m in range(l1):
                       a = str(list(data1['snps'].keys())[m])
                       b = str(list(i['snps'].keys())[k])
                       #print ("a=" +a , "b="+b)
                       if a in b:
                          c1 = list(data1['snps'].values())[m]
                          c2 = list(i['snps'].values())[k]['effect_allele']
                          #print("match a=" + a, "b=" + b)
                          #print("----------------------------")
                          snp.append(a)
                          Effect_Allele.append(c2)
                          Geneotype.append(c1)
                          if c2 in c1:
                              count=c1.count(c2)
                              OR=list(i['snps'].values())[k]['OR']
                              score = float(count * OR)
                              s = score
                               # print(s)
                              ORatio.append(OR)
                              scores.append(s)
                          else:
                              s=0
                              OR = list(i['snps'].values())[k]['OR']
                              ORatio.append(OR)
                              scores.append(s)

    return snp,Effect_Allele,Geneotype,ORatio,scores


snp_osteo = Osteo()
data2=snp_osteo.read_json_osteo()
data3=snp_osteo.read_json_individual()
snp,Effect_Allele,Geneotype,ORatio,scores = snp_osteo.parse_data_json(data2,data3)
snp_osteo.display_score(snp,ORatio,Effect_Allele,Geneotype,scores)
snp_osteo.score_report(snp,scores)