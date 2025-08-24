# Security Policy

## Model Downloads
The first run will download pre-trained weights for ResNet50 (ImageNet). Verify the download source (Keras/TensorFlow)
and ensure your environment uses trusted package indexes and HTTPS.

## Privacy
No images are uploaded by this app; files are processed locally and moved on disk.

## Data loss
Files are **moved** to a new folder. If a same-name file already exists, the underlying move operation may overwrite
or error, depending on the platform. Test with copies and consider enabling collision-safe renaming.
