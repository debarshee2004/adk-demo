"""
Content Automation Root Agent

This module defines the root agent for the content automation system.
It orchestrates LinkedIn, Twitter, and Medium content generation in parallel.
"""

from google.adk.agents import ParallelAgent

from .subagents.linkedin_automation.agent import (
    linkedin_content_agent as linkedin_agent,
)
from .subagents.twitter_automation.agent import twitter_content_agent as twitter_agent
from .subagents.medium_automation.agent import medium_content_agent as medium_agent

# Create the Parallel Content Generation Agent
root_agent = ParallelAgent(
    name="ContentAutomationPipeline",
    sub_agents=[
        # Generate content for all platforms simultaneously
        linkedin_agent,
        twitter_agent,
        medium_agent,
    ],
    description="Generates content for LinkedIn, Twitter, and Medium platforms simultaneously using parallel processing",
)
