import subprocess
import os

def compress_pdf_ghostscript(input_path, output_path, quality="ebook"):
    ghostscript_path = r"C:\Program Files\gs\gs10.04.0\bin\gswin64.exe"
    if not os.path.exists(ghostscript_path):
        print(f"Error: Ghostscript not found: {ghostscript_path}")
        return

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        print(f"Current working directory: {os.getcwd()}")  # Print current directory
        return

    try:
        command = [
            ghostscript_path,
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path,
        ]
        subprocess.run(command, check=True)
        print(f"File compressed successfully and saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Ghostscript compression: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage (using a relative path):
input_pdf = "Binder1.pdf"  # Assumes Binder1.pdf is in the same directory
output_pdf = "output_compressed_gs.pdf"

compress_pdf_ghostscript(input_pdf, output_pdf, quality="screen")