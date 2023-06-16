import nntplib
import shutil
import tarfile
import os

# Configuration
newsgroup_server = os.getenv('NNTP_SERVER')
newsgroup_name = 'bit.listserv.ibm-main'
output_directory = 'ibm-main'

# Connect to the newsgroup server
server = nntplib.NNTP(newsgroup_server)

server.login(os.getenv('NNTP_LOGIN'), os.getenv('NNTP_PASSWORD'))

# Get the group information
resp, count, first, last, name = server.group(newsgroup_name)

# Remove output directory if it exists
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download and save the articles
for i in range(int(first), int(last) + 1):
    try:
        resp, info = server.article(str(i))
        file_path = os.path.join(output_directory, i + '.txt')

        with open(file_path, 'w', encoding='utf-8') as f:
            for line in info.lines:
                f.write(line.decode('utf-8', errors='ignore') + '\n')
        print(f'Downloaded and saved article {i} with Message-ID: {info.message_id}')
    except nntplib.NNTPTemporaryError as e:
        print(f'Error downloading article {i}: {e}')

# Close the server connection
server.quit()

# Create a tar.gz archive
with tarfile.open(archive_name, 'w:gz') as tar:
    tar.add(output_directory)

print(f'Archive created: {archive_name}')
