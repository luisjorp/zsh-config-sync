import click
from auth.github_auth import get_github_client
from backup.backup import backup_configs
from backup.restore import restore_configs


# from backup.restore import restore_configs

# Create a Click group (this decorator is used to create a group of commands)
@click.group()
def cli():
    """Zsh Configuration Backup Tool"""
    pass


# Command to initialize the tool by authenticating with GitHub
@cli.command(help='Initialize the tool by authenticating with GitHub.')
def init():
    client = get_github_client()
    user = client.get_user()
    click.echo(f"Authenticated as {user.login}")


# Command to back up the Zsh configuration files
@cli.command(help='Backup your Zsh configurations to GitHub.')
def backup():
    # Placeholder for the backup function
    click.echo("Backing up configurations...")
    backup_configs()



# Command to restore the Zsh configuration files
@cli.command(help='Restore your Zsh configurations from GitHub.')
def restore():
    # Placeholder for the restore function
    click.echo("Restoring configurations...")
    restore_configs()


# Add commands to the CLI group
cli.add_command(init)
cli.add_command(backup)
cli.add_command(restore)


# Run the CLI
if __name__ == "__main__":
    cli()
