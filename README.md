# Automated Flashcard Generation Using LoRA-Enhanced Transformer Models

## Overview
This repository contains a production-ready implementation of an automated flashcard generation system, designed to streamline study practices by converting academic notes into high-quality flashcards. By leveraging advanced transformer models like T5 (Text-to-Text Transfer Transformer), enhanced with Low-Rank Adaptation (LoRA), this solution is optimized for scalability, efficiency, and contextual accuracy.

## Key Features
- Generate high-quality flashcards from academic notes with minimal manual effort.
- Fine-tuned T5 models with LoRA ensure optimal resource usage.
- Built using Streamlit, the application provides an intuitive platform for document uploads and flashcard generation.
- Flashcards are stored for reuse, reducing redundant processing.

## Tech Stack
- Programming Languages: Python
- Machine Learning Frameworks: Hugging Face Transformers, TensorFlow
- Pre-Trained Models: T5 (Fine-tuned on SQuAD and RACE datasets)
- Frontend: Streamlit, Dash
- Evaluation Metrics: ROUGE-L, BERTScore
- Dataset: SciQ ([from Kaggle](https://www.kaggle.com/datasets/thedevastator/sciq-a-dataset-for-science-question-answering))

## Project Workflow
- Data Preprocessing:
  - Input academic notes or documents (PDF format supported).
  - Preprocess and tokenize data to prepare for model ingestion.
- Model Fine-Tuning:
  - The T5 model, pre-trained on SQuAD and RACE datasets, is fine-tuned with the SciQ dataset.
  - LoRA is employed to reduce memory and computational overhead during training.
- Flashcard Generation:
  - Documents are split into manageable chunks to handle token limits.
  - Beam search ensures the generation of optimal question-answer pairs.
- Web Application:
  - Users upload documents through a Streamlit-powered interface.
  - Generated flashcards are displayed and stored for future reference.

## Getting Started

### Prerequisites
- Python 3.8+
- GPU

### Installation
- Clone the repository:
```
git clone https://github.com/your-repo/automated-flashcards.git
cd automated-flashcards
```
- Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
- Install dependencies:
```
pip install -r requirements.txt
```
- Run the application:
```
streamlit run app.py
```

## Example Use Case
- Upload a 20-page academic PDF document.
- The system preprocesses the content and generates 100+ flashcards.
- Flashcards are stored as reusable assets and can be exported as JSON or text files.

## Challenges Addressed
- LoRA reduced trainable parameters by 99.4%, making the model suitable for resource-constrained environments.
- Implemented chunking and summarization strategies to process long documents effectively.

## Results
- ROUGE-L: 0.733
- BERTScore: 0.931
