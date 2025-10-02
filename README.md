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
       ?- symptoms(patient1, [fever, facial_pain, nasal_discharge, recent_onset]).
       ?- diagnose(patient1, Dx).
     The expected diagnoses are:
       acute_sinusitis, chronic_sinusitis, rhinitis, deviated_nasal_septum
     See prolog/medical_kb.pl for full examples.

2. Python + pyswip
   - Install pyswip: pip install pyswip
   - Ensure SWI-Prolog is installed and available in PATH.
   - Run:
       python3 query_prolog.py
     This script demonstrates asserting symptoms and querying diagnoses via pyswip.

3. Rule-based engine with GUI (no extra libraries)
   - Run:
       python3 rule_engine_gui.py
     A simple Tkinter GUI will open where you can check symptoms and press INFER to get diagnoses.

--- Notes for group of 4 ---
This project is intentionally packaged for 4 students. Split responsibilities:
  - Member A: Prolog knowledge base and testing queries
  - Member B: Python pyswip integration
  - Member C: Rule engine & GUI
  - Member D: Report, screenshots, and packaging

If your group size differs, you can still use the same partitioning; let me know if you need a different layout.

