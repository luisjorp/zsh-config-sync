# Zsh Configuration Backup Tool

Welcome to the Zsh Configuration Backup Tool! This CLI tool is designed to make it easy for you to back up and restore your Zsh configuration files using GitHub. Whether you're moving to a new machine or just want to ensure your setup is safely backed up, this tool has got you covered.

## Features

- **Easy Backup**: Quickly compress and upload your Zsh configuration files to GitHub.
- **Seamless Restore**: Download and decompress your configuration files from GitHub with a simple command.
- **Safe Updates**: Automatically back up existing configuration files locally before overwriting them during restoration.
- **Flexible Configuration**: Supports both environment variables and `config.ini` for your GitHub token.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Git (for cloning this repository)
- A GitHub account and a personal access token with repo access

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/zsh-config-backup-tool.git
   cd zsh-config-backup-tool

2. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   
3. **Install the Required Packages**

   ```bash
    pip install -r requirements.txt
   
4. **Set Up Your GitHub Token**
    
   You can set your GitHub token using either environment variables or a `.env` file. The tool will look for environment variables first.

   - **Environment Variables**: Set the following environment variables with your GitHub token:

     ```bash
     export GITHUB_TOKEN=yourtoken
     ```

   - **`.env` File**: Create a `.env` file in the root directory of the repository with the following content:

     ```bash
     GITHUB_TOKEN=yourtoken
     ```

## Usage

The Zsh Configuration Backup Tool supports the following commands:

- `init`: Initializes the tool by creating a new repository on your GitHub account and adding the remote to the local repository.
- `backup`: Compresses and uploads your Zsh configuration files to GitHub.
- `restore`: Downloads and decompresses your Zsh configuration files from GitHub.
- `help`: Displays the help message.


### Init

Before you can use the backup and restore commands, you need to initialize the tool to authenticate with your GitHub account. You can do this by running the following command:

```bash
python main.py init
```

### Backup

To back up your Zsh configuration files, run the following command:

```bash
python main.py backup
```

### Restore

To restore your Zsh configuration files, run the following command:

```bash
python main.py restore
```

Take into account that if you already have a `.zshrc` file in your home directory, the tool will back it up renaming it to `.zshrc-local_backup` before restoring the new one.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any ideas, bug fixes, or changes you'd like to contribute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.