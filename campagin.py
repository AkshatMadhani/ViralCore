import streamlit as st
from phi.agent import Agent
from phi.tools.exa import ExaTools
from phi.model.google import Gemini
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
EXA_API_KEY=st.secrets["EXA_API_KEY"]
creator_matching_agent = Agent(
    name="Brand camapgin agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[ExaTools()],
    markdown=True,
    description="You are an expert marketing strategist who helps brands identify the best content creators for campaigns, generate creative content ideas, hashtags, and platform-specific strategies.",
    instructions=[
        "Analyze the brand's industry, target audience, and campaign goals to recommend creators who align with the brand's identity.",
        "Provide content ideas tailored to the campaign (e.g., themes, video styles, or post concepts).",
        "Suggest trending and relevant hashtags to maximize visibility.",
        "Recommend platforms that are best suited for the brand's target audience and campaign goals.",
        "Provide actionable insights, such as how the creator's content should look, the tone to use, and the engagement style.",
        "Focus on maximizing campaign effectiveness, user engagement, and brand visibility.",
        "Analyze competitor campaigns and suggest ways to outperform them.",
        "Use ExaTools to gather influencer data and provide recommendations for creators."
    ],
)

st.title("ViralCore: Influence Your Brand with Creative Campaigns")

brand_name = st.text_input("Enter your brand name")
target_audience = st.text_input("Describe your target audience (e.g., age group, interests, location)")
industry = st.text_input("Enter your industry (e.g., fashion, tech, F&B)")
primary_goal = st.text_input("What is your primary campaign goal? (e.g., brand awareness, lead generation, sales)")
preferred_platforms = st.text_input("Preferred platforms for the campaign (e.g., Instagram, TikTok, YouTube)")
content_tone = st.text_input("Preferred tone for the campaign (e.g., fun, professional, emotional)")

competitors = st.text_input("Enter your competitors ")

if st.button("Generate Creator and Campaign Recommendations"):
    user_query = f"""
    I am representing a brand named {brand_name} in the {industry} industry. 
    Our target audience includes {target_audience}, and our primary goal is {primary_goal}.
    We prefer to use {preferred_platforms}.
    The content tone we want is {content_tone}. 
    Competitors in the market are {competitors}. 
    Please recommend the best creators for our campaign (with reasoning), content ideas, 
    trending hashtags, platform-specific strategies, and ways to outperform our competitors.
    """

    with st.spinner("Generating recommendations..."):
        response = creator_matching_agent.run(user_query)
    
    st.write(response.content)

