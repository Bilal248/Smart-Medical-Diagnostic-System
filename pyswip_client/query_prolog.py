# query_prolog.py
# Example usage of pyswip to consult the Prolog KB and query diagnoses.
# Note: Requires SWI-Prolog installed and pyswip Python package.
# Install: pip install pyswip
# Run: python3 query_prolog.py

from pyswip import Prolog, Functor, Variable, Query

def run_example():
    prolog = Prolog()
    # adjust path if needed
    prolog.consult("prolog/medical_kb.pl")
    print("Consulted medical_kb.pl")

    # Example: assert symptoms for a patient and query diagnoses
    patient_symptoms = ['recent_onset','fever','facial_pain','purulent_nasal_discharge']
    # Convert Python list to Prolog list representation as atoms
    prolog_sym = "[" + ",".join(patient_symptoms) + "]"
    # Query diagnose(Symptoms, Dx).
    query = f"diagnose({prolog_sym}, Dx)"
    print("Running query:", query)
    results = list(prolog.query(query))
    if results:
        print("Diagnoses found:")
        for r in results:
            print(" -", r['Dx'])
    else:
        print("No diagnosis returned by KB.")

if __name__ == '__main__':
    run_example()
