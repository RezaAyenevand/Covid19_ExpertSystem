#import Rule.py
import tkinter as tk
from tkinter import ttk

import Rule

rules = []
selected_symptoms = []
result = ''
name = ''

def get_rules():
    return rules
def click():

    label = tk.Label(root , text="Choose The symptoms")
    label.grid(row=0, column=1)
    draw_options()

def save_symptom(symptom):
    global selected_symptoms
    selected_symptoms.append(symptom)
    print(selected_symptoms)

def save_name():
    global name
    name = e.get()
    print_label = tk.Label(root, text=e.get())
    print_label.grid(row=7, column=1)
    print("name: ",name)


def save_result(diagnose):
    global result
    result = diagnose
    print(selected_symptoms)

def printsym():
    print(selected_symptoms)
    print_label = tk.Label(root, text="Selected Symptoms Are:" )
    print_label.grid(row=7, column=1)
    for i in range(len(selected_symptoms)):
        symp_label = tk.Label(root, text=selected_symptoms[i] +" ," )
        symp_label.grid(row=8, column=1 + i)

def make_rule():
    global name
    global selected_symptoms
    global result
    global rules
    rule = Rule.Rule(name, selected_symptoms , result)
    rules.append(rule)

    rule_name = f"rule name: {name}"
    rule_result = f"rule diagnosis: {result}:"
    symp_label = tk.Label(root, text='Rule Created Sucessfully', bd=3).grid(row=9, column=0)
    name_label = tk.Label(root, text=rule_name, bd=3).grid(row=10, column=0)
    result_label = tk.Label(root, text=rule_result, bd=3).grid(row=11, column=0)


def check_result():
    results = {'Covid 19': 'Covid-19',
               'Cold': 'Cold',
               'The Flu': 'Flu'
               }
    tk.Label(root, text='Choose Diagnosis', bd=3).grid(row=2, column=0)
    var_material = tk.StringVar()

    result = ttk.Combobox(root, values=list(results.keys()), justify="center", textvariable=var_material)
    result.bind('<<ComboboxSelected>>', lambda event: save_result(results[var_material.get()]))

    result.grid(row=2, column=1)
    result.current(0)
    tk.Button(root, text="Add Rule", command=make_rule).grid(column=0, row=6)

def draw_options():
    print(selected_symptoms)
    symptoms = {'High fever': 'High',
                'Mild fever': 'Mild',
                'No fever': 'None',
                'Dry cough': 'Dry',
                'No Cough': 'NoCough',
                'Wet cough': 'Wet',
                }

    label_selected = []

    tk.Label(root, text='Choose Symptom', bd=3).grid(row=2, column=0)
    var_material = tk.StringVar()

    symptom = ttk.Combobox(root, values=list(symptoms.keys()), justify="center", textvariable=var_material)
    symptom.grid(row=2 , column=1)
    symptom.bind('<<ComboboxSelected>>',lambda event: save_symptom(symptoms[var_material.get()]))
    symptom.current(0)
    tk.Button(root, text="Add Symptom", command=printsym).grid(column=0, row=5)
    tk.Button(root, text="Finish", command=check_result).grid(column=0, row=6)







root = tk.Tk()
root.title("ES Rule Maker")
root.configure(bg='Dodgerblue4')
e = tk.Entry(root , width=50)
e.grid(row=0, column=6)
tk.Button(root, text="Enter Rule's Name", command=save_name).grid(column=6, row=1)
click()
def main():
    symptoms = {'High fever': 'High',
                'Mild fever': 'Mild',
                'No fever': 'None',
                'Dry cough': 'Dry',
                'No Cough': 'NoCough',
                'Wet cough': 'Wet',
                }










    root.mainloop()

if __name__ == '__main__':
    main()