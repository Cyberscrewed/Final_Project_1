from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 3
    MIN_CHANNEL: int = 1
    MAX_CHANNEL: int = 9

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.__old_volume: int = 0

        self.main_screen.hide()
        self.chanel_label.hide()
        self.volume_label.hide()

        self.power_button.clicked.connect(lambda: self.power_toggle())
        self.mute_button.clicked.connect(lambda: self.mute_toggle())
        self.volume_up_button.clicked.connect(lambda: self.volume_up())
        self.volume_down_button.clicked.connect(lambda: self.volume_down())
        self.channel_up_button.clicked.connect(lambda: self.channel_up())
        self.channel_down_button.clicked.connect(lambda: self.channel_down())
        self.button_1.clicked.connect(lambda: self.channel_number(1))
        self.button_2.clicked.connect(lambda: self.channel_number(2))
        self.button_3.clicked.connect(lambda: self.channel_number(3))
        self.button_4.clicked.connect(lambda: self.channel_number(4))
        self.button_5.clicked.connect(lambda: self.channel_number(5))
        self.button_6.clicked.connect(lambda: self.channel_number(6))
        self.button_7.clicked.connect(lambda: self.channel_number(7))
        self.button_8.clicked.connect(lambda: self.channel_number(8))
        self.button_9.clicked.connect(lambda: self.channel_number(9))

    def power_toggle(self) -> None:
        """
        Function to toggle power status of TV
        """
        if self.__status:
            self.__status = False
            self.main_screen.hide()
            self.chanel_label.hide()
            self.volume_label.hide()
        else:
            self.__status = True
            self.main_screen.show()
            self.chanel_label.show()
            self.volume_label.show()

    def mute_toggle(self) -> None:
        """
        Function to toggle mute status of TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__old_volume
                self.volume_label.setText('Current Volume: ' + str(self.__volume))
            else:
                self.__muted = True
                self.__old_volume = self.__volume
                self.__volume = self.MIN_VOLUME
                self.volume_label.setText('Current Volume: ' + str(self.__volume))

    def volume_up(self) -> None:
        """
        Function to increase volume, capping at max
        """
        if self.__status:
            if self.__muted:
                self.mute_toggle()
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
                    self.volume_label.setText('Current Volume: ' + str(self.__volume))
            else:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
                    self.volume_label.setText('Current Volume: ' + str(self.__volume))

    def volume_down(self) -> None:
        """
        Function to reduce volume, capping at min
        """
        if self.__status:
            if self.__muted:
                self.mute_toggle()
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1
                    self.volume_label.setText('Current Volume: ' + str(self.__volume))
            else:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1
                    self.volume_label.setText('Current Volume: ' + str(self.__volume))

    def channel_up(self) -> None:
        """
        Function to increase channel, looping at max
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
                self.chanel_label.setText('Current Channel: ' + str(self.__channel))
            else:
                self.__channel = self.MIN_CHANNEL
                self.chanel_label.setText('Current Channel: ' + str(self.__channel))
            self.set_screen(self.__channel)

    def channel_down(self) -> None:
        """
        Function to decrease channel, looping at min
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
                self.chanel_label.setText('Current Channel: ' + str(self.__channel))
            else:
                self.__channel = self.MAX_CHANNEL
                self.chanel_label.setText('Current Channel: ' + str(self.__channel))
            self.set_screen(self.__channel)

    def channel_number(self, num: int) -> None:
        """
        Function to change channel value to specified number
        :param num: Desired channel
        """
        if self.__status:
            self.__channel = num
            self.chanel_label.setText('Current Channel: ' + str(self.__channel))
            self.set_screen(num)

    def set_screen(self, num: int) -> None:
        """
        Function to set screen to desired channel
        :param num: channel value
        """
        self.main_screen.setPixmap(QtGui.QPixmap("images/channel"+str(num)+".png"))
        self.main_screen.setScaledContents(True)



