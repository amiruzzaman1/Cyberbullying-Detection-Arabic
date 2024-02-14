# Cyberbullying Detection App (Arabic) with Streamlit GUI

## Overview

This repository hosts a Cyberbullying Detection App tailored for the Arabic language. The app is designed to identify instances of cyberbullying in Arabic text using various machine learning and deep learning algorithms. The models are fine-tuned for natural language processing and classification tasks, aiming to differentiate between bullying and non-bullying content. The project involves preprocessing, feature representation, model training, and evaluation.

## Algorithms Used

- **Random Forest (RF)**
- **Support Vector Machine (SVM)**
- **Multinomial Naive Bayes (NB)**
- **Decision Tree (DT)**

## Process

1. **Preprocessing:** Ensure the data is suitable for training and evaluation through text tokenization, stemming or lemmatization, and elimination of stop words and unnecessary letters.

2. **Feature Representation:** Utilize various methods for classic algorithms (RF, SVM, DT, NB) and deep learning models (BERT, RNN, ANN, CNN, BiLSTM) to represent features effectively.

3. **Models:**
   - **BERT:** Bidirectional Encoder Representations from Transformers.
   - **RF:** Random Forest.
   - **SVM:** Support Vector Machine.
   - **DT:** Decision Tree.
   - **NB:** Naive Bayes.

4. **Evaluation:** Assess each algorithm's performance using accuracy, precision, recall, and F1-Score metrics.

## Arabic Dataset

The Arabic dataset categorizes online material into two classes: "Bullying" and "Not Bullying." This binary classification provides a clear differentiation between harmful and non-harmful online interactions in the Arabic language, supporting the creation of models to address and mitigate cyberbullying problems.

## Classification Report

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| RF        | 0.94     | 0.93      | 0.94   | 0.93     |
| SVM       | 0.94     | 0.94      | 0.94   | 0.93     |
| NB        | 0.93     | 0.93      | 0.93   | 0.92     |
| DT        | 0.93     | 0.92      | 0.93   | 0.92     |

## GUI with Streamlit

To interact with the Cyberbullying Detection App, visit the [live site](https://amiruzzaman-cbarabic.hf.space/#cyberbullying-detection-app-arabic) and enter text for cyberbullying detection.

### Sample Texts

1. "عنوان خرا 😠😠😠😠😠😠😠😠👎👎👎👎👎"
   - Prediction: Bullying

2. "وامبارح اشتركت بقناتك . شغلك جميل وحلو . واكثر شي بعجبني ب فيديوهاتك انك بتحسسني اني معك ."
   - Prediction: Not Bullying
