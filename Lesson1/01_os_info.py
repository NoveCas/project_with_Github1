# -*- coding: utf-8 -*-
import platform
import sys

# Этой программой собираю информацию об операционной системе и версии питона.

# TODO запустить этот скрипт и закомитить результат его работы (файл os_info.txt)


info = 'OS info is \n {}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
