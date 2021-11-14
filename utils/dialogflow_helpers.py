import json
from dataclasses import dataclass

import requests


@dataclass
class DialogFlowAPI:
    project_id: str
    agent_id: str
    base_url = 'https://dialogflow.cloud.google.com/v1/integrations/messenger/webhook'

    def detect_intent(self,
                      session_id: str,
                      text: str,
                      language_code: str = 'en',
                      context: str = None):

        response = lambda: None
        response.messages = []
        response.parameters = []

        data = {
            'queryInput': {
                'text': {
                    'text': text,
                    'languageCode': language_code,
                }
            },
        }

        if context:
            data['queryParams'] = {
                'contexts': [
                    {
                        'name': f'projects/{self.project_id}/agent/sessions/{session_id}/contexts/{context}',
                        'lifespanCount': 1,
                    }
                ]
            }

        df_response = requests.post(
            url=f'{self.base_url}/{self.agent_id}/sessions/{session_id}?platform=webdemo',
            data=json.dumps(data),
        )

        clean_response = df_response.text.replace(")]}'", "")

        results = json.loads(clean_response)
        # print(json.dumps(results, indent=4, sort_keys=True))

        return results
