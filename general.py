import os

# each website you crawl will be saved in a seperate project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating directory ' + directory)
        os.makedirs(directory)