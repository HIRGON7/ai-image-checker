# 🧠 AI Image Checker

### AI-Generated vs. Real Image Classification Using ResNet-18

A Python desktop application that uses **deep learning and computer vision** to predict whether an image is AI-generated or real.

Built with **PyTorch, Torchvision, ResNet-18, Tkinter, and Pillow**.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![ResNet](https://img.shields.io/badge/Model-ResNet--18-blueviolet?style=for-the-badge)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-009688?style=for-the-badge)

---

## 📖 Overview

**AI Image Checker** is a machine learning project that explores the challenge of distinguishing AI-generated imagery from real photographs.

The application uses a **ResNet-18 Convolutional Neural Network (CNN)** configured for binary image classification.

Users can upload an image through a graphical interface, preview the selected image, and receive a prediction with a confidence score.

The model predicts one of two classes:

- 🤖 **AI Generated** — The image is classified as artificially generated.
- 📷 **Real** — The image is classified as a real image.

The project demonstrates the integration of a trained deep learning model into a Python desktop application.

---

## ✨ Features

- **AI Image Detection:** Predicts whether an image is AI-generated or real.
- **ResNet-18 Architecture:** Uses a residual convolutional neural network for image classification.
- **Confidence Scores:** Displays the predicted class and its softmax confidence percentage.
- **Desktop Interface:** Built with Python's Tkinter library.
- **Image Upload:** Supports JPG, JPEG, and PNG files.
- **Image Preview:** Displays the selected image inside the application.
- **Image Preprocessing:** Applies resizing, tensor conversion, and normalization before inference.
- **CPU Inference:** Runs predictions on the CPU without requiring a dedicated GPU.
- **Custom Interface:** Uses a digital-themed background and electric-blue interface elements.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyTorch | Neural network execution and model inference |
| Torchvision | ResNet-18 architecture and image transformations |
| ResNet-18 | Binary image classification |
| Tkinter | Desktop graphical user interface |
| Pillow (PIL) | Image loading, conversion, and preview |

---

## 🧠 Model Architecture

The application uses **ResNet-18**, a convolutional neural network architecture that incorporates residual connections to support effective training of deep networks.

The classification head is configured to produce two output scores.

### Model Configuration

| Parameter | Value |
|---|---|
| Architecture | ResNet-18 |
| Classification Task | Binary classification |
| Input Resolution | 224 × 224 |
| Input Channels | RGB |
| Output Classes | 2 |
| Class 0 | AI Generated |
| Class 1 | Real |
| Model File | `best_model.pth` |
| Inference Device | CPU |

### Prediction Pipeline

```text
        User Uploads an Image
                  |
                  v
           Load Image (PIL)
                  |
                  v
             Convert to RGB
                  |
                  v
           Resize to 224x224
                  |
                  v
           Convert to Tensor
                  |
                  v
        ImageNet Normalization
                  |
                  v
             ResNet-18 CNN
                  |
                  v
          Classification Head
                  |
                  v
             Softmax Scores
                  |
                  v
           Select Highest Score
                  |
          +-------+-------+
          |               |
          v               v
     AI Generated        Real
          |               |
          +-------+-------+
                  |
                  v
       Display Confidence (%)
```

### Image Preprocessing

The uploaded image undergoes these transformations:

1. RGB conversion.
2. Resizing to 224 × 224 pixels.
3. Conversion into a PyTorch tensor.
4. Normalization using ImageNet statistics.
5. Addition of a batch dimension.

The normalized image is then passed through the trained ResNet-18 model for inference.

---

## 🖥️ Application Interface

The application uses a **420 × 600 Tkinter window** with a digital-themed background.

The interface includes:

- Application title.
- Image upload button.
- 250 × 250 image preview.
- Classification result.
- Confidence percentage.

### Example Output

```text
AI IMAGE CHECKER

[UPLOAD IMAGE]

Prediction: AI Generated
Confidence: 87.45%
```

*The confidence shown above is illustrative.*

---

## 📂 Project Structure

```text
ai-image-checker/
│
├── app.py
├── best_model.pth
├── digital.jpg
├── ico.ico
└── .gitattributes
```

### File Descriptions

| File | Description |
|---|---|
| `app.py` | Main application containing the Tkinter interface, model loading, preprocessing, and prediction functions |
| `best_model.pth` | Saved trained ResNet-18 model weights |
| `digital.jpg` | Background image displayed in the application |
| `ico.ico` | Icon asset |
| `.gitattributes` | Git configuration for text-file normalization |

---

## 🚀 Installation and Setup

### Prerequisites

- Python 3
- pip
- Git
- Required Python libraries
- The trained model file `best_model.pth`

### 1. Clone the Repository

```bash
git clone https://github.com/HIRGON7/ai-image-checker.git
cd ai-image-checker
```

### 2. Install Dependencies

```bash
python -m pip install torch torchvision pillow
```

Tkinter is included with most standard Python installations on Windows.

### 3. Run the Application

```bash
python app.py
```

A desktop window will open.

### 4. Classify an Image

1. Click **UPLOAD IMAGE**.
2. Select a JPG, JPEG, or PNG image.
3. The application displays an image preview.
4. The image is processed and passed through ResNet-18.
5. The predicted classification and confidence percentage appear on the screen.

The model weights are loaded from `best_model.pth`, so the application does not need to retrain the model when launched.

---

## 🔬 How Predictions Work

After processing an image, the model produces two output scores.

The application applies the **Softmax** function:

\[
P(y_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

The class with the highest score is selected as the prediction.

The application displays:

- Predicted class: `AI Generated` or `Real`.
- Confidence: Highest softmax score, expressed as a percentage.

**Note:** A high confidence score does not guarantee that the prediction is correct. Softmax values are not necessarily calibrated probabilities.

---

## 🧪 Training and Evaluation

The repository includes the trained ResNet-18 model weights used for classification.

The current repository focuses on the desktop inference application and does not include the original training pipeline, dataset, or evaluation reports.

Therefore, no specific accuracy, precision, recall, or F1-score is claimed in this README.

---

## ⚠️ Limitations

Detecting AI-generated images is a difficult computer vision problem, particularly as image generation technology continues to evolve.

Potential limitations include:

- Real photographs may be incorrectly classified as AI-generated.
- AI-generated images may be incorrectly classified as real.
- Performance may vary on images from generators not represented in the training data.
- Image editing, compression, or resizing may affect predictions.
- Confidence scores do not constitute proof of image authenticity.

This application is an **educational and experimental computer vision project**, not a definitive digital-forensics tool.

---

## 🔮 Future Improvements

Potential enhancements include:

- Comparing ResNet-18 with other CNN architectures.
- Experimenting with Vision Transformers.
- Improving generalization to newer image generators.
- Adding batch image processing.
- Implementing Grad-CAM for visual explainability.
- Adding detailed model evaluation reports.
- Improving confidence calibration.
- Developing a web-based interface.
- Packaging the application for easier distribution.

---

## 🎯 Project Objectives

This project was developed to gain practical experience with:

- Deep learning and computer vision.
- Image classification using Convolutional Neural Networks.
- ResNet-18 and residual learning.
- PyTorch inference workflows.
- Image preprocessing and normalization.
- Desktop application development with Tkinter.
- Integrating trained machine learning models into applications.

---

## 👨‍💻 Developer

**Hadi Jawhari**

Computer Science Graduate | AI & Software Developer

- **GitHub:** [HIRGON7](https://github.com/HIRGON7)
- **LinkedIn:** [Hadi Jawhari](https://www.linkedin.com/in/hadi-jawhari-3a4322245/)

---

**Built with Python, PyTorch, and ResNet-18.**

*Exploring computer vision and the challenges of identifying AI-generated imagery.*
