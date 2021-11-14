### Simple Dialogflow API

Use this API to get your Dialogflow's agent response without using any JSON service account file.  
This is useful in systems where you don't have access to upload this kind of files, like in ManyChat.  

Just send a POST request to the root of the API with the following body payload format:
```text
{
    "project_id": "tests-dfre",
    "agent_id": "d6d0ab34-ae52-4e39-b903-a5c2b1aec38b",
    "session_id": "user-001",
    "language": "en",
    "context": "",
    "text": "Hello"
}
```
That payload data is just that, an example for you to see how you can use it.  
<br>

#### Dialogflow info  
Go to your Dialogflow agent's settings and grab your Project ID:
![](https://zappa-rapidapi-dialogflow.s3.amazonaws.com/01.jpg)

Then go to Integrations - Web Demo:
![](https://zappa-rapidapi-dialogflow.s3.amazonaws.com/02.jpg)

Copy the ID at the end of the URL and enable the Web Demo:
![](https://zappa-rapidapi-dialogflow.s3.amazonaws.com/03.jpg)

Use that ID as your __agent_id__ in the API call.  

Set the __language__ you want to use (default to __en__) and send the __context__ if any for a better understanding.

<br>
<br>

#### About this project

This project was created by:
<br>
__Daian Gan__<br>
Github: [daiangan](https://github.com/daiangan)<br>
E-mail: daian@ganmedia.com<br>
Website: https://daiangan.com<br>