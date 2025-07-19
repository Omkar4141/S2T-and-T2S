

````markdown
# 🎤 Speech Interface Module (Speech-to-Text & Text-to-Speech)

This Python module provides an easy-to-use interface for:
- Capturing audio from the microphone and converting it to text (Speech-to-Text)
- Converting a text response into spoken audio (Text-to-Speech)

---

## 📦 Requirements

Install the required packages using:

```bash
pip install -r requirements.txt
````

**`requirements.txt`**

```
pyaudio==0.2.14
pyttsx3==2.99
SpeechRecognition==3.14.3
```

---

## 📁 File Structure

```
├── s2tt2s.py     # Main class for audio input/output
├── requirements.txt        # Python package requirements
└── README.md               # Documentation
```
---

## ❗Troubleshooting

* **PyAudio not installing?**
  On some platforms, you might need to install additional dependencies:

  * **Windows**: Use precompiled binaries from [https://www.lfd.uci.edu/\~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
  * **Linux**: `sudo apt-get install portaudio19-dev python3-pyaudio`
  * **macOS**: `brew install portaudio`

