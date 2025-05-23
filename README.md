Recidivism and Influencing Factors BI Project

Sprint 1: Problem Formulation

Brainstorm:
After reviewing recidivism literature and exploring datasets on Statistics Denmark (Statistikbanken), our team identified the RECIDIV and STRAF series tables as rich sources. Key variables include original sentence length, education level, time-to-recidivism, and offender demographics. We compared BI use cases in public policy and correctional program evaluation to pinpoint how data-driven insights can optimize rehabilitation strategies.


Brief Annotation:
This project investigates which factors most influence recidivism rates among released offenders in Denmark. We examine how sentence severity and educational attainment affect the likelihood and timing of reoffense within three years. Using BI tools and predictive modeling, we aim to forecast recidivism risk for individuals based on these key variables. Insights will support policymakers and social workers in designing targeted interventions to reduce reoffending and improve reintegration outcomes.


Research Questions:
____________________________________________________________________________________________________

RQ1. Does the level of education affect the likelihood of recidivism across different age groups?
Dataset: RECIDIV9

Variables: Recidivhændelser, Uddannelse, Alder, Køn

Purpose: To examine whether individuals with higher educational attainment have lower rates of recidivism within each age group.
____________________________________________________________________________________________________

RQ2. Are individuals with previous convictions more likely to recidivate than those without?
Dataset: RECIDIV10

Variables: Tidligere_domme, Recidivhændelser

Purpose: To evaluate how prior criminal records influence the likelihood of committing new offenses.
____________________________________________________________________________________________________

RQ3. How does the number of previous convictions relate to the speed of reoffending?
Dataset: RECIDIV10

Variables: Tidligere_domme, Varighed_til_tilbagefald

Purpose: To determine if repeat offenders reoffend faster than first-time offenders.
____________________________________________________________________________________________________

RQ4. Does gender influence the recidivism rate among those with the same educational level?
Dataset: RECIDIV9

Variables: Køn, Uddannelse, Recidivhændelser

Purpose: To test for gender disparities in recidivism under similar educational backgrounds.
____________________________________________________________________________________________________

RQ5. Are younger individuals more likely to reoffend than older individuals?
Datasets: RECIDIV9 and RECIDIV10

Variables: Alder, Recidivhændelser

Purpose: To compare age-related risk of recidivism.
____________________________________________________________________________________________________

✅ Updated Hypotheses
____________________________________________________________________________________________________

Education and Recidivism (RECIDIV9)
H₀: There is no difference in recidivism rates across education levels.

H₁: Individuals with higher education have significantly lower recidivism rates than those with basic education.
____________________________________________________________________________________________________

Prior Convictions and Recidivism (RECIDIV10)
H₀: Previous convictions do not affect the likelihood of recidivism.

H₁: Individuals with prior convictions have a higher likelihood of reoffending.
____________________________________________________________________________________________________

Prior Convictions and Time to Reoffend (RECIDIV10)
H₀: The number of prior convictions does not affect the time to reoffend.

H₁: Individuals with more prior convictions reoffend more quickly than those with none.
____________________________________________________________________________________________________

Gender and Recidivism (by Education) (RECIDIV9)
H₀: Gender does not affect recidivism rates among individuals with the same educational background.

H₁: Gender differences exist in recidivism rates even among equally educated individuals.
____________________________________________________________________________________________________

Age and Recidivism (RECIDIV9 & RECIDIV10)
H₀: Younger and older individuals reoffend at the same rate.

H₁: Younger individuals (15–24) have a higher recidivism rate than older individuals (50+).
____________________________________________________________________________________________________


Dataset: RECIDIV10 (gender, time to recidivism)


🛠 Tools & Platforms:
•	Version Control: GitHub repository for code and documentation
•	Development: Jupyter Notebooks / VS Code
•	Libraries: pandas, matplotlib, scikit-learn, statsmodels
•	BI Platform: Power BI or Tableau for interactive dashboards