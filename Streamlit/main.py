import streamlit as st

def show_homepage():
    st.image('images/crime.jpg', caption='Crime Data Visualization', use_column_width=True)

    st.write("")
    st.title('Recidivism and Influencing Factors BI Project')
    st.write('Group 6 - Made by: Bekhan, Otto, Victor & Patrick')

    st.header("""Sprint 1: Problem Formulation""")
    st.subheader("Brainstorm:")
    st.write("After reviewing recidivism literature and exploring datasets on Statistics Denmark (Statistikbanken), our team identified the RECIDIV and STRAF series tables as rich sources. Key variables include original sentence length, education level, time-to-recidivism, and offender demographics. We compared BI use cases in public policy and correctional program evaluation to pinpoint how data-driven insights can optimize rehabilitation strategies.")
    st.write("")

    st.subheader("Brief Annotation:")
    st.write("This project investigates which factors most influence recidivism rates among released offenders in Denmark. We examine how sentence severity and educational attainment affect the likelihood and timing of reoffense within three years. Using BI tools and predictive modeling, we aim to forecast recidivism risk for individuals based on these key variables. Insights will support policymakers and social workers in designing targeted interventions to reduce reoffending and improve reintegration outcomes.")
    st.write("")

    st.subheader("Research Questions:")
    st.markdown("""
        1. How does original custodial sentence length impact the probability and timing of recidivism?
        2. To what extent does education level reduce the three-year recidivism rate?
        3. Do conditional sentences lead to faster recidivism compared to unconditional custodial sentences?
        4. Are younger releasees (<25 years) more likely to reoffend sooner than older releasees (>40 years)?
    """)
    st.write("")

    st.subheader("Hypotheses & Datasets")
    st.write("•H₀: Original sentence length does not predict recidivism rate or timing.")
    st.write("H₁: Longer sentences associate with lower probability and slower timing of recidivism.")
    st.write("Datasets: RECIDIV3, RECIDIV4")
    st.write("")
    st.write("•H₀: Education level has no effect on three-year recidivism rate.")
    st.write("H₁: Higher education significantly reduces recidivism.")
    st.write("Datasets: RECIDIV6, RECIDIV7, RECIDIV8, RECIDIV9")
    st.write("")
    st.write("•H₀: Time-to-reoffense is the same for conditional and unconditional sentences.")
    st.write("H₁: Those given conditional sentences reoffend faster.")
    st.write("Datasets: RECIDIV1, RECIDIV5")
    st.write("")

    st.subheader("🛠 Tools & Platforms")
    st.markdown("""
        - Version Control: GitHub repository for code and documentation
        - Development: Jupyter Notebooks / VS Code
        - Libraries: pandas, matplotlib, scikit-learn, statsmodels, streamlit
        - BI Platform: Power BI or Tableau for interactive dashboards
    """)
    st.write("")

    st.subheader("Data Sources & Links")
    st.markdown("""
    - RECIDIV1–9, RECIDIV11: Time to recidivism, original sentence, education (2007–2022)
                
    - https://www.statistikbanken.dk/10059
    """)





def main():
    st.sidebar.title("Crime Data")
    page = st.sidebar.selectbox("Choose a page", ["Home page"])

    if page == "Home page":
        show_homepage()


if __name__ == "__main__":
    main()
