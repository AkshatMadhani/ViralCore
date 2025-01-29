import streamlit as st
from phi.agent import Agent
from phi.tools.exa import ExaTools
from phi.model.google import Gemini
from dotenv import load_dotenv
load_dotenv()
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
EXA_API_KEY=st.secrets["EXA_API_KEY"]
content_creation_agent = Agent(
    name="FlowIdea Agents",
    tools=[ExaTools()],
    model=Gemini(id="gemini-1.5-flash"),
    description="Content creation agent to suggest trending topics, hashtags, and generate transcripts for your content style.",
    instructions=[
        "Analyze current trends on YouTube, Instagram, and Facebook for content styles like Vlogger, Roaster, Gaming, Shorts,Tech, Movie.",
        "Provide transcript suggestions, current trending topics, hashtags, and video descriptions that align with the creator's niche and audience.",
        "Suggest hashtags, and video ideas tailored to maximize views and engagement on platforms like YouTube, Instagram, and Facebook.",
        "Offer creative content ideas based on the trending topics and content style of the creator."
    ]
)

st.title("StoryCraft: Where Ideas Turn into Engaging Content")

target_audience = st.text_input("Describe your target audience (e.g., age group, interests, location)")
content_ideas = st.text_input("tell me about your content sytle")
video_length = st.text_input("give me length of video")
content_format = st.text_input("enter your content idea")

platforms = st.multiselect("Select platforms for your content", ["Instagram", "Facebook", "YouTube"])

content_goal = "Increase views and attract brand sponsors by producing trending content."

if st.button("Content processing"):
    user_query = f"""
    I am creating content targeting {target_audience}. The content idea is {content_ideas}. 
    The video length preference is {video_length}. The content format preference is {content_format}. 
    The goal is to increase views, make content enjoyable to the audience, and attract brand sponsors. 
    Please provide a script for content related to {content_ideas}, along with relevant hashtags for {', '.join(platforms)}. 
    Include funny lines or jokes that would make the content more engaging and shareable.
    """
    
    with st.spinner("Processing"):
        response = content_creation_agent.run(user_query)
    
    st.write(response.content)
