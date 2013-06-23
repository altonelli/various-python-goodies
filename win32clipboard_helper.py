def get_clipboard_text():
	import win32clipboard
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data