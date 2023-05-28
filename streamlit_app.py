import streamlit as st
from auth0_component import login_button
import base64
from PyPDF2 import PdfReader
import docx2txt
import os
import youtube_listing_videos_to_csv
import youtubescraper
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# Authenticate and create the YouTube API service
# youtube = youtube_listing_videos_to_csv.authenticate()
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def main():
        image_file = 'assets/background/sidebar_bg_3.jpg'
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
    smart_app_image_file = 'assets/background/main_bg_6.jpg'
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
    st.title('Plan Smart')
    st.write(' ### Spend Less Time Planning, More Time Excelling')
    # Add file upload button
    uploaded_file = st.file_uploader('Upload your syllabus here:', type=['pdf', 'doc', 'docx'])
    
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

        courses = text.split(", ")
        youtubevideolist = ['https://www.youtube.com/watch?v=h5Lv5ZeNl0g', 'https://www.youtube.com/watch?v=saAkSk_arPA']
        videos_output=[]
        for video in youtubevideolist:
            title, commentlist, views = youtubescraper.ScrapComment(video)
            num_comments = len(commentlist)
            score_list=[]
            scoretotal=0
            input_list = commentlist
            for input_text in input_list:
                tokens = tokenizer.encode(input_text, return_tensors='pt')
                result = model(tokens)
                result.logits
                score = int(torch.argmax(result.logits))+1
                scoretotal += score
                score_list.append(score)
            
            sentiment_score = scoretotal/len(score_list)
            video_data = {
                'title': title,
                'sentiment_score': sentiment_score,
                'comments': num_comments,
                'views': views
                }
        videos_output.append(video_data)

        for video in videos_output:
            # Weighted scores
            sentiment_score_weighted = video['sentiment_score'] * 0.5
            views_per_day_weighted = (video['views']) * 0.25
            likes_comments_weighted = (video['comments']) * 0.25

            # Overall score
            overall_score = sentiment_score_weighted + views_per_day_weighted + likes_comments_weighted
            video['overall_score'] = overall_score

        # Sorting videos based on overall score
        videos_output.sort(key=lambda x: x['overall_score'], reverse=True)

        # Assigning ranks to videos
        for rank, video in enumerate(videos_output, start=1):
            video['rank'] = rank

        # Printing the ranked videos
        for video in videos_output:
            st.write(f"Rank: {video['rank']}, Title: {video['title']}, Overall Score: {video['overall_score']}")

                
    # for course in courses:
    #     search_query = course
    #     st.write(search_query)
    #     videos = youtube_listing_videos_to_csv.get_video_list(youtube, search_query)

    # Save the video list to a df
    # df = youtube_listing_videos_to_csv.save_videos_to_df(videos)
    # st.dataframe(df)
    


def how_to_use():
    how_to_use_image_file = 'assets/background/main_bg_5.jpg'
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
    image_file = 'assets/background/main_bg_9.jpg'
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
    st.write('''
    # Summary
    PlanSmart is an innovative platform designed to alleviate one of the biggest challenges faced by students: finding the best study materials. The goal of PlanSmart is to streamline the process of selecting courses and materials, saving students valuable time and effort in their educational journey. \n
    The core functionality of PlanSmart revolves around the intelligent recommendation of videos based on a given syllabus. By leveraging web scraping techniques, PlanSmart gathers data from popular platforms such as YouTube, Coursera, and other online learning platforms. The platform then utilizes sentiment analysis to evaluate the content of these videos, assessing factors such as the quality of explanations, relevance to the topic, and overall user sentiment. This analysis helps to identify the best video resources for each topic within the syllabus.\n
    To further enhance the user experience, PlanSmart incorporates a ranking and recommendation system. Videos are assigned scores based on various factors, including sentimental analysis results, the number of views per day, and the number of likes and comments. These scores are then used to create an index ranging from 1 to 10, with the video with the highest score being ranked as the best option. This ranking system ensures that students are provided with the highest-quality videos for each topic, empowering them to make informed decisions about their study materials.\n
    # Working 
    PlanSmart goes beyond simply recommending videos by offering a comprehensive study plan generation feature. The recommended videos are organized into a structured study plan, providing students with a clear roadmap to follow in their learning journey. This study plan takes into account the duration and complexity of each video, allowing students to optimize their study schedule and ensure efficient progress through their syllabus.\n
    In addition to the study plan and video recommendations, PlanSmart incorporates a coin-based reward system. Students earn coins by completing their syllabus or achieving certain milestones. These coins can be redeemed for various rewards within the platform, such as accessing additional features, exclusive content, or even discounts on educational resources. The reward system aims to motivate and incentivize students, making the learning process more engaging and enjoyable.\n
    PlanSmart also places a strong emphasis on user experience and accessibility. The platform features a user-friendly and intuitive interface developed using Streamlit, enabling students to easily navigate through the site and access the recommended resources. Integration with authentication services, such as Auth0, ensures secure user logins and protects personal information. \n
    # Future Aspects
    Looking towards the future, PlanSmart has ambitious plans for expansion. This includes incorporating support for additional learning platforms, such as Udemy and Skillshare, to provide a broader range of study materials for students. The platform will continue to evolve, integrating new features and functionalities to cater to the diverse needs of students across various educational levels and subjects. \n
    # Summary
    In summary, PlanSmart aims to revolutionize the way students discover and access study materials by leveraging sentiment analysis, ranking and recommendation algorithms, and a user-friendly interface. With its comprehensive study plan generation, coin-based reward system, and focus on user experience, PlanSmart is poised to empower students in their educational pursuits, helping them save time, make informed decisions, and achieve academic excellence. \n 
    ''')


def show_rewards():
    image_file = 'assets/background/main_bg_8.jpg'
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
