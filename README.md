# PDF Book Viewer

A simple Python tool with a Tkinter GUI to open scanned book PDFs at a specific page using configurable offsets.
- Opens PDFs named `YYYY_MM.pdf` from the `pdfs` folder.
- Allows you to specify a "book page" which is mapped to the actual PDF page using an offset.
- Stores offsets in `offsets.json` for persistent configuration.
- Uses Adobe Acrobat, though not sure if works on Windows yet. 

## To Dos

Page offsets doesn't work yet, not sure how to call adobe acrobat with page offset.
