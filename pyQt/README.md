# PyQt5

We used **PyQt5** for our frontend GUI

Reference: [PyQt5](https://pypi.org/project/PyQt5/)

---

## Creating GUI with QtDesigner

- Create GUI as .ui file with Qt Designer
  ![QtDesigner](/pyQt/QtDesigner.png)

- Load .ui file on python Code with QtWidget (QMainWindow) and add button, connecting to an action

  ```python
  class MyWindow(QMainWindow, form_class):
      def __init__(self):
          super().__init__()
          self.setupUi(self)

          # connect push button with clicked action
          self.pushButton.clicked.connect(self.btn_clicked)

      def btn_clicked(self):
          print("Button Clicked!")
  ```

  ![mywindow_clicked](/pyQt/mywindow_clicked.gif)

- Use **Signal/Slot** to send/receive data from outer class

  ```python
  class MySignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int, int)

    def run(self):
        # send data with emit() function
        print("emit signal1")
        self.signal1.emit()
        print("emit signal2...")
        self.signal2.emit(1, 2)

  class MyWindow(QMainWindow):
      def __init__(self):
          super().__init__()

          mysignal = MySignal()
          # receive data from emit()
          mysignal.signal1.connect(self.signal1_emitted)
          mysignal.signal2.connect(self.signal2_emitted)
          mysignal.run()

      @pyqtSlot()
      def signal1_emitted(self):
          time.sleep(2)
          print("signal1 emitted")

      @pyqtSlot(int, int)
      def signal2_emitted(self, arg1, arg2):
          time.sleep(5)
          print("signal2 emitted", arg1, arg2)
  ```

  ![mywindow_clicked](/pyQt/pyqt_slotSignal.gif)
