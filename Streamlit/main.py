import streamlit as st
import recidiv9CleanUp
import recidiv10CleanUp

def show_homepage():
    st.image('images/crime.jpg', caption='Crime Data Visualization', use_column_width=True)

    st.write("")
    st.title('Recidivism and Influencing Factors BI Project')
    st.write('Group 6 - Made by: Bekhan, Otto, Victor & Patrick')

    st.header("""Sprint 1: Problem Formulation""")
    st.write("---------------")
    st.subheader("Brainstorm:")
    st.write("After reviewing recidivism literature and exploring datasets on Statistics Denmark (Statistikbanken), our team identified the RECIDIV and STRAF series tables as rich sources. Key variables include original sentence length, education level, time-to-recidivism, and offender demographics. We compared BI use cases in public policy and correctional program evaluation to pinpoint how data-driven insights can optimize rehabilitation strategies.")
    st.write("---------------")

    st.subheader("Brief Annotation:")
    st.write("This project investigates which factors most influence recidivism rates among released offenders in Denmark. We examine how sentence severity and educational attainment affect the likelihood and timing of reoffense within three years. Using BI tools and predictive modeling, we aim to forecast recidivism risk for individuals based on these key variables. Insights will support policymakers and social workers in designing targeted interventions to reduce reoffending and improve reintegration outcomes.")
    st.write("---------------")

    st.subheader("Research Questions:")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ1.</strong> Does the level of education affect the likelihood of recidivism across different age groups?</li>
            <li><strong>Dataset:</strong> RECIDIV9</li>
            <li></li>
            <li><strong>Variables:</strong> Recidivhændelser, Uddannelse, Alder, Køn</li>
            <li><strong>Purpose:</strong> To examine whether individuals with higher educational attainment have lower rates of recidivism within each age group.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ2.</strong> Are individuals with previous convictions more likely to recidivate than those without?</li>
            <li><strong>Dataset:</strong> RECIDIV10</li>
            <li></li>
            <li><strong>Variables:</strong> Tidligere_domme, Recidivhændelser</li>
            <li><strong>Purpose:</strong> To evaluate how prior criminal records influence the likelihood of committing new offenses.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ3.</strong> How does the number of previous convictions relate to the speed of reoffending?</li>
            <li><strong>Dataset:</strong> RECIDIV10</li>
            <li></li>
            <li><strong>Variables:</strong> Tidligere_domme, Varighed_til_tilbagefald</li>
            <li><strong>Purpose:</strong> To determine if repeat offenders reoffend faster than first-time offenders.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ4.</strong> Does gender influence the recidivism rate among those with the same educational level?</li>
            <li><strong>Dataset:</strong> RECIDIV9</li>
            <li></li>
            <li><strong>Variables:</strong> Køn, Uddannelse, Recidivhændelser</li>
            <li><strong>Purpose:</strong> To test for gender disparities in recidivism under similar educational backgrounds.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ5.</strong> Are younger individuals more likely to reoffend than older individuals?</li>
            <li><strong>Dataset:</strong> RECIDIV9 and RECIDIV10</li>
            <li></li>
            <li><strong>Variables:</strong> Alder, Recidivhændelser</li>
            <li><strong>Purpose:</strong> To compare age-related risk of recidivism.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("___")

    st.subheader("Hypotheses & Datasets")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>Education and Recidivism (RECIDIV9)</strong></li>
            <li><strong>H₀:</strong> There is no difference in recidivism rates across education levels.</li>
            <li><strong>H₁:</strong> Individuals with higher education have significantly lower recidivism rates than those with basic education.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border: 1px solid #ccc; color: black; padding: 15px; border-radius: 8px; background-color: #f9f9f3;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>Prior Convictions and Recidivism (RECIDIV10)</strong></li>
            <li><strong>H₀:</strong> Previous convictions do not affect the likelihood of recidivism.</li>
            <li><strong>H₁:</strong> Individuals with prior convictions have a higher likelihood of reoffending.</li>
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
