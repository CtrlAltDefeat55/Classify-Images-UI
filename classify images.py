import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet import preprocess_input, decode_predictions

def classify_image(input_image):
    model = ResNet50(weights="imagenet")

    img = image.load_img(input_image, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=1)
    return decoded_predictions[0][0][1]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 300)
        self.setWindowTitle("Image Classifier")
        self.setStyleSheet("background-color: lightblue;")

        self.label = QLabel("Drop image file here", self)
        self.label.setGeometry(50, 50, 300, 200)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: lightgreen; font: 14pt Arial;")

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isfile(file_path):
                category = classify_image(file_path)
                output_directory = os.path.join(os.path.dirname(file_path), category)

                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

                shutil.move(file_path, os.path.join(output_directory, os.path.basename(file_path)))

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
