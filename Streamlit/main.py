import streamlit as st
import recidiv9CleanUp
import recidiv10CleanUp

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
        4. Are younger releasees (<25 years) more likely to reoffend than older releasees (>40 years)?
    """)
    st.write("")

    st.subheader("Hypotheses & Datasets")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>H₀:</strong> Original sentence length does not predict recidivism rate or timing.</li>
            <li><strong>H₁:</strong> Longer sentences associate with lower probability and slower timing of recidivism.</li>
            <li><strong>Datasets:</strong> RECIDIV10</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>H₀:</strong> Education level has no effect on three-year recidivism rate.</li>
            <li><strong>H₁:</strong> Higher education significantly reduces recidivism.</li>
            <li><strong>Datasets:</strong> RECIDIV9</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>H₀:</strong> Time-to-reoffense is the same for conditional and unconditional sentences.</li>
            <li><strong>H₁:</strong> Those given conditional sentences reoffend faster.</li>
            <li><strong>Datasets:</strong> RECIDIV10</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
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
    - RECIDIV1–9, RECIDIV10: Time to recidivism, original sentence, education (2007–2022)
                
    - https://www.statistikbanken.dk/10059
    """)





def main():
    st.sidebar.title("Crime Data")
    show_home = st.sidebar.button("🏠 Home Page")
    cleanup_page = st.sidebar.selectbox("Clean up", ["Recidiv 9 - Cleanup", "Recidiv 10 - Cleanup"])
    page = st.sidebar.selectbox("test", ["test"])

    if show_home:
        show_homepage()
    elif cleanup_page == "Recidiv 9 - Cleanup":
        recidiv9CleanUp.recidiv9cleanup()
    elif cleanup_page == "Recidiv 10 - Cleanup":
        recidiv10CleanUp.recidiv10cleanup()


if __name__ == "__main__":
    main()
