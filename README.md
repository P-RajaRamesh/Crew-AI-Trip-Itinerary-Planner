# Crew-AI-Trip-Itinerary-Planner
A powerful trip planning application built with Crew AI and LangChain that creates personalized 7-day travel itineraries with the help of agentic AI.

## Features

- **AI-Powered Itinerary Creation**: Leverages Google Gemini models through Crew AI to create comprehensive travel plans
- **Local Guide Agent**: Provides detailed destination information including attractions, local customs, transportation options, and insider tips
- **Itinerary Planner Agent**: Creates day-by-day schedules with activities, restaurants, accommodations, and budget estimates
- **Comprehensive Output**: Complete with destination guide, 7-day itinerary, and booking recommendations

## Project Structure

```
├── agents.py             # Definition of AI agents (Local Guide and Itinerary Planner)
├── tasks.py              # Tasks assigned to agents
├── tools.py              # Tools used by agents (web search, location info, etc.)
├── crew.py               # Crew AI configuration and orchestration
├── requirements.txt      # Python dependencies
└── .env.example          # Example environment variables file
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/P-RajaRamesh/Crew-AI-Trip-Itinerary-Planner.git
   cd Crew-AI-Trip-Itinerary-Planner
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file to add your API keys.

## Required API Keys

- **Google Gemini API Key**: Required for the AI models
  - Get one at: https://makersuite.google.com/app/apikey
- **SerpAPI Key**: Optional but recommended for better search results
  - Get one at: https://serpapi.com/

## Usage

Currently user inputs are hard coded in crew.py file. So simply run: python crew.py
But you can modify them by implementing streamlit for better user experience and dynamic inputs.

## How It Works

1. **User Input**: The user provides a destination and start and end dates through the Streamlit interface.

2. **Local Guide Research**: The Local Guide agent researches the destination using various tools including web search, location information lookup, attraction information gathering, and more.

3. **Itinerary Planning**: The Itinerary Planner agent uses the information from the Local Guide to create a day-by-day itinerary with specific activities, dining recommendations, accommodations, and cost estimates.

4. **Booking Recommendations**: The Itinerary Planner agent also provides recommendations for what to book in advance and when to make those bookings.

5. **Results Display**: The complete trip plan is displayed in an organized, user-friendly format and downlaoded in .md format.

## Customization

You can customize various aspects of the trip planning process:

- Modify the agent instructions in `agents.py` to change their expertise and focus
- Add or modify tools in `tools.py` to provide different information sources
- Adjust task parameters in `tasks.py` to change what information is collected and how itineraries are structured

## License

This project is released under the MIT License.

## Acknowledgments

- [Crew AI](https://github.com/joaomdmoura/crewAI)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Google Gemini](https://deepmind.google/technologies/gemini/)

