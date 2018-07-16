import os

# each website you crawl will be saved in a seperate project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + 'queue.txt' #list of links waiting to be crawled
    crawled = project_name + 'crawled.txt' #list of links that already crawled
    if not os.path.isfile(queue):
        write_file(queue, base_url) #start crawling from base
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create new File
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()