% Symptoms for each condition
symptom(acute_sinusitis, [nasal_congestion, thick_discharge, facial_pain, headache, fever]).
symptom(chronic_sinusitis, [nasal_congestion, thick_discharge, facial_pain, reduced_smell, fatigue]).
symptom(rhinitis, [sneezing, runny_nose, itchy_nose, nasal_congestion]).
symptom(deviated_septum, [nasal_obstruction, frequent_infections, nosebleeds, snoring]).

% Count matching symptoms
match_count([], _, 0).
match_count([S|Ss], L, C) :- member(S, L), !, match_count(Ss, L, R), C is R+1.
match_count([_|Ss], L, C) :- match_count(Ss, L, C).

% Score each condition
score(Cond, Input, Score) :- symptom(Cond, CondSyms), match_count(CondSyms, Input, Score).

% Diagnose: pick condition with highest score
diagnose(Symptoms, Best) :-
    findall(Score-Cond, score(Cond, Symptoms, Score), Scores),
    sort(0, @>=, Scores, [BestScore-Best|_]), BestScore > 0, !.
diagnose(_, unknown).