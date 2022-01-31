# https://github.com/miere43/anki-dark-titlebar

from platform import system
from aqt import mw, gui_hooks
from aqt.customstudy import CustomStudy
from aqt.exporting import ExportDialog
from aqt.fields import FieldDialog
from aqt.qt import QMainWindow, QDialog
from aqt.utils import showInfo
from ctypes import *

dwmapi = None
QMainWindow_show_old = None
QDialog_show_old = None
QDialog_exec_old = None
CustomStudy_setupSignals_old = None
ExportDialog_setup_old = None
FieldDialog_fillFields_old = None

def set_dark_titlebar(window):
    hwnd = c_void_p(int(window.winId()))
    DWMWA_USE_IMMERSIVE_DARK_MODE = c_int(20)
    hr = dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, byref(c_int(1)), c_size_t(4))
    # assert(hr >= 0)

def QMainWindow_show_new(self, *args, **kwargs):
    set_dark_titlebar(self)
    return QMainWindow_show_old(self, *args, *kwargs)

def QDialog_show_new(self, *args, **kwargs):
    set_dark_titlebar(self)
    return QDialog_show_old(self, *args, **kwargs)

def CustomStudy_setupSignals_new(self, *args, **kwargs):
    set_dark_titlebar(self)
    return CustomStudy_setupSignals_old(self, *args, **kwargs)

def ExportDialog_setup_new(self, *args, **kwargs):
    set_dark_titlebar(self)
    return ExportDialog_setup_old(self, *args, **kwargs)

def FieldDialog_fillFields_new(self, *args, **kwargs):
    set_dark_titlebar(self)
    return FieldDialog_fillFields_old(self, *args, **kwargs)

if system() == "Windows":
    dwmapi = WinDLL("dwmapi")
    dwmapi.DwmSetWindowAttribute.argtypes = [c_void_p, c_int, c_void_p, c_size_t]
    dwmapi.DwmSetWindowAttribute.restype = c_int

    QMainWindow_show_old = QMainWindow.show
    QMainWindow.show = QMainWindow_show_new

    QDialog_show_old = QDialog.show
    QDialog.show = QDialog_show_new

    CustomStudy_setupSignals_old = CustomStudy.setupSignals
    CustomStudy.setupSignals = CustomStudy_setupSignals_new

    ExportDialog_setup_old = ExportDialog.setup
    ExportDialog.setup = ExportDialog_setup_new

    FieldDialog_fillFields_old = FieldDialog.fillFields
    FieldDialog.fillFields = FieldDialog_fillFields_new
