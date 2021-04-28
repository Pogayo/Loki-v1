import json
import requests
import time
from time import sleep


# API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-luo"
headers = {"Authorization": f"Bearer api_sRfRskxxxNmTHoMGhTrdMRsXRYjqjdKEsF"}

adh_attempts=0
en_attempts=0

def query(payload, API_URL):
	data = json.dumps(payload)
	response = requests.request("POST", API_URL, headers=headers, data=data)
	return json.loads(response.content.decode("utf-8"))

def run_query(text, API_URL, attempts):

	inputs = {
        "inputs": text,
        "- wait_for_model": True

        }
	res = query(inputs, API_URL)
	# return type(res)
	if res and len(res)>0:
		if res[0].get('generated_text'):
			attempts=0 #return it to zero for the next request
			return res[0].get('generated_text')
		else:
			sleep(20)
			attempts = attempts + 1
	        
			if attempts < 4:
				run_query(inputs, API_URL, attempts)
			else:
				return "Attempts maxxed out. Please try again later"


def to_en(text):
	return run_query(text, "https://api-inference.huggingface.co/models/Ogayo/mt-adh-en", en_attempts)
	


def to_adh(text):
	return run_query(text, "https://api-inference.huggingface.co/models/Ogayo/mt-en-adh", adh_attempts)