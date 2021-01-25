# coursera-notes-downloader
This is a simple python parser to extract from a local .html file containing the notes from a particular Coursera course to a file that is easier to manipulate (so far only .xlsx format).

There are a few simple steps that you must take to obtain all your notes for some specific course. This steps are described below.

## Steps:
1. Log to Coursera and open the tab that has the notes, typically it has the following format: 
https://www.coursera.org/learn/name-of-the-course/home/notes.
2. Then you must charge all the notes that you have taken on the .html, to do so you must scroll down to the bottom of the page and in the case that your notes do not fit on the page, yo will see a button called ***See More Notes***. You must keep pressing this button until all the notes are on the page.
3. Then you must do ***right clic*** and save the full webpage to get the .html file on the directory ***notes directory*** that comes with the project.
4. Locally on your PC you should open the .html file with any text editor and then save it as a .txt file.
5. Copy the .txt file name, typically is : ***Name Of The Course.txt*** and paste it inside the variable ***filename*** inside the notesExporter.py file.
Currently the variable has the name ***example.txt***.
```Python
#code developed by jamigov
#email: jamigovfecrd@gmail.com

import pandas as pd

fileName = 'example.txt'

```

6. Run the notesExporter.py file. The output would be generated inside the ***output.xlsx*** file.