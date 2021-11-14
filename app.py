from flask import Flask, request

from utils import dialogflow_helpers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        request_data = request.get_json()
        response = {
            'ok': True,
            'message': 'Everything ok.',
            'dialogflow_response': None,
        }

        session_id = request_data.get('session_id')
        if not session_id:
            response['ok'] = False
            response['message'] = 'Please send me the session_id'
            return response

        project_id = request_data.get('project_id')
        if not project_id:
            response['ok'] = False
            response['message'] = 'Please send me the project_id'
            return response

        agent_id = request_data.get('agent_id')
        if not agent_id:
            response['ok'] = False
            response['message'] = 'Please send me the agent_id'
            return response

        language = request_data.get('language', 'en')
        context = request_data.get('context', '')
        input_text = request_data.get('text')

        df = dialogflow_helpers.DialogFlowAPI(
            project_id=project_id,
            agent_id=agent_id,
        )

        dialogflow_response = df.detect_intent(
            session_id=session_id,
            text=input_text,
            language_code=language,
            context=context if context != '' else None
        )

        if 'error' in dialogflow_response:
            response['ok'] = False
            response['message'] = dialogflow_response['error']['message']

        response['dialogflow_response'] = dialogflow_response

        return response

    else:
        return 'Welcome to Dialogflow API!'


if __name__ == '__main__':
    app.run()
