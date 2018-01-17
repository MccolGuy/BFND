import win32clipboard
book = input("무슨 서 입니까?")
chapter = input("몇 장 입니까?")
c = int(chapter)
f = open('\\bible\\개역개정_%s%d.txt' % (book, c))
lines = f.readlines()
start = input("몇절부터?")
a = int(start)
end = input("몇절까지?")
b = int(end)

import sys
sys.stdout.writelines(lines[a-1:b])
# set clipboard data
x = "\n".join(lines[a-1:b])
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("%s"% x)
win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
import os
os.system('Pause')


