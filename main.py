import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QWidget, QFileDialog, QMessageBox, QComboBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt  # إضافة هذه السطر
import qrcode
from PIL import Image

class QRCodeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator")
        self.setGeometry(100, 100, 500, 400)
        
        # واجهة المستخدم
        self.init_ui()
    
    def init_ui(self):
        # عناصر الواجهة
        self.label_type = QLabel("Select the type:", self)
        self.combo_type = QComboBox(self)
        self.combo_type.addItems(["text", "image"])
        
        self.label_input = QLabel("Enter text and your website link or choose an image:", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter text here if you want text.")
        self.browse_button = QPushButton("Select an image", self)
        self.browse_button.clicked.connect(self.browse_image)
        
        self.generate_button = QPushButton("Generate code QR", self)
        self.generate_button.clicked.connect(self.generate_qr)
        
        self.qr_label = QLabel(self)
        self.qr_label.setFixedSize(300, 300)
        self.qr_label.setStyleSheet("border: 1px solid black;")
        
        # إضافة اسم المطور
        self.developer_label = QLabel("Developed by Obaid Med Bouslahi", self)
        self.developer_label.setAlignment(Qt.AlignCenter)
        
        # ترتيب العناصر
        layout = QVBoxLayout()
        layout.addWidget(self.label_type)
        layout.addWidget(self.combo_type)
        layout.addWidget(self.label_input)
        layout.addWidget(self.input_field)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.qr_label)
        layout.addWidget(self.developer_label)  # إضافة اسم المطور
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select an image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_path:
            self.input_field.setText(file_path)
    
    def generate_qr(self):
        qr_data = self.input_field.text()
        if not qr_data:
            QMessageBox.critical(self, "Error", "Please enter text or choose an image.!")
            return
        
        # إنشاء كود QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # تحقق من النوع
        if self.combo_type.currentText() == "image":
            try:
                img = Image.open(qr_data)
                qr.add_data(qr_data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Image could not be opened.: {e}")
                return
        else:
            qr.add_data(qr_data)
        
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # حفظ وعرض كود QR
        save_path, _ = QFileDialog.getSaveFileName(self, "Save code QR", "", "PNG Files (*.png)")
        if save_path:
            qr_img.save(save_path)
            pixmap = QPixmap(save_path)
            self.qr_label.setPixmap(pixmap.scaled(300, 300))
            QMessageBox.information(self, "success", "QR code saved successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeApp()
    window.show()
    sys.exit(app.exec_())
