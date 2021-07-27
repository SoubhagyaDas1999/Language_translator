import glob
import speech_recognition as sr
from tqdm import tqdm
import io

r = sr.Recognizer()

audio_path = 'C:/Users/Soubhagya/Documents/#Work/Speech_Project/wavs/'
op_trans_path = 'C:/Users/Soubhagya/Documents/#Work/Speech_Project/op_trans/'

lang_id = 'hi-IN'

wavs = glob.glob(audio_path+"*.wav")

wavs.sort()

#file = open(op_trans_path+"/"+"go_hi_op.txt","w")
file = io.open(op_trans_path+"go_hi_op.txt", mode="w", encoding="UTF-16 LE")


for x in tqdm(range(0, len(wavs))):
	AUDIO_FILE = (wavs[x])

	try:
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)
		text = r.recognize_google(audio,language=lang_id)
		file.write(AUDIO_FILE.split('f_')[-1].strip(".wav")+" : "+text+"\n")
		#print(AUDIO_FILE.split('f_')[-1].strip(".wav")+" : "+text)
	except:
		file.write(AUDIO_FILE.split('f_')[-1].strip(".wav")+" : "+"ERROR in Transcription"+"\n")
		#print(AUDIO_FILE.split('f_')[-1].strip(".wav")+" : "+"ERROR in Transcription")

file.close()