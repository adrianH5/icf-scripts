# PDF Book Viewer

A simple Python tool with a Tkinter GUI to open scanned book PDFs at a specific page using configurable offsets.
- Opens PDFs named `YYYY_MM.pdf` from the `pdfs` folder.
- Allows you to specify a "book page" which is mapped to the actual PDF page using an offset.
- Stores offsets in `offsets.json` for persistent configuration.
- Designed for macOS with Adobe Acrobat Reader DC (adjustable for other platforms).

## Setup

1. **Download**
   - Download the scanned book PDFs.

2. **Create the PDF Folder**
   - In the project directory, create a folder named `pdfs`.
   - Place all your PDF files inside the `pdfs` folder.

3. **Clone This Repository**
   - Clone or download this project to your local machine.

4. **Install Python 3**
   - Ensure Python 3 is installed.
   - Verify with:
     ```bash
     python3 --version
     ```

## Configuration

- **Adobe Acrobat** is used to open PDFs at a specific page.
  - Make sure it is installed.

## Running the Application

1. Open a Terminal and navigate to the project directory.
2. Run the script:
   ```bash
   python3 main.py
   ```

