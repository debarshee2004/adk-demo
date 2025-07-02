"""
Tools for Twitter Post Reviewer Agent

This module provides tools for analyzing and validating Twitter posts.
"""

from typing import Any, Dict

from google.adk.tools.tool_context import ToolContext


def count_characters(text: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Tool to count characters in the provided text and provide length-based feedback for Twitter.
    Updates review_status in the state based on length requirements.

    Args:
        text: The text to analyze for character count
        tool_context: Context for accessing and updating session state

    Returns:
        Dict[str, Any]: Dictionary containing:
            - result: 'fail' or 'pass'
            - char_count: number of characters in text
            - message: feedback message about the length
    """
    char_count = len(text)
    MAX_LENGTH = 280  # Twitter character limit

    print("\n----------- TOOL DEBUG -----------")
    print(f"Checking tweet length: {char_count} characters")
    print("----------------------------------\n")

    if char_count > MAX_LENGTH:
        chars_to_remove = char_count - MAX_LENGTH
        tool_context.state["review_status"] = "fail"
        return {
            "result": "fail",
            "char_count": char_count,
            "chars_to_remove": chars_to_remove,
            "message": f"Tweet is too long. Remove {chars_to_remove} characters to meet Twitter's {MAX_LENGTH} character limit.",
        }
    else:
        tool_context.state["review_status"] = "pass"
        return {
            "result": "pass",
            "char_count": char_count,
            "message": f"Tweet length is good ({char_count} characters).",
        }


def exit_loop(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Call this function ONLY when the tweet meets all quality requirements,
    signaling the iterative process should end.

    Args:
        tool_context: Context for tool execution

    Returns:
        Empty dictionary
    """
    print("\n----------- EXIT LOOP TRIGGERED -----------")
    print("Tweet review completed successfully")
    print("Loop will exit now")
    print("------------------------------------------\n")

    tool_context.actions.escalate = True
    return {}
