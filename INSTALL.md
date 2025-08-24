# Install & Run — Drag-and-Drop Image Classifier & Sorter

This app is Python-based and works on **Windows / macOS / Linux**, subject to TensorFlow wheel availability for your platform.

## 1) Get the code

```bash
git clone https://github.com/<you>/image-classifier-sorter.git
cd image-classifier-sorter
```

## 2) Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

## 3) Install dependencies

**CPU (default):**
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Apple Silicon (macOS):** If the CPU wheel is not available or you want native acceleration,
you may install `tensorflow-macos` instead of `tensorflow`:

```bash
python -m pip install --upgrade pip
python -m pip install PyQt5 Pillow tensorflow-macos
# Optional GPU acceleration on Apple Silicon:
# python -m pip install tensorflow-metal
```

## 4) Run the app

```bash
python "classify images.py"
```

The first run may download **ResNet50** weights (~100MB). This happens once and is cached for later use.

## 5) Troubleshooting

- **TensorFlow wheel not found**: Ensure you are on a supported Python version for your platform.
- **ImportError: PyQt5**: `pip install PyQt5`
- **Model download blocked**: Ensure internet access or pre-populate the Keras cache directory.
- **App window is unresponsive during classification**: See CONTRIBUTING.md about loading the model once and moving inference
  to a worker thread to keep the UI responsive.
