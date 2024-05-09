import requests
import json

url= "http://localhost:11434/api/generate"

headers= {
    "Content-type" : "application/json"
}

data= {
    "model" : "llama3",
    "prompt" : "frame 5 questions from the following content: Sections 41 to 54 of the Maharashtra Land Revenue Code, 1966 (Mah. XLI of 1966) provide for the regulation of use of lands. Section 42 of the said Code provides for permission of the Collector for non-agricultural use of lands.",
    "stream" : False
}

response= requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code==200:
    response_text=response.text
    data=json.loads(response_text)
    actual_response=data['response']
    print(actual_response)
else:
    print("Error:", response.status_code, response.text)