import streamlit as st 


def main():
        components.html("""
           <!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="index.css" />
  <meta charset="UTF-8">
  <title>File(s) size</title>
</head>

<body>
 <p class="lead text-light mt-4">Select Voice</p>
    
    <!-- Select Menu for Voice -->
    <select id="voices" class="form-select bg-secondary text-light"></select>

    <!-- Range Slliders for Volume, Rate & Pitch -->
    <div class="d-flex mt-4 text-light">
      <div>
        <p class="lead">Volume</p>
        <input type="range" min="0" max="1" value="1" step="0.1" id="volume" />
        <span id="volume-label" class="ms-2">1</span>
      </div>
      <div class="mx-5">
        <p class="lead">Rate</p>
        <input type="range" min="0.1" max="10" value="1" id="rate" step="0.1" />
        <span id="rate-label" class="ms-2">1</span>
      </div>
      <div>
        <p class="lead">Pitch</p>
        <input type="range" min="0" max="2" value="1" step="0.1" id="pitch" />
        <span id="pitch-label" class="ms-2">1</span>
      </div>
    </div>

    <form name="uploadForm">
    <div>
      <input id="uploadInput" type="file" name="myFiles" multiple>
      selected files: <span id="fileNum">0</span>;
      total size: <span id="fileSize">0</span>
    </div>
    <div><button id="submitup" class="btn btn-success mt-5 me-3">Upload</button></div>
  </form>

    <!-- Control Buttons -->
    <div class="mb-5">
      <button id="start" class="btn btn-success mt-5 me-3">Start</button>
      <button id="pause" class="btn btn-warning mt-5 me-3">Pause</button>
      <button id="resume" class="btn btn-info mt-5 me-3">Resume</button>
      <button id="cancel" class="btn btn-danger mt-5 me-3">Cancel</button>
    </div>
  </body>
<script src="./textToSpeech.js"></script>
<script src="/path/to/pdf.js"></script>
<script>
PDFJS.workerSrc = '/path/to/pdf.worker.js';
let dropbox;

dropbox = document.getElementById("dropbox");
dropbox.addEventListener("dragenter", dragenter, false);
dropbox.addEventListener("dragover", dragover, false);
dropbox.addEventListener("drop", drop, false);
function dragenter(e) {
  e.stopPropagation();
  e.preventDefault();
}

function dragover(e) {
  e.stopPropagation();
  e.preventDefault();
}
function drop(e) {
  e.stopPropagation();
  e.preventDefault();

  const dt = e.dataTransfer;
  const files = dt.files;
  updateSize();
 
}

  

  function updateSize() {
    let nBytes = 0,
        oFiles = this.files,
        nFiles = oFiles.length;
    for (let nFileId = 0; nFileId < nFiles; nFileId++) {
      nBytes += oFiles[nFileId].size;
    }
    let sOutput = nBytes + " bytes";

    document.getElementById("fileNum").innerHTML = nFiles;
    document.getElementById("fileSize").innerHTML = sOutput;
    document.getElementById("submitup").addEventListener("change", readoutpdf(oFiles), false);
  }

  document.getElementById("uploadInput").addEventListener("change", updateSize, false);
  
 function readoutpdf(filepdf){
  
  let speech = new SpeechSynthesisUtterance();


speech.lang = "en";

let voices = []; 

window.speechSynthesis.onvoiceschanged = () => {

  voices = window.speechSynthesis.getVoices();
  speech.voice = voices[0];

  
  let voiceSelect = document.querySelector("#voices");
  voices.forEach((voice, i) => (voiceSelect.options[i] = new Option(voice.name, i)));
};

document.querySelector("#rate").addEventListener("input", () => {
  //🐀
  const rate = document.querySelector("#rate").value;
  speech.rate = rate;
  document.querySelector("#rate-label").innerHTML = rate;
});

document.querySelector("#volume").addEventListener("input", () => {
  //🔉🔊
  const volume = document.querySelector("#volume").value;
  speech.volume = volume;
  document.querySelector("#volume-label").innerHTML = volume;
});

document.querySelector("#pitch").addEventListener("input", () => {
  //🏏
  const pitch = document.querySelector("#pitch").value;
  speech.pitch = pitch;
  document.querySelector("#pitch-label").innerHTML = pitch;
});

document.querySelector("#voices").addEventListener("change", () => {
  speech.voice = voices[document.querySelector("#voices").value];
});

document.querySelector("#start").addEventListener("click", () => {
  speech.text = PDFJS.getDocument(filepdf).then(function (pdf) {
            var pdfDocument = pdf;
            var pagesPromises = [];

            for (var i = 0; i < pdf.numPages; i++) {
                
                (function (pageNumber) {
                    pagesPromises.push(getPageText(pageNumber, pdfDocument));
                })(i + 1);
            }

            Promise.all(pagesPromises).then(function (pagesText) {

                return pagesText;
            });

        }, function (reason) {
            // PDF loading error
            return reason;
        });

  window.speechSynthesis.speak(speech);
});

document.querySelector("#pause").addEventListener("click", () => {
  window.speechSynthesis.pause();
});

document.querySelector("#resume").addEventListener("click", () => {
  window.speechSynthesis.resume();
});

document.querySelector("#cancel").addEventListener("click", () => {
  window.speechSynthesis.cancel();
});
}
</script>
</body>
</html>
""")
	
