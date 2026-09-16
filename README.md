# The Cebuano Doctor

The Cebuano Doctor is a locally running healthcare chatbot that allows users to ask general health questions in Cebuano (Bisaya). The project uses multiple local AI models through Ollama to translate the user's question, generate a medical response, and translate the response back into Cebuano.

## Project Goal

The goal of this project is to create a simple healthcare chatbot that can understand Cebuano questions while keeping the AI models running locally on the user's computer.

The system uses one model for translation and another model that is focused on medical information.

## Technologies Used

* Python
* Ollama
* Gemma 4 by Google DeepMind
* MedGemma
* Ollama Python library

## How It Works

The chatbot uses three main stages:

```text
Cebuano User Question
        ↓
     Gemma 4
        ↓
English Translation
        ↓
     MedGemma
        ↓
English Medical Response
        ↓
     Gemma 4
        ↓
Cebuano Response
        ↓
      User
```

### 1. Cebuano to English

Gemma 4 receives the user's Cebuano question and translates it into English.

### 2. Medical Response

The English translation is sent to MedGemma. MedGemma generates a general healthcare response based on the translated question.

### 3. English to Cebuano

The medical response is sent back to Gemma 4, which translates it into Cebuano before showing it to the user.

## Requirements

Before running the project, install:

* Python 3
* Ollama
* The required Gemma 4 model
* The required MedGemma model

The project requires the Python `ollama` package.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Cheswhes/Cebuano-Doctor.git
cd Cebuano-Doctor
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install the Python requirements

```bash
pip install -r requirements.txt
```

### 4. Install Ollama models

Make sure Ollama is installed and running.

Check the models currently installed with:

```bash
ollama list
```

The model names used in `app.py` should match the model tags installed on your computer.

The current project configuration uses:

```python
GEMMA_MODEL = "gemma4:e4b"
MEDGEMMA_MODEL = "medgemma1.5"
```

If your installed model tags are different, update these values in `app.py`.

## Running the Chatbot

Make sure Ollama is running before starting the chatbot.

Run:

```bash
python app.py
```

The program will display:

```text
=================================
THE CEBUANO DOCTOR
=================================

IMPORTANT: This chatbot provides general health information only.
It is not a replacement for a licensed medical professional.
For emergencies, seek immediate medical attention.

Type your healthcare question in Cebuano.
Type 'exit' to quit.
```

Enter a Cebuano healthcare question when prompted.

To close the chatbot normally, type:

```text
exit
```

You can also press `Ctrl+C` to exit the program.

## Example Interaction

```text
You: Sakit akong ulo sukad kagahapon. Unsay posible nga hinungdan ani?

Doctor: Ang mga headache kasagarang adunay daghang posibleng hinungdan...
```

The actual response may vary depending on the local models and their generated output.

## Testing and Evaluation

The chatbot was tested using different types of healthcare questions:

1. Simple symptoms
2. Medication/general health
3. Lifestyle
4. Multiple symptoms
5. Potentially urgent symptoms

The evaluation focused on:

* Cebuano-to-English translation accuracy
* Medical response quality
* English-to-Cebuano translation quality
* Safety
* Clarity

The testing showed that the chatbot was generally able to understand Cebuano questions and generate relevant medical information.

One of the main limitations found during testing was the final Cebuano translation. Some medical terms and sentences were translated awkwardly or remained partly in English.

More detailed testing results can be found in:

```text
tests/evaluation.md
```

## Safety Notice

The Cebuano Doctor is an educational healthcare information project.

It is **not a replacement for a licensed medical professional** and should not be used as a substitute for professional medical diagnosis or treatment.

For emergencies or serious symptoms, users should seek immediate medical attention.

The chatbot provides general information and does not personally diagnose users.

## Limitations

The current version has several limitations:

* Cebuano medical translation is not always completely natural.
* Some medical terms may remain in English.
* AI-generated responses can vary between runs.
* The chatbot depends on the local Ollama models being installed and available.
* Response time depends on the computer hardware and the models being used.
* The system provides general health information rather than professional medical diagnosis.

## Project Structure

```text
Cebuano-Doctor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    └── evaluation.md
```

## Future Improvements

Possible improvements for future versions include:

* Improving Cebuano medical translation
* Adding more Cebuano test cases
* Improving response speed
* Adding a graphical user interface
* Adding more medical safety checks
* Testing with a larger number of users
* Using a Cebuano-specific medical language model if one becomes available

## Author

Created as a school project for studying local AI models, natural language processing, and healthcare chatbot development.
