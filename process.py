import files
import bar
import webbrowser
import os

files = files.files()
bar_path = bar.produceBarChart(files[54])

webbrowser.open("file://"+os.path.realpath(bar_path))
