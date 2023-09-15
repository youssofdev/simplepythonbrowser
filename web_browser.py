import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the browser
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # Set the default homepage

        # Create navigation bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Create buttons
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.setStatusTip("Forward to next page")
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        refresh_btn = QAction("Refresh", self)
        refresh_btn.setStatusTip("Refresh page")
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go to homepage")
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Create a URL bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Update the URL bar when the page is loaded
        self.browser.urlChanged.connect(self.update_urlbar)

        # Add the browser to the main window
        self.setCentralWidget(self.browser)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

def main():
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Web Browser")
    window = WebBrowser()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
