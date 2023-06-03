# Web App of Meta's META's  Massively Multilingual Speech (MMS)

This repository contains a Python code that implements a [META's  Massively Multilingual Speech (MMS)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms)  using the Gradio library. The application allows users to record audio and convert it to text, or enter text and generate corresponding local speech output.

## Step 1: Clone repo
```shell
git clone https://github.com/ikequan/meta-mms.git
cd meta-mms
```
## Step 2: Prerequisites

Before running the code, make sure you have the following requirements installed:

- Python 3.x
- gradio
- speech_recognition
- ttsmms
- deep_translator

You can install the required packages using the following command:

```shell
pip install gradio SpeechRecognition ttsmms deep_translator
```

## Step 3: Download language model
Check [here](https://github.com/wannaphong/ttsmms/blob/main/support_list.txt) for supported languages and  their iso code for this step.
```shell
curl https://dl.fbaipublicfiles.com/mms/tts/{put your language iso code here}.tar.gz --output {put your language iso code here}.tar.gz # Update lang
mkdir -p data && tar -xzf {put your language iso code here}.tar.gz -C data/ # Update langcode
```

## Step 4: Run code
```shell
python app.py
```