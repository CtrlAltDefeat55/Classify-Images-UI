# Contributing

Thanks for helping improve the **Drag-and-Drop Image Classifier & Sorter**!

## Dev setup

```bash
git clone https://github.com/<you>/image-classifier-sorter.git
cd image-classifier-sorter
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Project specifics

- **GUI:** PyQt5 (drag-enter & drop events on a QLabel inside QMainWindow)
- **Model:** `tensorflow.keras.applications.ResNet50(weights="imagenet")`
- **Preprocessing:** `tensorflow.keras.preprocessing.image` + `preprocess_input`
- **Prediction:** `decode_predictions(..., top=1)`; the label string is used for the destination folder

### Performance upgrades (recommended)

- **Load model once**: Create the model at app startup (e.g., in `MainWindow.__init__`) and pass it to the classifier.
  Loading per-file causes large delays.
- **Threading**: Move classification work to a **QThread** or `concurrent.futures` executor to keep the UI responsive
  on big files or many drops.
- **Batching**: If you plan to support folders or many files at once, batch preprocessing to reuse tensors.

### Safety & UX

- Add collision-safe saves: if `dest/filename` exists, append a suffix (e.g., `_1`, timestamp, or hash).
- Show toast/status: display the predicted label and the new location in the UI.
- File validation: ignore non-image files or show an error.

## Style & quality

- Follow **PEP 8**.
- Add docstrings to any added functions/classes.
- Optional tools:
  ```bash
  python -m pip install black ruff mypy
  black .
  ruff check .
  mypy .  # if you add type hints
  ```

## Test plan

- Single small JPG/PNG
- Large images (e.g., 4–8K)
- Multiple drops (2–10 files)
- Duplicate filename in destination folder
- Offline mode (weights already cached)
