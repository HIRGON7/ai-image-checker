import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import torch.nn as nn
from torchvision import transforms, models
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


ELECTRIC_BLUE = "#00BFFF"


device = torch.device("cpu")

model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load(resource_path("best_model.pth"), map_location=device))
model.eval()


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_tensor)
        probs = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probs, 1)

    label = "AI Generated" if predicted.item() == 0 else "Real"
    return label, confidence.item()


def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        label, confidence = predict_image(file_path)

        result_label.config(
            text=f"{label}\nConfidence: {confidence*100:.2f}%",
            fg=ELECTRIC_BLUE
        )


root = tk.Tk()
root.title("AI Image Checker")
root.geometry("420x600")
root.resizable(False, False)


bg_image = Image.open(resource_path("digital.jpg"))
bg_image = bg_image.resize((420, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title_label = tk.Label(
    root,
    text="AI IMAGE CHECKER",
    font=("Arial", 20, "bold"),
    fg=ELECTRIC_BLUE,
    bg="black"
)
title_label.pack(pady=15)

upload_btn = tk.Button(
    root,
    text="UPLOAD IMAGE",
    font=("Arial", 12, "bold"),
    fg="black",
    bg=ELECTRIC_BLUE,
    width=20,
    height=2,
    command=upload_image
)
upload_btn.pack(pady=15)

image_label = tk.Label(root, bg="black")
image_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    fg=ELECTRIC_BLUE,
    bg="black"
)
result_label.pack(pady=15)

root.mainloop()
