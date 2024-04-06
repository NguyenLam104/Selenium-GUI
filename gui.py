import sys, os
from ui_form import Ui_Widget
from PySide6.QtCore import (QCoreApplication, QLocale,
                            QMetaObject, QRect,
                            QSize, Qt, QUrl)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon,
                           QPixmap, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget, QMessageBox)
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests, urllib3
from urllib.parse import urlparse, urljoin
from openpyxl import Workbook

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
            Widget.resize(800, 600)
            sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
            Widget.setSizePolicy(sizePolicy)
            Widget.setWindowTitle(u"C\u00f4ng c\u1ee5 ki\u1ec3m th\u1eed trang web t\u1ef1 \u0111\u1ed9ng")
            icon = QIcon()
            icon.addFile(u"../../Img/KTTW.ico", QSize(), QIcon.Normal, QIcon.Off)
            Widget.setWindowIcon(icon)
            Widget.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
            self.line = QFrame(Widget)
            self.line.setObjectName(u"line")
            self.line.setGeometry(QRect(250, 120, 341, 16))
            self.line.setFrameShape(QFrame.HLine)
            self.line.setFrameShadow(QFrame.Sunken)
            self.label = QLabel(Widget)
            self.label.setObjectName(u"label")
            self.label.setEnabled(True)
            self.label.setGeometry(QRect(250, 50, 541, 41))
            sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.label.setSizePolicy(sizePolicy)
            self.label.setMaximumSize(QSize(600, 16777215))
            font = QFont()
            font.setFamilies([u"Arial"])
            font.setPointSize(15)
            font.setBold(True)
            font.setKerning(False)
            self.label.setFont(font)
            self.label.setLocale(QLocale(QLocale.Vietnamese, QLocale.Vietnam))
            self.label.setTextFormat(Qt.PlainText)
            self.label.setScaledContents(False)
            self.label_2 = QLabel(Widget)
            self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(80, 10, 51, 101))
            self.label_2.setMouseTracking(True)
            self.label_2.setContextMenuPolicy(Qt.CustomContextMenu)
            self.label_2.setAcceptDrops(True)
            self.label_2.setPixmap(QPixmap(u"../../Img/image.png"))
            self.label_2.setScaledContents(True)
            self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
            self.groupBox = QGroupBox(Widget)
            self.groupBox.setObjectName(u"groupBox")
            self.groupBox.setGeometry(QRect(150, 170, 501, 131))
            self.label_3 = QLabel(self.groupBox)
            self.label_3.setObjectName(u"label_3")
            self.label_3.setGeometry(QRect(10, 30, 261, 20))
            self.lineEdit = QLineEdit(self.groupBox)
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setGeometry(QRect(100, 70, 371, 31))
            self.groupBox_2 = QGroupBox(Widget)
            self.groupBox_2.setObjectName(u"groupBox_2")
            self.groupBox_2.setGeometry(QRect(130, 310, 241, 241))
            self.errorCheck_302 = QCheckBox(self.groupBox_2)
            self.errorCheck_302.setObjectName(u"errorCheck_302")
            self.errorCheck_302.setGeometry(QRect(20, 40, 61, 26))
            self.errorCheck_302.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_403 = QCheckBox(self.groupBox_2)
            self.errorCheck_403.setObjectName(u"errorCheck_403")
            self.errorCheck_403.setGeometry(QRect(20, 90, 51, 26))
            self.errorCheck_403.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_404 = QCheckBox(self.groupBox_2)
            self.errorCheck_404.setObjectName(u"errorCheck_404")
            self.errorCheck_404.setGeometry(QRect(20, 140, 51, 26))
            self.errorCheck_404.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_408 = QCheckBox(self.groupBox_2)
            self.errorCheck_408.setObjectName(u"errorCheck_408")
            self.errorCheck_408.setGeometry(QRect(20, 190, 51, 26))
            self.errorCheck_408.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_500 = QCheckBox(self.groupBox_2)
            self.errorCheck_500.setObjectName(u"errorCheck_500")
            self.errorCheck_500.setGeometry(QRect(140, 40, 61, 26))
            self.errorCheck_500.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_503 = QCheckBox(self.groupBox_2)
            self.errorCheck_503.setObjectName(u"errorCheck_503")
            self.errorCheck_503.setGeometry(QRect(140, 90, 51, 26))
            self.errorCheck_503.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheck_504 = QCheckBox(self.groupBox_2)
            self.errorCheck_504.setObjectName(u"errorCheck_504")
            self.errorCheck_504.setGeometry(QRect(140, 140, 51, 26))
            self.errorCheck_504.setCursor(QCursor(Qt.PointingHandCursor))
            self.errorCheckAll = QCheckBox(self.groupBox_2)
            self.errorCheckAll.setObjectName(u"errorCheckAll")
            self.errorCheckAll.setGeometry(QRect(140, 190, 51, 26))
            self.errorCheckAll.setCursor(QCursor(Qt.PointingHandCursor))
            self.pushButton = QPushButton(Widget)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setGeometry(QRect(460, 370, 161, 51))
            font1 = QFont()
            font1.setPointSize(12)
            self.pushButton.setFont(font1)
            self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
            self.pushButton_2 = QPushButton(Widget)
            self.pushButton_2.setObjectName(u"pushButton_2")
            self.pushButton_2.setGeometry(QRect(490, 440, 101, 41))
            self.pushButton_2.setFont(font1)
            self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
            self.retranslateUi(Widget)
            QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        self.label.setText(QCoreApplication.translate("Widget", u"C\u00d4NG C\u1ee4 KI\u1ec2M TH\u1eec TRANG WEB T\u1ef0 \u0110\u1ed8NG", None))
        self.label_2.setText("")
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"H\u00e3y nh\u1eadp link trang web c\u1ea7n ki\u1ec3m tra : ", None))
        self.lineEdit.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Ch\u1ecdn l\u1ed7i", None))
        self.errorCheck_302.setText(QCoreApplication.translate("Widget", u"302", None))
        self.errorCheck_403.setText(QCoreApplication.translate("Widget", u"403", None))
        self.errorCheck_404.setText(QCoreApplication.translate("Widget", u"404", None))
        self.errorCheck_408.setText(QCoreApplication.translate("Widget", u"408", None))
        self.errorCheck_500.setText(QCoreApplication.translate("Widget", u"500", None))
        self.errorCheck_503.setText(QCoreApplication.translate("Widget", u"503", None))
        self.errorCheck_504.setText(QCoreApplication.translate("Widget", u"504", None))
        self.errorCheckAll.setText(QCoreApplication.translate("Widget", u"All", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"B\u1eaft \u0111\u1ea7u ki\u1ec3m th\u1eed", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Tho\u00e1t", None))
        pass

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # Kết nối sự kiện click của checkbox "errorCheckAll" với phương thức checkAllErrors
        self.ui.errorCheckAll.clicked.connect(self.checkAllErrors)
        # Kết nối sự kiện click của nút "Bắt đầu kiểm thử" với phương thức check_errors
        self.ui.pushButton.clicked.connect(self.check_errors)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.label_2.mousePressEvent = self.open_url

    def open_url(self, event):
            # Mở liên kết khi pixmap được nhấp vào
        QDesktopServices.openUrl(QUrl("http://dntu.edu.vn"))
    def check_errors(self):
        # Lấy URL từ trường nhập
        url = self.ui.lineEdit.text()
        if self.is_valid_url(url):
            if not any([self.ui.errorCheck_302.isChecked(),
                        self.ui.errorCheck_403.isChecked(),
                        self.ui.errorCheck_404.isChecked(),
                        self.ui.errorCheck_408.isChecked(),
                        self.ui.errorCheck_500.isChecked(),
                        self.ui.errorCheck_503.isChecked(),
                        self.ui.errorCheck_504.isChecked()]):
                QMessageBox.warning(
                    self, "Cảnh báo", "Vui lòng chọn ít nhất một lỗi cần kiểm tra!")
                return
            try:
                # Lấy danh sách mã lỗi được chọn
                selected_errors = self.get_selected_errors()
                # Kiểm tra mã lỗi
                self.check_Error(url, selected_errors)
                QMessageBox.information(
                    self, "Thành công", "Kiểm tra lỗi hoàn thành!")
            except Exception as e:
                QMessageBox.critical(
                    self, "Lỗi", f"Có lỗi xảy ra: {str(e)}")
        else:
            QMessageBox.warning(
                self, "Cảnh báo", "Vui lòng nhập URL hợp lệ trước khi kiểm tra! ""(Các đường link hợp lệ phải bao gồm ""https://{link}/" ")")
    def is_valid_url(self, url):
        return bool(urlparse(url).scheme)

    def check_Error(self, url, selected_errors):
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')  # Chạy Edge ở chế độ headless (ẩn)
        options.add_argument('--disable-gpu')  # Tắt GPU để giảm tài nguyên sử dụng
        driver = webdriver.Edge(options=options)
        try:
            driver.get(url)
            all_links = driver.find_elements(By.TAG_NAME, 'a')
            driver.get(url)
            all_links = driver.find_elements(By.TAG_NAME, 'a')
            error_messages = []  # Danh sách lưu các thông báo lỗi
            for link in all_links:
                link_url = link.get_attribute('href')
                try:
                    if not link_url:
                        continue

                    if urlparse(link_url).scheme == '':
                        link_url = urljoin(url, link_url)

                    try:
                        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                        response = requests.get(link_url, verify=False)
                        response.raise_for_status()

                        if not response.text.strip():
                            error_messages.append(f'Lỗi: Trang web trống - {link_url}')

                    except requests.exceptions.RequestException as re:
                        error_messages.append(f'Lỗi khi kiểm tra link {link_url}: {re}')
                        continue

                    if response.status_code in selected_errors:
                        error_messages.append(f'Lỗi {response.status_code} - {link_url}')

                except Exception as e:
                    error_messages.append(f'Có lỗi xảy ra: {e}')

            # Hiển thị các thông báo lỗi trong MessageBox
            if error_messages:
                QMessageBox.warning(self, "Cảnh báo", "\n".join(error_messages))
        finally:
            driver.quit()
    def get_selected_errors(self):
        selected_errors = []
        if self.ui.errorCheck_302.isChecked():
            selected_errors.append(302)
        if self.ui.errorCheck_403.isChecked():
            selected_errors.append(403)
        if self.ui.errorCheck_404.isChecked():
            selected_errors.append(404)
        if self.ui.errorCheck_408.isChecked():
            selected_errors.append(408)
        if self.ui.errorCheck_500.isChecked():
            selected_errors.append(500)
        if self.ui.errorCheck_503.isChecked():
            selected_errors.append(503)
        if self.ui.errorCheck_504.isChecked():
            selected_errors.append(504)
        return selected_errors

    def checkAllErrors(self):
        # Kiểm tra trạng thái của checkbox "errorCheckAll"
        all_checked = self.ui.errorCheckAll.isChecked()
        # Đặt trạng thái của các checkbox còn lại theo trạng thái của "errorCheckAll"
        self.ui.errorCheck_302.setChecked(all_checked)
        self.ui.errorCheck_403.setChecked(all_checked)
        self.ui.errorCheck_404.setChecked(all_checked)
        self.ui.errorCheck_408.setChecked(all_checked)
        self.ui.errorCheck_500.setChecked(all_checked)
        self.ui.errorCheck_503.setChecked(all_checked)
        self.ui.errorCheck_504.setChecked(all_checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())