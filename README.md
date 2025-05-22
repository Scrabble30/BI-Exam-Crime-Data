Recidivism and Influencing Factors BI Project

Sprint 1: Problem Formulation

Brainstorm:
After reviewing recidivism literature and exploring datasets on Statistics Denmark (Statistikbanken), our team identified the RECIDIV and STRAF series tables as rich sources. Key variables include original sentence length, education level, time-to-recidivism, and offender demographics. We compared BI use cases in public policy and correctional program evaluation to pinpoint how data-driven insights can optimize rehabilitation strategies.


Brief Annotation:
This project investigates which factors most influence recidivism rates among released offenders in Denmark. We examine how sentence severity and educational attainment affect the likelihood and timing of reoffense within three years. Using BI tools and predictive modeling, we aim to forecast recidivism risk for individuals based on these key variables. Insights will support policymakers and social workers in designing targeted interventions to reduce reoffending and improve reintegration outcomes.


Research Questions:
1.	How does original custodial sentence length impact the probability and timing of recidivism?
2.	To what extent does education level reduce the three-year recidivism rate?
3.	Do conditional sentences lead to faster recidivism compared to unconditional custodial sentences?
4.	Are younger releasees (<25 years) more likely to reoffend sooner than older releasees (>40 years)?


Hypotheses & Datasets:
•	H₀: Original sentence length does not predict recidivism rate or timing.
•   H₁: Longer sentences associate with lower probability and slower timing of recidivism.

•	H₀: Education level has no effect on three-year recidivism rate.
•   H₁: Higher education significantly reduces recidivism.

•	H₀: Time-to-reoffense is the same for conditional and unconditional sentences.
•   H₁: Those given conditional sentences reoffend faster.


Team Engagement:
•	Member A: Data extraction and cleaning (RECIDIV and STRAF tables)
•	Member B: EDA, visualization, and normality testing
•	Member C: Regression and clustering model development
•	Member D: Dashboard design, documentation, and presentation


🛠 Tools & Platforms:
•	Version Control: GitHub repository for code and documentation
•	Development: Jupyter Notebooks / VS Code
•	Libraries: pandas, matplotlib, scikit-learn, statsmodels
•	BI Platform: Power BI or Tableau for interactive dashboards