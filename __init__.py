# https://github.com/miere43/anki-dark-titlebar

from platform import system
from aqt import mw
from ctypes import *

def set_dark_titlebar(window):
    hwnd = c_void_p(int(window.winId()))
    DWMWA_USE_IMMERSIVE_DARK_MODE = c_int(20)
    true_value = c_int(1)
    sizeof_true_value = c_size_t(4)
    hr = windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, byref(true_value), sizeof_true_value)
    # hr should be >=0

def init():
    dwmapi = windll.dwmapi
    dwmapi.DwmSetWindowAttribute.argtypes = [c_void_p, c_int, c_void_p, c_size_t]
    dwmapi.DwmSetWindowAttribute.restype = c_int

if system() == "Windows":
    init()
    set_dark_titlebar(mw)
