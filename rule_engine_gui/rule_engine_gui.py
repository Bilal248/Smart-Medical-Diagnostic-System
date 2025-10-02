# rule_engine_gui.py
# Simple rule-based engine with a Tkinter GUI for symptom input and forward-chaining inference.
# No external libraries required.
# Run: python3 rule_engine_gui.py

import tkinter as tk
from tkinter import ttk, messagebox

# Define rules as functions; each rule returns diagnosis if matched.
def rule_acute(symptoms):
    needed = {'recent_onset','fever','facial_pain','purulent_nasal_discharge'}
    if needed.issubset(symptoms):
        return 'acute_sinusitis'
    # alternate rule
    if {'recent_infection','facial_pain','purulent_nasal_discharge'}.issubset(symptoms):
        return 'acute_sinusitis'
    return None

def rule_chronic(symptoms):
    needed = {'symptoms_more_than_12_weeks','nasal_obstruction','facial_pressure'}
    if needed.issubset(symptoms):
        return 'chronic_sinusitis'
    return None

def rule_rhinitis_allergic(symptoms):
    needed = {'sneezing','nasal_itching','watery_rhinorrhea','allergen_exposure'}
    if needed.issubset(symptoms):
        return 'rhinitis_allergic'
    return None

def rule_rhinitis_non_allergic(symptoms):
    needed = {'watery_rhinorrhea','nasal_congestion'}
    if needed.issubset(symptoms) and 'allergen_exposure' not in symptoms:
        return 'rhinitis_non_allergic'
    return None

def rule_deviated(symptoms):
    if {'visible_deviation','chronic_nasal_obstruction'}.issubset(symptoms) or {'history_of_trauma','unilateral_nasal_obstruction'}.issubset(symptoms):
        return 'deviated_nasal_septum'
    return None

RULES = [rule_acute, rule_chronic, rule_rhinitis_allergic, rule_rhinitis_non_allergic, rule_deviated]

SYMPTOMS = [
    'recent_onset','recent_infection','fever','facial_pain','purulent_nasal_discharge',
    'symptoms_more_than_12_weeks','nasal_obstruction','facial_pressure','sneezing',
    'nasal_itching','watery_rhinorrhea','allergen_exposure','nasal_congestion',
    'visible_deviation','chronic_nasal_obstruction','history_of_trauma','unilateral_nasal_obstruction'
]

class App:
    def __init__(self, root):
        self.root = root
        root.title("Medical Rule Engine - ENT (Demo)")

        self.vars = {}
        row = 0
        ttk.Label(root, text="Select symptoms present:").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        row += 1
        for i, s in enumerate(SYMPTOMS):
            var = tk.BooleanVar()
            chk = ttk.Checkbutton(root, text=s, variable=var)
            chk.grid(row=row + i//2, column=i%2, sticky='w', padx=10)
            self.vars[s] = var
        bottom_row = row + len(SYMPTOMS)//2 + 2
        ttk.Button(root, text="Infer Diagnosis", command=self.infer).grid(row=bottom_row, column=0, padx=10, pady=10)
        ttk.Button(root, text="Clear", command=self.clear).grid(row=bottom_row, column=1, padx=10, pady=10)
        self.output = tk.Text(root, height=8, width=60)
        self.output.grid(row=bottom_row+1, column=0, columnspan=2, padx=10, pady=5)

    def infer(self):
        symptoms = {s for s,v in self.vars.items() if v.get()}
        diagnoses = []
        # forward chaining: evaluate rules in order, append diagnoses if found
        for r in RULES:
            d = r(symptoms)
            if d and d not in diagnoses:
                diagnoses.append(d)
        if not diagnoses:
            diagnoses = ['unknown']
        self.output.delete('1.0', tk.END)
        self.output.insert(tk.END, "Symptoms selected: {}\n\n".format(", ".join(symptoms) if symptoms else "none"))
        self.output.insert(tk.END, "Diagnoses inferred:\n")
        for d in diagnoses:
            self.output.insert(tk.END, " - {}\n".format(d))

    def clear(self):
        for v in self.vars.values():
            v.set(False)
        self.output.delete('1.0', tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
