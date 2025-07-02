"""
Tools for Medium Blog Post Reviewer Agent

This module provides tools for analyzing and validating Medium blog posts.
"""

from typing import Any, Dict

from google.adk.tools.tool_context import ToolContext


def count_words(text: str, tool_context: ToolContext) -> Dict[str, Any]:
    """
    Tool to count words in the provided text and provide length-based feedback for Medium.
    Updates review_status in the state based on length requirements.

    Args:
        text: The text to analyze for word count
        tool_context: Context for accessing and updating session state

    Returns:
        Dict[str, Any]: Dictionary containing:
            - result: 'fail' or 'pass'
            - word_count: number of words in text
            - message: feedback message about the length
    """
    word_count = len(text.split())
    MIN_LENGTH = 1500
    MAX_LENGTH = 2500

    print("\n----------- TOOL DEBUG -----------")
    print(f"Checking blog post length: {word_count} words")
    print("----------------------------------\n")

    if word_count < MIN_LENGTH:
        words_needed = MIN_LENGTH - word_count
        tool_context.state["review_status"] = "fail"
        return {
            "result": "fail",
            "word_count": word_count,
            "words_needed": words_needed,
            "message": f"Blog post is too short. Add {words_needed} more words to reach minimum length of {MIN_LENGTH}.",
        }
    elif word_count > MAX_LENGTH:
        words_to_remove = word_count - MAX_LENGTH
        tool_context.state["review_status"] = "fail"
        return {
            "result": "fail",
            "word_count": word_count,
            "words_to_remove": words_to_remove,
            "message": f"Blog post is too long. Remove {words_to_remove} words to meet maximum length of {MAX_LENGTH}.",
        }
    else:
        tool_context.state["review_status"] = "pass"
        return {
            "result": "pass",
            "word_count": word_count,
            "message": f"Blog post length is good ({word_count} words).",
        }


def exit_loop(tool_context: ToolContext) -> Dict[str, Any]:
    """
    Call this function ONLY when the blog post meets all quality requirements,
    signaling the iterative process should end.

    Args:
        tool_context: Context for tool execution

    Returns:
        Empty dictionary
    """
    print("\n----------- EXIT LOOP TRIGGERED -----------")
    print("Blog post review completed successfully")
    print("Loop will exit now")
    print("------------------------------------------\n")

    tool_context.actions.escalate = True
    return {}
