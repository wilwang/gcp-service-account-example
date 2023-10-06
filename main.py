from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'creds/<name of your service account key>.json'

generation_model = TextGenerationModel.from_pretrained("text-bison@latest")

PROJECT_ID = "<PROJECT ID>"
LOCATION = "<REGION>"

import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)

txt = generation_model.predict("""
Why is the sky blue?
""")

print(txt)