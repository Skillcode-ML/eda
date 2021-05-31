import PyPDF2
import fitz
import streamlit as st 
import pyttsx3


boolna = 0
onpage = 0

def main():
	onpage = 0
	type = [".txt",".pdf"]	
	choice = st.sidebar.selectbox("Select the type of file",type)

	if choice == '.txt':
		st.subheader("Reading text file")

		data = st.file_uploader("Upload a text file", type=["txt"])
		if data is not None:
			df = data.read()
			
			volume = st.slider('Volume',0,100,25,1)
			rate = st.slider('Rate',0,100,85,1)
			engine = pyttsx3.init()
			engine.setProperty('rate', rate)
			engine.setProperty('volume', volume)
			engine.say(text)
			engine.runAndWait()
			
				
		
	if choice == '.pdf':
		st.subheader("Reading pdf file")

		data = st.file_uploader("Upload a pdf file", type=["pdf"])
		if data is not None:
			pdfreader = PyPDF2.PdfFileReader(data)
			pages = pdfreader.numPages()
			
			volume = st.slider('Volume',0,100,25,1)
			rate = st.slider('Rate',0,100,45,1)
			
			if st.button("Play"):
				boolna = 2
				playy(data, volume, rate, onpage, pages)
			if st.button("Pause"):
				boolna = 1
			if st.button("Stop"):
				boolna = 0
				onpage = 0
def playy(file, vol, r, yo, pages):
	while boolna==2:
		with fitz.open(file) as doc:
			for page in doc:
				player = pyttsx3.init()
				player.setProperty('rate', r)
				player.setProperty('volume', vol)
				player.say(page.getText())
				player.runAndWait()
				onpage = yo
	
	st.write("Finished")

main()
#for num in range(yo, page in doc):
			#page = pdfreader.getPage(pgno)
			#tex = page.extractText()
