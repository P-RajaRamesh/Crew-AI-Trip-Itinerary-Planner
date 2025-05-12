from crewai import Task
from agents import planner_agent,local_guide_agent

location_research_task = Task(
        description="""
            Research and provide comprehensive information about {location} as a tourist destination.
            The trip will take place during {start_date} to {end_date}.
            
            Your research should include:
            
            1. Overview of {location} - geography, culture, and best times to visit
            2. Top 15-20 attractions and activities in {location} and surrounding areas
            3. Information about local transportation options
            4. Typical costs for accommodation, food, transportation, and activities
            5. Weather forecast for the dates {start_date} to {end_date}
            6. Local cuisines and recommended restaurants
            7. Cultural customs and etiquette to be aware of
            8. Safety information and travel advisories if any
            9. Special events or festivals happening during {start_date} to {end_date}
            10. Insider tips that would enhance the experience
            
            Provide detailed information that would be valuable for planning a 7-day itinerary.
            The information will be used by an itinerary planner to create a comprehensive
            day-by-day plan, so include specific details about each attraction or activity,
            including estimated time needed, costs, and any special considerations.
        """,
        agent=local_guide_agent,
        expected_output="""
            A comprehensive guide to the specified location with all requested information
            organized in clear sections. Each attraction should include specific details
            about location, suggested duration of visit, approximate costs, and any special
            notes. The guide should be detailed and practical enough to be used as a
            reference for creating a personalized 7-day itinerary.
        """
    )

itinerary_planning_task = Task(
        description="""
            Create a detailed 7-day itinerary for a trip to {location} starting on {start_date}.
            Use the information provided by the local guide
            
            Your itinerary should include:
            
            1. Day-by-day schedule with specific activities and attractions
            2. Dining recommendations for each day
            3. Accommodation suggestions with approximate costs
            4. Transportation details between activities
            5. Estimated budget for each day and overall trip
            6. Practical tips for each day
            7. Alternative options for bad weather or closures
            
            Each day should be well-balanced with a mix of activities, adequate time for meals,
            and consideration for travel times between locations. Group activities by proximity
            to minimize travel time. Ensure the pace is reasonable, avoiding scheduling too many
            activities in a single day.
            
            The final itinerary should be presented as a comprehensive day-by-day plan that is
            ready to be followed by travelers, with all necessary details included.
        """,
        agent=planner_agent,
        expected_output="""
            A detailed 7-day itinerary organized by day, with each day containing:
            - Date
            - Morning activities with times, locations, costs
            - Lunch recommendation with location and price range
            - Afternoon activities with times, locations, costs
            - Dinner recommendation with location and price range
            - Evening activities (if applicable)
            - Accommodation for the night with price
            - Daily budget estimate
            - Practical tips for the day
            
            The itinerary should also include:
            - Total estimated budget breakdown
            - Packing recommendations
            - Important local emergency information
            - Alternative options for activities in case of bad weather
        """
    )


booking_recommendation_task=Task(
        description="""
            Based on the 7-day itinerary for {location} starting on {start_date},
            provide recommendations for what to book in advance and when to book.
            
            Review the itinerary and identify:
            
            1. Accommodations that should be booked ahead of time
            2. Transportation that requires advance booking
            3. Activities or attractions that need reservations
            4. Restaurants that may require reservations
            5. Recommended booking timeline for each item (e.g., 3 months in advance,
               1 week in advance, etc.)
            6. Estimated costs for bookings and total budget
            
            Organize your recommendations in a clear, prioritized format to help
            the traveler plan their bookings efficiently.
            
            Here is the complete itinerary for reference:
            
        """,
        agent=planner_agent,
        expected_output="""
            A comprehensive booking guide with:
            - Prioritized list of what to book in advance
            - Recommended booking timeline for each item
            - Estimated costs and booking fees
            - Links or references to booking platforms where available
            - Tips for getting the best rates
            - Cancellation policy recommendations
        """
    )
