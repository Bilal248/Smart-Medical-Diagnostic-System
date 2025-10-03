from pyswip import Prolog

def get_all_symptoms(prolog):
    symptoms = set()
    for result in prolog.query("symptom(_, L)"):
        symptoms.update(result['L'])
    return list(symptoms)

def ask_symptoms(possible_symptoms):
    patient_symptoms = []
    for symptom in possible_symptoms:
        ans = input(f"Do you have {symptom.replace('_', ' ')}? (y/n): ").strip().lower()
        if ans == 'y':
            patient_symptoms.append(symptom)
    return patient_symptoms

def main():
    prolog = Prolog()
    prolog.consult("prolog/medical_kb.pl")

    possible_symptoms = get_all_symptoms(prolog)
    patient_symptoms = ask_symptoms(possible_symptoms)
    if not patient_symptoms:
        print("No symptoms entered. Cannot diagnose.")
        return

    prolog_sym = "[" + ",".join(patient_symptoms) + "]"
    query = f"diagnose({prolog_sym}, Condition)"
    results = list(prolog.query(query))
    if results:
        print(results[0]['Condition'])
    else:
        print("No diagnosis found.")

if __name__ == '__main__':
    main()
