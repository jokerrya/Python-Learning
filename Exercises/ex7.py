"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""

filename = input("Input your filename:")
file_tpye = filename.split(".")[-1]
print("The extension of the file is " + file_tpye)