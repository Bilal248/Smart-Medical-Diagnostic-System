% medical_kb.pl
% Knowledge base for ENT conditions: acute_sinusitis, chronic_sinusitis, rhinitis, deviated_nasal_septum
% Facts and rules use a simple symptom-list approach.

% Sample symptoms (you can assert these into the DB per patient)
% symptoms(Patient, [symptom1, symptom2, ...]).

% Definitions / helper predicates
member_of(X,[X|_]).
member_of(X,[_|T]):- member_of(X,T).

has_sym(S, L) :- member_of(S, L).

has_all([], _).
has_all([H|T], L) :- has_sym(H,L), has_all(T,L).

% Rules for diagnoses - these are intentionally simple and for educational use only.
% Acute sinusitis: recent onset (<= 4 weeks) OR recent_infection, fever, facial pain, purulent nasal discharge
diagnose(Symptoms, acute_sinusitis) :-
    has_all([recent_onset, fever, facial_pain, purulent_nasal_discharge], Symptoms).

diagnose(Symptoms, acute_sinusitis) :-
    has_all([recent_infection, facial_pain, purulent_nasal_discharge], Symptoms).

% Chronic sinusitis: symptoms lasting > 12 weeks, nasal obstruction, facial pressure, hyposmia (reduced smell)
diagnose(Symptoms, chronic_sinusitis) :-
    has_all([symptoms_more_than_12_weeks, nasal_obstruction, facial_pressure], Symptoms).

% Allergic rhinitis: sneezing, itching, watery_rhinorrhea, seasonal or allergen_exposure
diagnose(Symptoms, rhinitis_allergic) :-
    has_all([sneezing, nasal_itching, watery_rhinorrhea, allergen_exposure], Symptoms).

% Non-allergic rhinitis: rhinorrhea, nasal_congestion, no allergen history
diagnose(Symptoms, rhinitis_non_allergic) :-
    has_all([watery_rhinorrhea, nasal_congestion], Symptoms),
    \\+ has_sym(allergen_exposure, Symptoms).

% Deviated nasal septum: history of trauma or visible_deviation or chronic_nasal_obstruction with unilateral symptoms
diagnose(Symptoms, deviated_nasal_septum) :-
    has_all([visible_deviation, chronic_nasal_obstruction], Symptoms).

diagnose(Symptoms, deviated_nasal_septum) :-
    has_all([history_of_trauma, unilateral_nasal_obstruction], Symptoms).

% Catch-all: if no rule matches, unknown
diagnose(_, unknown).

% Example dataset (patients with symptoms)
% Uncomment to use sample facts:
% symptoms(patient1, [recent_onset, fever, facial_pain, purulent_nasal_discharge]).
% symptoms(patient2, [symptoms_more_than_12_weeks, nasal_obstruction, facial_pressure]).
% symptoms(patient3, [sneezing, nasal_itching, watery_rhinorrhea, allergen_exposure]).
% symptoms(patient4, [visible_deviation, chronic_nasal_obstruction]).

% End of KB
