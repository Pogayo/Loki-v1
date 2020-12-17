import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
import numpy as np
import pandas as pd

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelWithLMHead


device = 'cpu'
if torch.cuda.is_available(): #check if GPU device is available
    device = 'cuda' # assign the gpu to the device

model_en= AutoModelWithLMHead.from_pretrained("models/en-ach-model")
tokenizer_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-luo", use_fast=False)

model_ach = AutoModelWithLMHead.from_pretrained("models/ach-en-model")
tokenizer_ach = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-luo-en", use_fast=False)



def return_results(data, source):

	if source=="en":
		model = model_en
		tokenizer = tokenizer_en
	else:
		model = model_ach
		tokenizer = tokenizer_ach
		

	tokens=tokenizer.prepare_seq2seq_batch([data],padding=True,truncation=True, return_tensors="pt" )

	tokens.to(device)
	model.to(device)
	translated = model.generate(**tokens)
	tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
	result=tgt_text[0]

	return result