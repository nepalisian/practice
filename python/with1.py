from filemanager import FileManager

with FileManager('text.txt') as fd:
    fd.write('hello world')