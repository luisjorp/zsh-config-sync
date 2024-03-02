from github import Github
from dotenv import load_dotenv
import os

def get_github_client():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the GitHub token from an environment variable
    token = os.getenv('GITHUB_TOKEN')

    if not token:
        raise EnvironmentError("GitHub token not found. Please ensure the GITHUB_TOKEN is set in the .env file.")

    # Create and return a Github instance using the token
    return Github(token)

# Example usage
if __name__ == "__main__":
    try:
        github_client = get_github_client()
        user = github_client.get_user()
        print(f"Authenticated as {user.login}")
    except Exception as e:
        print(f"Error: {e}")
