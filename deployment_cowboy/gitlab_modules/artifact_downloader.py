import requests
import json
import subprocess
from keys import API_KEY


base_url = 'https://gitlab.com/api/v4/projects/39946816/jobs/'

headers = {
    'PRIVATE-TOKEN': API_KEY
}

#get job id 
r = requests.get(base_url, headers=headers)
responce_data = json.loads(r.content)
post_id = responce_data[0]['id']
artifact_url = f"{base_url}{post_id}/artifacts"

# Get files 
r = requests.get(artifact_url, headers=headers)
print(r.status_code)
open('archive.zip', 'wb').write(r.content)

subprocess.run(["scripts/process_archive.sh"])
