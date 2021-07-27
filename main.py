import os

def main():
	print("Starting Process..........")
	path = "C:/Users/Soubhagya/Documents/#Work/Speech_Project/prog_files"
	os.chdir(path)

	cmd1 = "python asr.py"
	print("Converting Speech to Text!")
	os.system(cmd1)

	cmd2 = "python tt.py"
	print("Converting to a new Language!")
	os.system(cmd2)

	cmd3 = "python tts.py"
	print("Getting the Speech Raedy!")
	os.system(cmd3)


if __name__ == "__main__":
		main()
		print("Job Done!")