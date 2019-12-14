import sys
import os
import requests
from PyQt5 import QtWidgets, QtCore, QtGui, QtWebEngineWidgets


class MainWindow(QtWidgets.QMainWindow, ):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Red Foxy browser')
        self.resize(950, 720)
        self.setWindowIcon(QtGui.QIcon('./redfoxy.png'))

        # 创建浏览器组件
        self.browser = QtWebEngineWidgets.QWebEngineView()
        # url = 'http://www.baidu.com/'
        # url = 'https://www.datasheets.com/'
        # url = 'https://www.datasheets.com/search'
        self.url_line = ''
        # self.browser.setUrl(QtCore.QUrl(url))
        # self.browser.load(QtCore.QUrl(url))

        # 添加表格布局控件
        self.tabs_layout = QtWidgets.QGridLayout()
        # 将浏览器组件添加到表格布局中
        self.tabs_layout.addWidget(self.browser)

        # 添加QTabWidget选项卡
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setLayout(self.tabs_layout)
        self.tabs.addTab(self.browser, '')
        # 添加选项卡到窗口中
        self.setCentralWidget(self.tabs)

        self.browser.loadFinished.connect(lambda: self.tabs.setTabText(0, self.browser.page().title()))

        # 添加编辑框
        self.url_edit = QtWidgets.QLineEdit()

        self.turn_button = QtWidgets.QAction(QtGui.QIcon('./zhuandao.png'), 'Turn', self)
        self.back_button = QtWidgets.QAction(QtGui.QIcon('./fanhui.png'), 'Back', self)
        self.next_button = QtWidgets.QAction(QtGui.QIcon('./tiaozhuan.png'), 'Forward', self)
        self.stop_button = QtWidgets.QAction(QtGui.QIcon('./close.png'), 'Stop', self)
        self.reload_button = QtWidgets.QAction(QtGui.QIcon('./shuaxin.png'), 'Reload', self)
        self.add_button = QtWidgets.QAction(QtGui.QIcon('./add.png'), 'Addpage', self)

        # 添加QToolBar工具条 添加导航栏
        self.main_toolbar = QtWidgets.QToolBar()
        self.main_toolbar.setIconSize(QtCore.QSize(16, 16))
        self.addToolBar(self.main_toolbar)

        self.main_toolbar.addWidget(self.url_edit)
        self.main_toolbar.addSeparator()
        self.main_toolbar.addAction(self.back_button)
        self.main_toolbar.addAction(self.next_button)
        self.main_toolbar.addAction(self.stop_button)
        self.main_toolbar.addAction(self.reload_button)
        self.main_toolbar.addAction(self.add_button)
        self.main_toolbar.addAction(self.turn_button)

        # 添加信号事件
        # 响应地址栏回车事件
        self.url_edit.returnPressed.connect(self.browser.forward)
        # 响应其他事件
        self.back_button.triggered.connect(self.browser.back)
        self.next_button.triggered.connect(self.browser.forward)
        self.stop_button.triggered.connect(self.browser.close)
        self.reload_button.triggered.connect(self.browser.reload)
        self.turn_button.triggered.connect(self.open_url_line)
        self.browser.urlChanged.connect(self.set_url_line)
        self.tabs.tabBarDoubleClicked.connect(lambda x: self.new_page())
        self.add_button.triggered.connect(lambda x: self.new_page())
        self.tabs.tabCloseRequested.connect(self.close_page)

    def set_url_line(self, url):
        if isinstance(url, str):
            self.url_edit.setText(url)
        else:
            self.url_edit.setText(url.toString())

    def open_url_line(self):
        self.url_line = self.url_edit.text()
        print(self.url_line)
        # self.browser.setUrl(QtCore.QUrl(self.url_line))
        self.browser.load(QtCore.QUrl(self.url_line))
        self.browser.loadFinished.connect(self.page_callback)

    def page_callback(self):
        page = self.browser.page()
        page.toHtml(self.parser_html)

    def parser_html(self, content):
        print(content)

    def new_page(self, url='http://www.baidu.com', label='百度'):
        try:
            # self.set_url_line(url)
            browser = QtWebEngineWidgets.QWebEngineView()
            browser.setUrl(QtCore.QUrl(url))
            i = self.tabs.addTab(browser, label)
            self.tabs.setCurrentIndex(i)
            # print(i)

            browser.loadFinished.connect(lambda: self.tabs.setTabText(i, browser.page().title()))
        except Exception as ex:
            print('new_page: {}'.format(ex))

    def goto(self, url):
        self.set_url_line(url)
        self.open_url_line()

    def close_page(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # url = 'https://www.datasheets.com/search/{}'.format('')
    url = 'https://www.datasheets.com/zh-cn/search/{}'.format('RK73B1ELTP4R7J')
    window.goto(url)
    sys.exit(app.exec_())
    # app.exit(app.exec_())
