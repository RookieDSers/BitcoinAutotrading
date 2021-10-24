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

- Use **Signal/Slot** to receive data from outer class
