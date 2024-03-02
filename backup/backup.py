import os
import zipfile

from github import GithubException

from auth.github_auth import get_github_client


def compress_configs(config_paths_list, output_filename='zsh_config_backup.zip'):
    """Compress the Zsh configuration files."""
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for file_path in config_paths_list:
            expanded_path = os.path.expanduser(file_path)  # Expand the user home directory path
            if os.path.exists(expanded_path):
                zipf.write(expanded_path, os.path.basename(expanded_path))
            else:
                print(f"Warning: {expanded_path} does not exist and will not be included in the backup.")


def upload_to_github(filename, repository_name, commit_message):
    """Upload the compressed file to a GitHub repository."""
    client = get_github_client()
    repo = client.get_repo(repository_name)
    with open(filename, 'rb') as file:
        content = file.read()

    # Here, a new release is created or commit directly to the repo
    # This example commits the file directly to the root of the repository
    git_file = f"backups/{filename}"
    try:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, commit_message, content, contents.sha)
        print(f"Updated existing file: {filename}")
    except GithubException:
        try:
            repo.create_file(git_file, commit_message, content)
            print(f"Created new file: {filename}")
        except GithubException as e:
            print(f"Error during upload: {e}")
            return f"Error during upload: {e}"


def backup_configs():
    # Define the paths to your Zsh configuration files
    config_paths_list = ['~/.zshrc', '~/.zshenv']  # Adjust as necessary
    output_filename = 'zsh_config_backup.zip'  # The name of the compressed file
    repository_name = 'luisjorp/zsh-file'  # Your GitHub repository
    commit_message = 'Backup Zsh configuration'  # Commit message for the upload

    # Compress the configuration files
    compress_configs(config_paths_list, output_filename)

    # Upload the compressed file to GitHub
    upload_to_github(output_filename, repository_name, commit_message)
    print("Backup process completed successfully.")


# Example usage
if __name__ == '__main__':
    # Define paths to the Zsh configuration files
    config_paths = ['~/.zshrc', '~/.zshenv']
    # Compress the configuration files
    compress_configs(config_paths)
    # Upload the compressed file to GitHub
    upload_to_github('zsh_config_backup.zip', 'luisjorp/zsh-file', 'Backup Zsh configuration')
