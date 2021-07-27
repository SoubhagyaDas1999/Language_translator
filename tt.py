from googletrans import Translator
from tqdm import tqdm
import requests
import io

def translate_text(source, target, text):
	translator = Translator()
	translation = translator.translate(text, dest = target)
	return translation.text

path = "C:/Users/Soubhagya/Documents/#Work/Speech_Project/op_trans"

file = io.open(path+"/"+"en.txt", mode="w", encoding="UTF-16 LE")
f = io.open(path+"/"+"go_hi_op.txt", mode="r", encoding="UTF-16 LE")
a = f.read().splitlines()
f.close()

for lines in tqdm(a):
	result = translate_text('hi','en',lines)
	file.write(" "+result+"\n")
	#print(result+"\n")

file.close()	