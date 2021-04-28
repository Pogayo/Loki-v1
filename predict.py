# import torch
# from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForSeq2SeqLM
# import numpy as np
import predict_luo
import predict_acholi
import predict_adhola

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelWithLMHead


# device = 'cpu'
# if torch.cuda.is_available(): #check if GPU device is available
#     device = 'cuda' # assign the gpu to the device

# model_en_ach= AutoModelForSeq2SeqLM.from_pretrained("models/en-ach-model")
# tokenizer_en_ach = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-luo", use_fast=False)

# model_ach_en= AutoModelForSeq2SeqLM.from_pretrained("models/ach-en-model")
# tokenizer_ach_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-luo-en", use_fast=False)

# model_adh_en = AutoModelForSeq2SeqLM.from_pretrained("models/adh-en-model")
# tokenizer_adh_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-luo-en", use_fast=False)

# model_en_adh = AutoModelForSeq2SeqLM.from_pretrained("models/en-adh-model")
# tokenizer_en_adh = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-luo", use_fast=False)



def return_results(data, source, target):

	if source=="en" and target=="ach":
		# model = model_en_ach
		# tokenizer = tokenizer_en_ach
		return predict_acholi.to_ach(data)


	elif source=="ach" and target=="en":
		# model = model_ach_en
		# tokenizer = tokenizer_ach_en
		return predict_acholi.to_en(data)


	elif source=="adh" and target=="en":
		# model = model_adh_en
		# tokenizer = tokenizer_adh_en
		return predict_adhola.to_en(data)


	elif source=="en" and target=="adh":
		# model = model_en_adh
		# tokenizer = tokenizer_en_adh
		return predict_adhola.to_adh(data)


	elif source=="luo" and target=="en":
		return predict_luo.to_en(data)

	elif source=="en" and target=="luo":
		return predict_luo.to_luo(data)

	else:
		return ("Please select a valid combination. English - Luo, English - Acholi, English - Dhopadola, Luo - English, Acholi - English, Dhopadhola - English", -1)
		

	# tokens=tokenizer.prepare_seq2seq_batch([data],padding=True,truncation=True, return_tensors="pt" )

	# tokens.to(device)
	# model.to(device)
	# translated = model.generate(**tokens)
	# tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
	# result=tgt_text[0]

	# return result