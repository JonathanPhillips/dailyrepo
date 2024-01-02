import os
import datetime
from git import Repo

# Path to your local git repository
repo_path = 'GithubProjects/dailyrepo'
repo = Repo(repo_path)

# Function to create a new file with the current date
def create_file_with_date(repo_path):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(repo_path, f'{date_str}.txt')
    with open(file_path, 'w') as file:
        file.write(f'File created on {date_str}\n')
    return file_path

# Function to commit and push changes
def commit_and_push(repo, file_path, message):
    repo.git.add(file_path)
    repo.git.commit(m=message)
    repo.git.push()

# Create a new file
new_file_path = create_file_with_date(repo_path)

# Commit and push the file
commit_message = f'Add file for {datetime.datetime.now().strftime("%Y-%m-%d")}'
commit_and_push(repo, new_file_path, commit_message)

print("New file committed and pushed to GitHub.")
