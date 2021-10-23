# PyQt5

We used **PyQt5** for our frontend GUI

Reference: [PyQt5](https://pypi.org/project/PyQt5/)

---

## Creating GUI with QtDesigner

![QtDesigner](/pyQt/QtDesigner.png)

- Qt Designer to design GUI and save as .ui file

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

- Load .ui file on python Code with embedded QtWidget class

  ```python
  import sys
  from PyQt5.QtWidgets import *
  from PyQt5 import uic

  form_class = uic.loadUiType(
      "mywindow.ui")[0]

    # 1
  class MyWindow(QMainWindow, form_class):
      def __init__(self):
          super().__init__()
          self.setupUi(self)
          self.pushButton.clicked.connect(self.btn_clicked)

      def btn_clicked(self):
          print("Button Clicked!")


  app = QApplication(sys.argv)
  window = MyWindow()
  window.show()
  app.exec_()

  ```

  - 1. this dfl:
