from time import sleep
from os import system
import os
import base
k=0
ordered_symptom = ['cough', 'fever', 'muscle_pain','breath_shortness','sneeze_and_drops','gender','age']
symptom_types = [['Dry','NoCough','Wet'],['High','Mild','None'],['Yes','No'],['Yes','No'],['Yes','No'],['Male','Female'],['Adult','Child']]
symptoms_list = []
ruleNum = 1



def Clear():
    os.system( 'cls' )

questions = []
for i in range(len(ordered_symptom)):
    string = ''
    for j in symptom_types[i]:
        string += f"{j}, "
    questions.append(f"Do You Have {ordered_symptom[i]}?({string}) ?")
#while True:
print("#############################################################")
print("############# Covid-19 Diagnosing Expert System #############")
print("#############################################################")
print("#")
print("#")
print("#")
print("#")
if k ==0:
    print("# Welcome!")
    print("# I will ask you about your symptoms and try to diagnose your illness type")
    input("# Press Any Key When You Are Ready..")
    k +=1
for question in questions:
    print("#",question)
    symptom = input("Please Write Your Symptom...\n")
    symptoms_list.append(symptom)
    result = base.diagnose(symptoms_list)
    if result == 'Covid-19':
        print("# From The Symptoms You Have Mentioned,")
        print("# I Have Concluded That You Are Probably Infected With : ", result)
        print("# I Suggest You Visit Your Doctor And Seek Medical Treatments")
        print("# Please Stay In An Isolated Room And Cover Your Face With A Mask")
        break
    if result == 'Cold':
        print("# From The Symptoms You Have Mentioned,")
        print("# I Have Concluded That You Are Probably Infected With : ", result)
        print("# Luckily, This Disease Is Not Dangerous.")
        print("# I Suggest You Rest And Drink Fluids For A Couple Of Days")
        break
    if result == 'Flu':
        print("# From The Symptoms You Have Mentioned,")
        print("# I Have Concluded That You Are Probably Infected With : ", result)
        print("# You Are Not Infected With Covid However,")
        print("# The Flue Is ALso Dangerous I Suggest You Visit Your Doctor Soon")
        break
    else:
        pass
    ruleNum += 1
print("# Thank You For Consulting With Me.I Hope You Feel Better Soon")
