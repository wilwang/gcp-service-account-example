import google
import vertexai

PROJECT_ID = "<PROJECT_ID>"
LOCATION = "<REGION>"

# need to set the quota_project_id (https://github.com/googleapis/python-aiplatform/issues/2557#issuecomment-1709284744)
creds, _ = google.auth.load_credentials_from_file(
    filename='./creds/<service account key file>.json', 
    quota_project_id=PROJECT_ID)

vertexai.init(
    project=PROJECT_ID, 
    location=LOCATION, 
    credentials=creds)

from vertexai.preview.language_models import TextGenerationModel

generation_model = TextGenerationModel.from_pretrained("text-bison@latest")
txt = generation_model.predict("""Why is the sky blue?""")

print(txt)