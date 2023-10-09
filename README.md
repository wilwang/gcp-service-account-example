# Authenticating with Service Account Keys

**Disclaimer:** *Using service account keys should be viewed as a last resort*

Service account keys could pose a security risk if compromised. We recommend you avoid downloading service account keys and instead attach service accounts through IAM or Workload Identity. 

https://cloud.google.com/blog/products/identity-security/how-to-authenticate-service-accounts-to-help-keep-applications-secure

## VertexAI SDK requires setting the quota project id

Reference: https://github.com/googleapis/python-aiplatform/issues/2557#issuecomment-1709284744

When you have a service account from a different project, you must set the `quota_project_id` to the project where the Vertex API is enabled

The service account must be granted in IAM these roles:
* Vertex AI User
* Service Usage Consumer

```
creds, _ = google.auth.load_credentials_from_file(
    filename='./creds/<service account key file>.json', 
    quota_project_id=PROJECT_ID)

vertexai.init(
    project=PROJECT_ID, 
    location=LOCATION, 
    credentials=creds)    
```

# Set up virtualenv
```
python -m venv .venv
source .venv/bin/activate
```

# Install dependencies
```
pip install -r requirements.txt
```

# *(NOT RECOMMENDED)*, demo purposes only!
- Create a folder called 'creds'
- Create a service account in IAM
- Create a service account key and download and save into the 'creds' folder
  - this will be referenced in the code

# Run code
```
python main.py
```