# Drag-and-Drop Image Classifier & Sorter (PyQt5 + ResNet50)

A desktop utility that **auto-sorts images by content**. Drop images into the window and the app runs **ResNet50 (ImageNet)**
to predict the best class, then **moves the file** into a same-folder subdirectory named after the predicted label
(e.g., `Labrador_retriever/`). Built with **PyQt5** for a simple GUI and **TensorFlow/Keras** for inference.

- **Core script:** `classify images.py`
- **Behavior:** dragging a file into the window classifies it and moves it into a category folder next to the source file.

---

## Table of Contents

- [Features](#features)
- [Screenshot](#screenshot)
- [Installation](#installation)
- [Usage](#usage)
- [Notes & Limitations](#notes--limitations)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

---

## Features

- **Drag-and-drop** image classification
- **ResNet50 (ImageNet)** pre-trained weights with **top-1** class selection
- **Auto-organize**: file is moved into a `{predicted_label}/` folder beside the original image
- **Minimal UI**: single-window drop zone with clear styling
- Cross-platform GUI (**Windows / macOS / Linux**), subject to TensorFlow wheel availability on your platform

## Screenshot

<img width="394" height="323" alt="classify_Images_UI" src="https://github.com/user-attachments/assets/f6dc5971-35ca-494b-af95-62e7ad2d4693" />



## Installation

See **[INSTALL.md](INSTALL.md)** for a step-by-step guide (virtual env, platform notes for TensorFlow/PyQt).

Quick start:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python "classify images.py"
```

## Usage

1. Run the app: `python "classify images.py"`.
2. Drag one or more image files into the window.
3. The app predicts a label using **ResNet50** and **moves** each image into a folder named after the predicted class
   in the **same directory** as the image file.

> The first prediction will **download ResNet50 weights (~100MB)** if not present. Subsequent runs use the cached weights.

## Notes & Limitations

- **Model load time**: the provided script loads the model **per image**. See CONTRIBUTING.md for guidance on caching the
  model in memory (load once at startup) to speed up batch operations.
- **Overwrites**: if a target file already exists in the destination class folder, `shutil.move` may overwrite or raise an error
  depending on the OS and filesystem. Consider adding unique naming (timestamp or hash) if that matters for your use case.
- **Classes**: ImageNet labels contain underscores (e.g., `Labrador_retriever`). This is expected.
- **GPU/CPU**: TensorFlow falls back to CPU if GPU is unavailable. GPU setup is optional.

## Dependencies

From `requirements.txt`:

- `tensorflow` (CPU build; or `tensorflow-macos` on Apple Silicon)
- `PyQt5`
- `Pillow`

## Contributing

We welcome improvements! See **[CONTRIBUTING.md](CONTRIBUTING.md)** for style, testing, and performance tips.
