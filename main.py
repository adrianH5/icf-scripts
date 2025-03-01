import tkinter as tk
from tkinter import messagebox
import os
import json
import subprocess

PDF_FOLDER = "pdfs"

OFFSETS_FILE = "offsets.json"

if os.path.exists(OFFSETS_FILE):
    with open(OFFSETS_FILE, "r") as f:
        offsets_data = json.load(f)
else:
    offsets_data = {}


def get_offset(year, month):
    """
    Retrieve the stored offset for the given year and month.
    If not present, default to 0.
    """
    key = f"{year}_{month}"
    return offsets_data.get(key, 0)


def set_offset(year, month, offset):
    """
    Update the offset for the given year and month in the offsets JSON.
    """
    key = f"{year}_{month}"
    offsets_data[key] = offset
    with open(OFFSETS_FILE, "w") as f:
        json.dump(offsets_data, f, indent=2)


def open_pdf():
    """
    Read year, month, and desired book page from the GUI,
    compute the PDF page by subtracting offset, and open the PDF
    at that page if possible.
    """
    year = year_var.get()
    month = month_var.get()
    book_page_str = page_var.get()

    if not year or not month or not book_page_str.isdigit():
        messagebox.showerror("Error", "Please enter valid Year, Month, and Page.")
        return

    book_page = int(book_page_str)

    # get the offset for this PDF
    offset = get_offset(year, month)

    # convert the book page to actual PDF page
    # clamp it at 1 if the math goes below 1
    pdf_page = max(1, book_page - offset)

    pdf_filename = f"{year}_{month}.pdf"
    pdf_path = os.path.join(PDF_FOLDER, pdf_filename)

    if not os.path.exists(pdf_path):
        messagebox.showerror("Error", f"PDF not found: {pdf_path}")
        return

    # might be different for macos, windows, linux
    try:
        print(pdf_path)
        subprocess.Popen(
            [
                "open",
                "-a",
                "Adobe Acrobat",
                pdf_path,  # The file to open
                "--args",
                "/A",
                f"page={pdf_page}",
            ]
        )
    except FileNotFoundError:
        messagebox.showerror(
            "Error", "Could not find Acrobat Reader. Check the path in the script."
        )
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")


def update_offset():
    """
    Let the user update the offset for the currently entered (year, month).
    """
    year = year_var.get()
    month = month_var.get()
    offset_str = offset_var.get()

    if not year or not month or not offset_str.isdigit():
        messagebox.showerror("Error", "Please enter valid Year, Month, and Offset.")
        return

    offset_value = int(offset_str)

    set_offset(year, month, offset_value)

    messagebox.showinfo(
        "Success", f"Offset updated to {offset_value} for {year}_{month}"
    )


root = tk.Tk()
root.title("PDF Book Viewer")

# Year
tk.Label(root, text="Year (YYYY):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
year_var = tk.StringVar()
tk.Entry(root, textvariable=year_var).grid(row=0, column=1, padx=5, pady=5)

# Month
tk.Label(root, text="Month (MM):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
month_var = tk.StringVar()
tk.Entry(root, textvariable=month_var).grid(row=1, column=1, padx=5, pady=5)

# Book Page
tk.Label(root, text="Book Page:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
page_var = tk.StringVar()
tk.Entry(root, textvariable=page_var).grid(row=2, column=1, padx=5, pady=5)

# Offset
tk.Label(root, text="Offset:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
offset_var = tk.StringVar()
tk.Entry(root, textvariable=offset_var).grid(row=3, column=1, padx=5, pady=5)

# Buttons
open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

offset_button = tk.Button(root, text="Update Offset", command=update_offset)
offset_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()
