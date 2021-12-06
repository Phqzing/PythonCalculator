# PythonCalculator
One of my very first projects. A calculator made in python with tkinter

# How to use
- must have python installed in your machine
- open command line / terminal
- cd to the directory where the the calculator.py is located
- run the command ```python3 calculator.py```

# Convert to .EXE
- Since I am on a Linux machine I am not able to convert the file to a windows executable. If you want to convert it to a executable just follow these steps
```
1. Install PyInstaller
 - if PyInstaller is not yet installed for you then you can install it using pip.
 - run the command ```pip install pyinstaller```
 
2. Convert the file to an executable
 - Once PyInstaller is installed all you need to do i run a simple command.
 - cd to the directory where the calculator.py is located and run this command
 ```
 pyinstaller --onefile --clean --noconsole calculator.py
 ```
 - once the process is done, open the directory of where the calculator.py is located. Go to the folder named ``dist`` and you will find the .exe file there.
```
