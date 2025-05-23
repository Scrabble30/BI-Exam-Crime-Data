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
    <div style="border: 0px solid #ccc; color: white; padding: 15px; border-radius: 8px; background-color: #262730;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ1: Linear Regression</strong></li>
            <li><strong>Question:</strong> How do prior convictions, age, and gender predict the time until first reoffense?</li>
            <li><strong>Dataset:</strong> Recidiv 10 </li>
            <li>______________________________________________________________________________</li>
            <li><strong>H:</strong> Offenders with more prior convictions, younger age, or male gender will have significantly shorter times until first reoffense.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border: 0px solid #ccc; color: white; padding: 15px; border-radius: 8px; background-color: #262730;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ2: Clustering</strong></li>
            <li><strong>Question:</strong> What natural clusters of offenders emerge when grouping by recidivism frequency, education, age, and gender?</li>
            <li><strong>Dataset:</strong> Recidiv 9 </li>
            <li>______________________________________________________________________________</li>
            <li><strong>H:</strong> Distinct offender clusters (e.g., “young low-educated repeat offenders” vs. “older high-educated occasional offenders”) will emerge with strong internal cohesion (silhouette score ≥ 0.5).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border: 0px solid #ccc; color: white; padding: 15px; border-radius: 8px; background-color: #262730;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ3: Classification</strong></li>
            <li><strong>Question:</strong> Can we classify whether an individual will reoffend at least once based on age, gender, and prior convictions?</li>
            <li><strong>Dataset:</strong> Recidiv 10 </li>
            <li>______________________________________________________________________________</li>
            <li><strong>H:</strong> A classification model using age, gender, and prior convictions will achieve ROC AUC ≥ 0.75 in predicting any recidivism.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div style="border:0px solid #ccc; color: white; padding: 15px; border-radius: 8px; background-color: #262730;">
        <ul style="margin-top: 0; list-style-type: none; padding-left: 0;">
            <li><strong>RQ4: Descriptive Statistics</strong></li>
            <li><strong>Question:</strong> What are the central tendency and variability characteristics of “time until first reoffense” across different education levels?</li>
            <li><strong>Dataset:</strong> Recidiv 6 </li>
            <li>______________________________________________________________________________</li>
            <li><strong>H:</strong> The distribution of time to first reoffense (e.g., mean, median, variance) differs significantly between education levels, with higher-educated offenders exhibiting longer times until reoffense.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
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
