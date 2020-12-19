from PySide2 import QtWidgets, QtMultimedia, QtMultimediaWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPlayer")

        self.open_icon = self.style().standardIcon(QtWidgets.QStyle.SP_DriveDVDIcon)
        self.play_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay)
        self.previous_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipBackward)
        self.pause_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause)
        self.stop_icon = self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop)

        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.video_widget = QtMultimediaWidgets.QVideoWidget()
        self.player = QtMultimedia.QMediaPlayer()
        self.toolbar = QtWidgets.QToolBar()
        self.file_menu = self.menuBar().addMenu("Fichier")

        # ACTIONS
        self.act_open = self.file_menu.addAction(self.open_icon, "Ouvrir")
        self.act_open.setShortcut("Ctrl+O")
        self.act_play = self.toolbar.addAction(self.play_icon, "Lire")
        self.act_previous = self.toolbar.addAction(self.previous_icon, "Revenir au début")
        self.act_pause = self.toolbar.addAction(self.pause_icon, "Pause")
        self.act_stop = self.toolbar.addAction(self.stop_icon, "Stop")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        pass

    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.video_widget)
        self.player.setVideoOutput(self.video_widget)

    def setup_connections(self):
        pass
