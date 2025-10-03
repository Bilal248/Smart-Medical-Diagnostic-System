Medical Knowledge-Based System
Domain: ENT (Nose-related conditions)
Problems covered: acute_sinusitis, chronic_sinusitis, rhinitis, deviated_nasal_septum

Deliverables:
- Prolog knowledge base (medical_kb.pl)
- Python client showing how to use pyswip with SWI-Prolog (query_prolog.py)
- A simple rule-based engine with a Tkinter GUI (rule_engine_gui.py)
- Sample screenshots demonstrating example inputs and inferencing
- This zip is packaged for a group of 4 students; no exception needed.

Due date: 3 Oct 2025

--- Quick structure ---
prolog/medical_kb.pl           -- Prolog facts & rules
pyswip_client/query_prolog.py -- Example Python code using pyswip
rule_engine_gui/rule_engine_gui.py -- Tkinter GUI + forward-chaining rules in Python
screenshots/                   -- Example PNG screens (sample outputs)
README.md

--- How to run (local machine) ---

1. Prolog (SWI-Prolog)
   - Install SWI-Prolog (https://www.swi-prolog.org)
   - Run SWI-Prolog and consult the file:
       ?- [medical_kb].
     Example queries:
       ?- diagnose([nasal_congestion, thick_discharge, facial_pain], C).

     The expected diagnoses are:
       acute_sinusitis, chronic_sinusitis, rhinitis, deviated_nasal_septum
     See prolog/medical_kb.pl for full examples.

2. Python + pyswip
   - Install pyswip: pip install pyswip
   - Ensure SWI-Prolog is installed and available in PATH.
   - Run:
       python3 pyswip_client/query_prolog.py

     This script demonstrates asserting symptoms and querying diagnoses via pyswip.

3. Rule-based engine with GUI (no extra libraries)
   - Run:
       streamlit run rule_engine_gui/rule_engine_gui.py
     A simple web app  will open where you can check symptoms and press INFER to get diagnoses.

--- Notes for group of 2 ---
No group approached us to join their team, so we proceeded as a group of two.

  
