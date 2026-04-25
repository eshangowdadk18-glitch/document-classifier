from PIL import Image
import pytesseract
import os

# Ensure tesseract is in path or set it explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    image_path = "test.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found!")
        return

    print(f"Opening image: {image_path}")
    try:
        img = Image.open(image_path)
        print("Extracting text... (this may take a few seconds)")
        text = pytesseract.image_to_string(img)
        
        print("-" * 20)
        print("Extracted Text:")
        print("-" * 20)
        if text.strip():
            print(text)
        else:
            print("[No text found in image]")
        print("-" * 20)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
