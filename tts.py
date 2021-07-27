from gtts import gTTS
from tqdm import tqdm
import io
import os

path = "C:/Users/Soubhagya/Documents/#Work/Speech_Project/op_trans/"
dest = "C:/Users/Soubhagya/Documents/#Work/Speech_Project/op_trans/wavs_out/"

file = io.open(path+"/"+"en.txt", mode="r", encoding="UTF-16 LE")
a = file.read().splitlines()
file.close()
b = 0
for lines in tqdm(a):
	myobj = gTTS(text = lines, lang = 'en', slow = False)
	fi = "r"+"_"+str(b)+".mp3"
	myobj.save(dest+fi)
	b = b+1

cm = "type *.mp3>out.mp3"
os.system(cm)