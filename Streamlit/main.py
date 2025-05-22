import streamlit as st

def show_homepage():
    st.image('images/crime.jpg', caption='Crime Data Visualization', use_column_width=True)

    st.write("")
    st.title('BI - CRIME DATA')
    st.write('Group 6 - Made by: Bekhan, Otto, Victor & Patrick')

    st.write("""
    ### Info om projektet her""")


def main():
    st.sidebar.title("Crime Data")
    page = st.sidebar.selectbox("Choose a page", ["Home page"])

    if page == "Home page":
        show_homepage()


if __name__ == "__main__":
    main()
