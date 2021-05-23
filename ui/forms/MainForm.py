from PyQt5.QtWidgets import QWidget
import ui.ui_designer.forms.main_form as main_form


# 定义一些中间变量
class _MainForm(main_form.Ui_MainForm):
    s = 'abc\n123'
    pass


class MainForm(QWidget):

    def __init__(self):
        super().__init__()
        self.form = _MainForm()
        self.form.setupUi(self)
        # self.mainForm.init()

        self.form.textEdit.setText(self.form.s)

    pass
