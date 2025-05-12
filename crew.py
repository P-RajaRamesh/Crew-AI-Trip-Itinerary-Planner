from crewai import Crew,Process
from agents import local_guide_agent,planner_agent
from tasks import booking_recommendation_task,itinerary_planning_task,location_research_task


crew = Crew(
  agents=[local_guide_agent, planner_agent],
  tasks=[booking_recommendation_task,itinerary_planning_task,location_research_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True,
  embedder={
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        }
 }
)


result=crew.kickoff(inputs={
    'location':'Vizag',
    'start_date' : '1st June 2025',
    'end_date' : '8th June 2025'
})
print(result)
with open("my-itinerary.md", "w", encoding="utf-8") as file:
    file.write(str(result))

# Open the file and read its content
with open("my-itinerary.md", "r", encoding="utf-8") as file:
    content = file.read()

# Remove specific characters
content = content.replace("`", "")

# Save the modified content back to the file
with open("my-itinerary.md", "w", encoding="utf-8") as file:
    file.write(content)
