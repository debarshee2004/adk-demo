"""
Medium Blog Post Generator Root Agent

This module defines the root agent for the Medium blog post generation application.
It uses a sequential agent with an initial post generator followed by a refinement loop.
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .subagents.post_generator.agent import initial_blog_generator
from .subagents.post_refiner.agent import blog_refiner
from .subagents.post_reviewer.agent import blog_reviewer

# Create the Refinement Loop Agent
refinement_loop = LoopAgent(
    name="BlogRefinementLoop",
    max_iterations=10,
    sub_agents=[
        blog_reviewer,
        blog_refiner,
    ],
    description="Iteratively reviews and refines a Medium blog post until quality requirements are met",
)

# Create the Sequential Pipeline
medium_content_agent = SequentialAgent(
    name="MediumBlogGenerationPipeline",
    sub_agents=[
        # Step 1: Generate initial blog post
        initial_blog_generator,
        # Step 2: Review and refine in a loop
        refinement_loop,
    ],
    description="Generates and refines a Medium blog post through an iterative review process",
)
