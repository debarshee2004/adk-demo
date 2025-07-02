"""
Twitter Post Generator Root Agent

This module defines the root agent for the Twitter post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .subagents.post_generator.agent import initial_tweet_generator
from .subagents.post_refiner.agent import tweet_refiner
from .subagents.post_reviewer.agent import tweet_reviewer

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="TweetRefinementLoop",
    max_iterations=10,
    sub_agents=[
        tweet_reviewer,
        tweet_refiner,
    ],
    description="Iteratively reviews and refines a Twitter post until quality requirements are met",
)

# Create the Sequential Pipeline
twitter_content_agent = SequentialAgent(
    name="TwitterPostGenerationPipeline",
    sub_agents=[
        # Step 1: Generate initial tweet
        initial_tweet_generator,
        # Step 2: Review and refine in a loop
        refinement_loop,
    ],
    description="Generates and refines a Twitter post through an iterative review process",
)
