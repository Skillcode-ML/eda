import PyPDF2
import streamlit as st 
import pyttsx3




def main():
	boolna = 0
	onpage = 0
	type = [".txt",".pdf"]	
	choice = st.sidebar.selectbox("Select the type of file",type)

	if choice == '.txt':
		st.subheader("Reading text file")

		data = st.file_uploader("Upload a text file", type=["txt"])
		if data is not None:
			df = pd.read_txt(data)
			
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
				playy(volume, rate, onpage, pages)
			if st.button("Pause"):
				boolna = 1
			if st.button("Stop"):
				boolna = 0
				onpage = 0
def playy(vol, r, pgno, pages):
	while boolna==2:
		for num in range(pgno, pages)
			page = pdfreader.getPage(pgno)
			tex = page.extractText()
			player = pyttsx3.init()
			player.setProperty('rate', r)
			player.setProperty('volume', vol)
			player.say(text)
			player.runAndWait()
			onpage = pgno
		st.write("Finished")

main()
