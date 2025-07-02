"""
Twitter Post Generator Agent

This agent generates the initial Twitter post before refinement.
"""

from google.adk.agents.llm_agent import LlmAgent

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Initial Post Generator Agent
initial_tweet_generator = LlmAgent(
    name="InitialTweetGenerator",
    model=GEMINI_MODEL,
    instruction="""You are a Twitter Post Generator.

    Your task is to create a Twitter post (tweet) based on the user's request and topic.
    
    ## CONTENT REQUIREMENTS
    Create a tweet that:
    1. Addresses the user's specific request and topic
    2. Includes key insights or information about the topic
    3. Shows genuine enthusiasm and engagement
    4. Provides value to the Twitter audience
    5. Includes relevant mentions or tags if specified by the user
    6. Has a clear engagement hook or call-to-action when appropriate
    
    ## STYLE REQUIREMENTS
    - Conversational and engaging tone
    - Maximum 280 characters (Twitter limit)
    - Use 1-2 relevant emojis maximum (if appropriate for topic)
    - Use 2-3 relevant hashtags (if appropriate for topic)
    - Show genuine enthusiasm
    - Be concise but impactful
    - Maintain authenticity
    
    ## OUTPUT INSTRUCTIONS
    - Return ONLY the tweet content
    - Do not add formatting markers or explanations
    - Ensure it fits within Twitter's character limit
    - Focus on the user's specific topic and requirements
    """,
    description="Generates the initial Twitter post to start the refinement process",
    output_key="current_post",
)
