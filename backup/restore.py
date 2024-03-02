import os
import zipfile
from github import Github
from auth.github_auth import get_github_client


def download_backup(filename, repository_name):
    """Download the backup file from GitHub, returning success status."""
    client = get_github_client()
    repo = client.get_repo(repository_name)

    try:
        contents = repo.get_contents(f"backups/{filename}")
        file_content = contents.decoded_content
        with open(filename, 'wb') as file:
            file.write(file_content)
        print(f"Downloaded {filename} successfully.")
        return True  # Indicate success
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
        return False  # Indicate failure


def decompress_configs(input_filename):
    """Decompress the Zsh configuration files, backing up any existing files."""
    with zipfile.ZipFile(input_filename, 'r') as zipf:
        for member in zipf.infolist():
            target_path = os.path.expanduser(f"~/{member.filename}")
            backup_path = f"{target_path}-local_backup"

            # Check if the file exists and back it up
            if os.path.exists(target_path):
                os.rename(target_path, backup_path)
                print(f"Backed up existing file to {backup_path}")

            zipf.extract(member, path=os.path.expanduser('~'))
        print(f"Extracted {input_filename} successfully.")


def restore_configs():
    # Define the name of the backup file and the GitHub repository
    filename = 'zsh_config_backup.zip'  # The name of the backup file
    repository_name = 'luisjorp/zsh-file'  # Your GitHub repository

    success = download_backup(filename, repository_name)
    if success:
        # Decompress the configuration files
        decompress_configs(filename)
        return "Restore completed successfully."
    else:
        # Attempt to restore from local backup if download fails
        try:
            local_backup_filename = f"{filename}-local_backup"
            decompress_configs(local_backup_filename)
            return "Restored from local backup successfully."
        except Exception as e:
            # echo(f"Error during restoration from local backup: {e}")
            return f"Error during restoration from local backup: {e}"


# Example usage
if __name__ == '__main__':
    filename = 'zsh_config_backup.zip'
    repository_name = 'luisjorp/zsh-file'  # Your GitHub repository
    # Download the backup file from GitHub
    download_backup(filename, repository_name)
    # Decompress the configuration files
    decompress_configs(filename)
