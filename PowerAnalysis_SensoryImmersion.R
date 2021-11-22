# Power analysis

library(pwr)
# Hypothesis 1: A  bivariate linear regression on self-reported immersion scores by sensory feature condition (dummy-coded) 
# and sequences (dummy-coded). 

pwr.f2.test(u = 4, f2 = 0.15, sig.level = 0.05, power = 0.95)

# Hypothesis 2: A linear multiple regression on the total number of saccades with self-reported immersion scores, 
# sensory feedback condition (dummy-coded), sequences (dummy-coded) and immersion-by-condition interaction terms

pwr.f2.test(u = 7, f2 = 0.15, sig.level = 0.05, power = 0.95)

# Hypotheses 3: A linear multiple regression on pupil dilation with self-reported immersion scores, sensory
# feedback condition (dummy coded), outcome type (dummy coded), phase, and sequences (dummy-coded). 

pwr.f2.test(u = 9, f2 = 0.15, sig.level = 0.05, power = 0.95)

# Hypotheis 4: A linear multiple regression on ratio of dwell time on credit window to spinning reels window with 
# self-reported immersion scores, sensory feedback condition (dummy coded), outcome type (dummy coded), and sequences (dummy-coded). 

pwr.f2.test(u = 7, f2 = 0.15, sig.level = 0.05, power = 0.95)

# Hypothesis 5: A  linear multiple regression on pupil diameter for each fixation with sensory feedback condition (dummy-coded), 
# outcome type (dummy coded), phase as predictor variables (dummy coded), sequences (dummy-coded), and sensory immersion scores. 

pwr.f2.test(u = 9, f2 = 0.15, sig.level = 0.05, power = 0.95)

#Redoing the power analysis: 

pwr.f2.test(u = 4, f2 = 0.15, sig.level = 0.01, power = 0.80)

pwr.f2.test(u = 7, f2 = 0.15, sig.level = 0.01, power = 0.80)

pwr.f2.test(u = 9, f2 = 0.15, sig.level = 0.01, power = 0.80)

pwr.f2.test(u = 7, f2 = 0.15, sig.level = 0.01, power = 0.80)

pwr.f2.test(u = 9, f2 = 0.15, sig.level = 0.01, power = 0.80)
