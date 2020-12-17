import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
import numpy as np
import pandas as pd

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelWithLMHead


model = AutoModelWithLMHead.from_pretrained("models/ach-en-model")
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-luo-en", use_fast=False)


device = 'cpu'
if torch.cuda.is_available(): #check if GPU device is available
    device = 'cuda' # assign the gpu to the device



def return_results(data):
	tokens=tokenizer.prepare_seq2seq_batch([data],padding=True,truncation=True, return_tensors="pt" )

	tokens.to(device)
	model.to(device)
	translated = model.generate(**tokens)
	tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
	result=tgt_text[0]

	return result