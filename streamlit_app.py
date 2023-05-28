import streamlit as st
from auth0_component import login_button
import base64
from PyPDF2 import PdfReader
import docx2txt
import os
import youtube_listing_videos_to_csv

# Authenticate and create the YouTube API service
# youtube = youtube_listing_videos_to_csv.authenticate()

def main():
        image_file = 'assets/background/sidebar_bg_2.jpg'
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
            <style>
            .css-6qob1r {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover;
                colour:
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        # Add logo and app name
        st.sidebar.image('logo/plansmart_logo_1.png', use_column_width=True)
        st.sidebar.title('PlanSmart')
        # Add app description
        st.sidebar.write('A short description about the app')
        # Create navigation bar with two sections
        st.sidebar.title('Navigation')
        app_section = st.sidebar.radio('Go to', ['PlanSmart App', 'How to use' , 'Rewards', 'About PlanSmart'])
        if app_section == 'PlanSmart App':
            show_plan_smart_app()
        elif app_section == 'How to use':
            how_to_use()
        elif app_section == 'Rewards':
            show_rewards()
        elif app_section == 'About PlanSmart':
            show_about_plan_smart()
        
        
def show_plan_smart_app():
    smart_app_image_file = 'assets/background/main_bg_1.jpg'
    with open(smart_app_image_file, "rb") as smart_app_image_file:
        smart_app_encoded_string = base64.b64encode(smart_app_image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{smart_app_encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    # PlanSmart App section
    st.title('PlanSmart App')
    
    # Add file upload button
    uploaded_file = st.file_uploader('Upload a file', type=['pdf', 'doc', 'docx'])
    
    # Process the uploaded file
    if uploaded_file is not None:
        if uploaded_file.type == 'application/pdf':
            """
            Extracts text from a PDF document.
            """
            text = ''
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
            st.write('Text extracted from the PDF document:')
            st.write(text)

        elif uploaded_file.type == 'application/msword':
            """
            Extracts text from a Word document.
            """
            text = docx2txt.process(uploaded_file)
            st.write('Text extracted from the Word document:')
            st.write(text)

        else:
            st.write('Unsupported file format. Please upload a PDF or Word document.')

    courses = ['Partial ordering relations', 'Poset', 'Lattices', 'Basic Properties of Lattices', 'Distributive', 'complemented lattices', 'Boolean lattices', 'Boolean Algebra', 'Propositional', 'Predicate']

    # for course in courses:
    #     search_query = course
    #     st.write(search_query)
    #     videos = youtube_listing_videos_to_csv.get_video_list(youtube, search_query)

    # Save the video list to a df
    # df = youtube_listing_videos_to_csv.save_videos_to_df(videos)
    # st.dataframe(df)
    


def how_to_use():
    how_to_use_image_file = 'assets/background/main_bg_4.jpg'
    with open(how_to_use_image_file, "rb") as how_to_use_image_file:
        how_to_use_encoded_string = base64.b64encode(how_to_use_image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{how_to_use_encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    st.title("How to give a good input")
    st.write("Write the Syllabus in the given format below for the best results")

    # Example usage
    st.write("""
    ### Example format
    MA2101: ENGINEERING MATHEMATICS III \n
    topic: Boolean Algebra \n
    course content :  Partial ordering relations, Poset, Lattices, Basic Properties of Lattices. Distributive and complemented lattices, Boolean lattices, and Boolean Algebra. Propositional and Predicate. \n
    topic: Calculus \n
    course content : Well-formed formula, connectives, quantifications, Inference theory of propositional and predicate calculus. \n
    topic: Elementary configuration \n
    course content : Permutations and Combinations, Generating function, Principle of inclusion and exclusion Partitions, compositions. \n

    AI2101: RELATIONAL DATABASE MANAGEMENT SYSTEMS \n
    topic: Introduction \n
    course content : Database -System Applications, Relational Databases, Database Design, Data Storage and Querying, Transaction Management, Database Architecture. \n
    topic: Relational Algebra \n
    course content : Fundamental Relational -Algebra Operations, Extended Relational -Algebra Operations, Null Val ues, Modification of the Database. \n
    
    """)

    
    

def show_about_plan_smart():
    image_file = 'assets/background/main_bg_2.jpg'
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    # About PlanSmart section
    st.title('About PlanSmart')
    st.write('Detailed information about PlanSmart goes here.')


def show_rewards():
    image_file = 'assets/background/main_bg_2.jpg'
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    # Rewards section
    st.title('Rewards')
    st.write('Earn coins by completing tasks and redeem them for exciting rewards!')
    
    coins_earned = 100  # Example: Replace with the actual coins earned by the student
    st.subheader('Your Coins')
    st.write(f"You have {coins_earned} coins")

    redemption_level = 500  # Example: Specify the redemption level for rewards
    if coins_earned >= redemption_level:
        st.success('Congratulations! You can redeem your coins for rewards.')
        st.button('Redeem Coins')
        # Add reward redemption logic here when the button is clicked
    else:
        remaining_coins = redemption_level - coins_earned
        st.warning(f"Earn {remaining_coins} more coins to unlock redemption.")

if __name__ == '__main__':
    main()
