import json
import requests
import time

# API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-luo"
headers = {"Authorization": f"Bearer api_sRfRskxxxNmTHoMGhTrdMRsXRYjqjdKEsF"}

luo_attempts=0
en_attempts=0

def query(payload, API_URL):
	data = json.dumps(payload)
	response = requests.request("POST", API_URL, headers=headers, data=data)
	return json.loads(response.content.decode("utf-8"))

def run_query(text, API_URL, attempts):

	inputs = {
        "inputs": text
        }
	res = query(inputs, API_URL)
	if res[0].get('translation_text'):
		attempts=0 #return it to zero for the next request
		return res[0].get('translation_text')
	else:
		sleep(20)
		attempts = attempts + 1
        
		if attempts < 4:
			run_query(inputs, API_URL)
		else:
			return "Attempts maxxed out. Please try again later"


def to_en(text):
	return run_query(text, "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-luo-en", en_attempts)
	


def to_luo(text):
	return run_query(text, "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-luo", luo_attempts)