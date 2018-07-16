import os


# each website you crawl will be saved in a seperate project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'  # list of links waiting to be crawled
    crawled = project_name + '/crawled.txt'  # list of links that already crawled
    if not os.path.isfile(queue):
        write_file(queue, base_url)  # start crawling from baseURL
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create new File
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data to existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')  # stick a new link


# Delete Contents of the File
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a File and convert each line to Set Items
def file_to_set(file_name):
    results = set()  # using set to prevent duplications of items
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', '')) # add item to the set without the new line
    return results


# Iterate through a set, each item in the set will be a new line in a file
def set_to_file(links, file):
    delete_file_contents(file) # get rid of old data
    for link in sorted(links):
        append_to_file(file, link)

