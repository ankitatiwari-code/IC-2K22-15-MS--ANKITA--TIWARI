# Multimedia Lab Assignment

**Course:** Multimedia Lab
**Student Name:** Ankita Tiwari
**Program:** Integrated MCA
**Institute:** International Institute of Professional Studies (IIPS), DAVV, Indore

## 📌 About the Project

This repository contains practical assignments completed as part of the Multimedia Lab. The projects explore multimedia processing using Python, including image analysis, audio analysis, video processing, file handling, metadata extraction, and report generation.

The objective is to understand how multimedia data can be processed, analyzed, and organized using Python libraries and command-line tools.

## 🎯 Objectives

* Understand different multimedia file formats.
* Extract and analyze image metadata.
* Process audio files and retrieve audio information.
* Analyze video properties and metadata.
* Perform file operations using Python.
* Generate reports from multimedia analysis.
* Explore speech processing and AI-based voice cloning.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Image Processing:** Pillow (PIL)
* **Audio Metadata:** Mutagen
* **Video Processing:** FFmpeg / FFprobe
* **Environment Variables:** python-dotenv
* **Voice Cloning and Text-to-Speech:** ElevenLabs Python SDK
* **Development Environment:** Visual Studio Code

## 📂 Project Structure

```text
Multimedia-Lab/
│
├── Cluster01-Image-Processing/
│   ├── image_analyzer.py
│   └── photos.jpg
│
├── Cluster02-Audio-Processing/
│   ├── audio_analyzer.py
│   └── datasets/
│       └── sound.m4a
│
├── Cluster03-Video-Processing/
│   └── video_analyzer.py
│
├── Cluster04-File-Utilities/
│   └── file_utils.py
│
├── Cluster05-Task-Pipe/
│   ├── task_pipe.py
│   └── ocr.py
│
├── report_generator.py
├── main.py
├── requirements.txt
└── README.md
```

*Note: Update the folder names and file structure to match your actual repository. The structure above is illustrative.*

## 🖼️ 1. Image Analysis

The image analysis module processes image files and extracts useful information.

**Key features:**

* Open and inspect image files.
* Retrieve image dimensions and format.
* Identify image properties using Pillow.
* Extract available EXIF metadata.

**Library:** `Pillow`

## 🎵 2. Audio Analysis

The audio analysis module examines audio files and retrieves available metadata.

**Key features:**

* Read supported audio files.
* Extract duration and audio properties where supported.
* Retrieve available tags and metadata.
* Analyze audio information using Python.

**Library:** `Mutagen`

## 🎬 3. Video Analysis

The video analysis module extracts information about video files using FFprobe.

**Key features:**

* Inspect video file properties.
* Retrieve duration, resolution, and format when available.
* Examine video and audio streams.
* Process video metadata using command-line tools.

**Tool:** `FFmpeg / FFprobe`

## 📁 4. File Utilities

The file utilities module helps manage multimedia files and supports operations such as file identification, path handling, and organizing input files.

## 📄 5. Task Pipe and OCR

This module explores a pipeline-based approach to multimedia processing and Optical Character Recognition (OCR).

**Key concepts:**

* Processing input through multiple stages.
* Extracting text from supported image or document inputs.
* Organizing processing steps into reusable functions.
* Understanding how pipeline components work together.

*The exact features depend on the implementation in your Python scripts.*

## 📊 6. Report Generation

The report generation module brings analysis results together in a structured format.

**Possible responsibilities:**

* Collect multimedia analysis results.
* Organize extracted metadata.
* Present results in a readable report.
* Support combined execution through a main Python script.

## 🗣️ 7. Voice Cloning and Speech Processing

The voice-cloning assignment explores AI-powered speech generation using the ElevenLabs API.

**Key concepts:**

* Loading API credentials securely.
* Connecting to the ElevenLabs service.
* Creating a voice from eligible audio samples.
* Generating speech using a configured voice.
* Handling API responses and errors.

**Security note:** Keep API keys in a `.env` file and never upload secrets to GitHub.

## ⚙️ Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

If a `requirements.txt` file exists:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your scripts, for example:

```bash
pip install Pillow mutagen python-dotenv elevenlabs
```

Install FFmpeg separately and ensure that `ffprobe` is available in your system PATH if the video analyzer requires it.

### Step 4: Configure environment variables

For the voice-cloning assignment, create a `.env` file in the appropriate project directory:

```env
ELEVENLABS_API_KEY=your_api_key_here
```

Do not commit this file to GitHub.

## ▶️ How to Run

Run the relevant Python script from its directory.

**Image analysis**

```bash
python image_analyzer.py
```

**Audio analysis**

```bash
python audio_analyzer.py
```

**Video analysis**

```bash
python video_analyzer.py "video.mp4"
```

**Main application**

```bash
python main.py
```

The exact commands depend on how the scripts accept their inputs. For example, a script may require a file path as a command-line argument.

## 🔐 Security and Best Practices

* Never upload API keys, passwords, or private credentials.
* Add `.env` and virtual-environment folders to `.gitignore`.
* Use sample multimedia files that you are permitted to share.
* Handle invalid paths and unsupported file formats.
* Keep dependencies documented in `requirements.txt`.

## 📚 Learning Outcomes

Through these assignments, I developed practical experience with:

* Python programming and modular code.
* Image, audio, and video metadata.
* Multimedia file handling.
* External command-line tools.
* API integration and environment variables.
* Basic OCR and AI-based speech processing.
* Debugging and executing Python projects in VS Code.

## 👩‍💻 Author

**Ankita Tiwari**
Integrated MCA
International Institute of Professional Studies (IIPS), DAVV, Indore

---

*This repository is intended for academic learning and practical exploration of multimedia technologies.*

