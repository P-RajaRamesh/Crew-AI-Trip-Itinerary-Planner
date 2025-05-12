from crewai import Agent, LLM
# from langchain_groq import ChatGroq
from tools import search

import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('GEMINI_API_KEY')

llm = LLM(
    model="gemini/gemini-2.0-flash",  
    api_key=api_key,
    temperature=0.5
)

local_guide_agent=Agent(
    role='Local Travel Guide Expert',
    goal='Provide detailed and accurate information about tourist destinations {location}',
    verboe=True,
    memory=True,
    backstory=(
       "You are an experienced local travel guide with extensive knowledge about "
        "various tourist destinations worldwide. You have spent years exploring different "
        "cities, understanding their culture, attractions, local customs, transportation, "
        "and insider tips. Your expertise helps travelers experience authentic and memorable "
        "journeys with practical advice that goes beyond typical tourist information." 
    ),
    tools=[search],
    llm=llm,
    allow_delegation=True
)


planner_agent=Agent(
    role='Travel Itinerary Planning Specialist',
    goal='Create comprehensive and personalized 7-day travel itineraries for {location}',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert travel itinerary planner with years of experience in the tourism "
        "industry. You have planned thousands of successful trips for clients with diverse "
        "preferences and requirements. Your specialty is creating balanced itineraries that "
        "maximize experiences while keeping logistics practical and within budget. You know "
        "how to sequence activities optimally, account for travel times, and include appropriate "
        "rest periods. Your itineraries always include detailed cost estimates for accommodations, "
        "transportation, activities, meals, and other expenses."
    ),
    tools=[search],
    llm=llm,
    allow_delegation=True
)