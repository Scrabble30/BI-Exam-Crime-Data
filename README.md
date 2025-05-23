Recidivism and Influencing Factors BI Project

Sprint 1: Problem Formulation

Brainstorm:
After reviewing recidivism literature and exploring datasets on Statistics Denmark (Statistikbanken), our team identified the RECIDIV and STRAF series tables as rich sources. Key variables include original sentence length, education level, time-to-recidivism, and offender demographics. We compared BI use cases in public policy and correctional program evaluation to pinpoint how data-driven insights can optimize rehabilitation strategies.


Brief Annotation:
This project investigates which factors most influence recidivism rates among released offenders in Denmark. We examine how sentence severity and educational attainment affect the likelihood and timing of reoffense within three years. Using BI tools and predictive modeling, we aim to forecast recidivism risk for individuals based on these key variables. Insights will support policymakers and social workers in designing targeted interventions to reduce reoffending and improve reintegration outcomes.


Research Questions:

RQ1: Linear Regression
Question: How do prior convictions, age, and gender predict the time until first reoffense?
Dataset: Recidiv10.
H: Offenders with more prior convictions, younger age, or male gender will have significantly shorter times until first reoffense.

RQ2: Clustering
Question: What natural clusters of offenders emerge when grouping by recidivism frequency, education, age, and gender?
Dataset: Recidiv 9.
H: Distinct offender clusters (e.g., “young low-educated repeat offenders” vs. “older high-educated occasional offenders”) will emerge with strong internal cohesion (silhouette score ≥ 0.5).

RQ3: Classification
Question: Can we classify whether an individual will reoffend at least once based on age, gender, and prior convictions?
Dataset: Recidiv 10.
H: A classification model using age, gender, and prior convictions will achieve ROC AUC ≥ 0.75 in predicting any recidivism.

RQ4: Descriptive Statistics
Question: What are the central tendency and variability characteristics of “time until first reoffense” across different education levels?
Dataset: Recidiv 6.
H: The distribution of time to first reoffense (e.g., mean, median, variance) differs significantly between education levels, with higher-educated offenders exhibiting longer times until reoffense.


🛠 Tools & Platforms:
•	Version Control: GitHub repository for code and documentation
•	Development: Jupyter Notebooks / VS Code
•	Libraries: pandas, matplotlib, scikit-learn, statsmodels
•	BI Platform: Power BI or Tableau for interactive dashboards