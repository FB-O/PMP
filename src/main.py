import sys

from helpers import milliseconds_to_hh_mm_ss

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QSlider, QStyle
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon

from main_ui import Ui_MainWindow




class MainWindow(QMainWindow):
    # Constructor for the MainWindow class
    def __init__(self):
        # Call the constructor of the base class (QMainWindow)
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window parameters
        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PySide Media Player")
        self.setWindowIcon(QIcon('resources/pmp.ico'))

        self.ui.pb_play.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        
        # Set-up the media player
        self.mediaplayer = QMediaPlayer(self)
        self.audio = QAudioOutput()

        self.mediaplayer.setVideoOutput(self.ui.videoWidget)
        self.mediaplayer.setAudioOutput(self.audio)

        # File actions
        self.ui.actionOpen.triggered.connect(self.open_video)
        # Media events
        self.mediaplayer.playbackStateChanged.connect(self.update_playtoggle_button)
        self.mediaplayer.positionChanged.connect(self.update_handle_position_of_progress_bar)
        self.mediaplayer.durationChanged.connect(self.set_progress_bar_duration)
        # PushButton events
        self.ui.pb_play.clicked.connect(self.play_video)
        self.ui.pb_play.setToolTip('Select media file.') 
        # Slider events
        self.ui.slider_progressBar.sliderReleased.connect(self.set_media_position)
        


    @Slot()
    def open_video(self) -> None:
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaplayer.setSource(filename)
            self.ui.pb_play.setEnabled(True)
            self.ui.lbl_position.setText("00:00:00")

    
    @Slot()
    def play_video(self) -> None:
        if self.mediaplayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()

        else:
            self.mediaplayer.play()


    @Slot()
    def update_playtoggle_button(self) -> None:
        """
        Switch the ico of the play pushbutton between 'MediaPause' and 'MediaPlay'.
        """
        if self.mediaplayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.ui.pb_play.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )

        else:
            self.ui.pb_play.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )


    @Slot(int)
    def set_progress_bar_duration(self, media_duration: int) -> None:
        """
        Sets the max value of the -slider- progress bar, and update the total duration text.

        Parameters:
            media_duration: int
                Duration of the media in milliseconds.
        """
        self.ui.slider_progressBar.setRange(0, media_duration)

        hh_mm_ss = milliseconds_to_hh_mm_ss(media_duration)
        self.ui.lbl_duration.setText(hh_mm_ss)


    @Slot(int)
    def update_handle_position_of_progress_bar(self, media_position: int) -> None:
        """
        Continuously update both the position of the progress bar, \
        and the timestamp text as the media position changes.
        """
        if not self.ui.slider_progressBar.isSliderDown():
            self.ui.slider_progressBar.setValue(media_position)
        
        hh_mm_ss = milliseconds_to_hh_mm_ss(media_position)
        self.ui.lbl_position.setText(hh_mm_ss)
    
    
    @Slot(int)
    def set_media_position(self):
        """
        Change the media position when the handle of the progress bar\
        jumps to a new position by click, or when it's dragged.
        """
        handle_position = self.ui.slider_progressBar.sliderPosition()
        self.mediaplayer.setPosition(handle_position)
        


if __name__ == "__main__":
    # Create an instance of the QApplication to manage the application's GUI
    app = QApplication(sys.argv)
    # Create an instance of the QMainWindow
    window = MainWindow()
    # Display the main window
    window.show()
    
    # Start the application event loop
    sys.exit(app.exec())
