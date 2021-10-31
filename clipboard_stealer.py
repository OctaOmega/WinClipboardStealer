import ctypes
from ctypes import wintypes
from os import close
import win32api


CF_UNICODETEXT = 13

user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

Open_Clipboard = user32.OpenClipboard
Open_Clipboard.argtypes = wintypes.HWND,
Open_Clipboard.restype = wintypes.BOOL
Get_Clipboard_Data = user32.GetClipboardData
Get_Clipboard_Data.argtypes = wintypes.UINT,
Get_Clipboard_Data.restype = wintypes.HANDLE
Global_Lock = kernel32.GlobalLock
Global_Lock.argtypes = wintypes.HGLOBAL,
Global_Lock.restype = wintypes.LPVOID
Global_Unlock = kernel32.GlobalUnlock
Global_Unlock.argtypes = wintypes.HGLOBAL,
Close_Clipboard = user32.CloseClipboard
Close_Clipboard.argtypes = None
Close_Clipboard.restype = wintypes.BOOL

data = " "
if Open_Clipboard(None):
    clipboard_mem = Get_Clipboard_Data(CF_UNICODETEXT)
    lock_mem_add = Global_Lock(clipboard_mem)
    data = ctypes.wstring_at(lock_mem_add)
    Global_Unlock(clipboard_mem)
    Close_Clipboard()

win32api.MessageBox(None, data, 'Your clipboard Data:' )