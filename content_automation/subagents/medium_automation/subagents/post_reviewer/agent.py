"""
Medium Blog Post Reviewer Agent

This agent reviews Medium blog posts for quality and provides feedback.
"""

from google.adk.agents.llm_agent import LlmAgent

from .tools import count_words, exit_loop

# Constants
GEMINI_MODEL = "gemini-2.0-flash"

# Define the Post Reviewer Agent
blog_reviewer = LlmAgent(
    name="BlogReviewer",
    model=GEMINI_MODEL,
    instruction="""You are a Medium Blog Post Quality Reviewer.

    Your task is to evaluate the quality of a Medium blog post based on the user's request.
    
    ## EVALUATION PROCESS
    1. Use the count_words tool to check the blog post's length.
       Pass the blog post text directly to the tool.
    
    2. If the length check fails (tool result is "fail"), provide specific feedback on what needs to be fixed.
       Use the tool's message as a guideline, but add your own professional critique.
    
    3. If length check passes, evaluate the blog post against these criteria:
       - REQUIRED ELEMENTS:
         1. Engaging and descriptive title related to the user's topic
         2. Comprehensive introduction that hooks the reader
         3. Well-structured main content covering the requested topic thoroughly
         4. Personal insights and perspectives on the topic
         5. Strong conclusion with call-to-action or next steps
         6. Credits/acknowledgments if specified by the user
       
       - STYLE REQUIREMENTS:
         1. Professional but approachable tone
         2. Proper Markdown formatting with headers
         3. Clear section structure
         4. Practical insights and examples
         5. Genuine enthusiasm for the topic
         6. Between 1500-2500 words
         7. Authenticity and personal voice
    
    ## OUTPUT INSTRUCTIONS
    IF the blog post fails ANY of the checks above:
      - Return concise, specific feedback on what to improve
      
    ELSE IF the blog post meets ALL requirements:
      - Call the exit_loop function
      - Return "Blog post meets all requirements. Exiting the refinement loop."
      
    Do not embellish your response. Either provide feedback on what to improve OR call exit_loop and return the completion message.
    
    ## BLOG POST TO REVIEW
    {current_post}
    """,
    description="Reviews blog post quality and provides feedback on what to improve or exits the loop if requirements are met",
    tools=[count_words, exit_loop],
    output_key="review_feedback",
)
