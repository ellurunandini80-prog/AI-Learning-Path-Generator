from config import model
import requests

def generate_learning_path(goal):

    try:
        youtube_status = requests.get(
            "https://youtube.run.tools",
            timeout=5
        ).status_code
    except Exception:
        youtube_status = "Unavailable"

    try:
        drive_status = requests.get(
            "https://googledrive.run.tools",
            timeout=5
        ).status_code
    except Exception:
        drive_status = "Unavailable"

    try:
        notion_status = requests.get(
            "https://notion.run.tools",
            timeout=5
        ).status_code
    except Exception:
        notion_status = "Unavailable"

    prompt = f"""
    Create a detailed learning path for: {goal}

    MCP Status:
    YouTube MCP: {youtube_status}
    Google Drive MCP: {drive_status}
    Notion MCP: {notion_status}

    Include:
    1. Beginner topics
    2. Intermediate topics
    3. Advanced topics
    4. Recommended projects
    5. Estimated timeline
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"