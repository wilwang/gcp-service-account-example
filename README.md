# Authenticating with Service Account Keys

**Disclaimer:** *Using service account keys should be viewed as a last resort*

Service account keys could pose a security risk if compromised. We recommend you avoid downloading service account keys and instead attach service accounts through IAM or Workload Identity. 

https://cloud.google.com/blog/products/identity-security/how-to-authenticate-service-accounts-to-help-keep-applications-secure

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