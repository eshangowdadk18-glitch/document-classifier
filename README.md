# Document Classification & OCR

A Python-based project for extracting text from documents using Tesseract OCR and classifying them.

## 🚀 Features
- **OCR Engine**: Powered by Tesseract OCR 5.x.
- **Image Processing**: Utilizes Pillow for image manipulation.
- **Easy Setup**: Scripts included for environment configuration.

## 🛠️ Prerequisites

### 1. Tesseract OCR Installation
You must have Tesseract OCR installed on your system.
- **Windows**: Download from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
- **Path Config**: Ensure `C:\Program Files\Tesseract-OCR` is added to your System Environment Variables (PATH).

### 2. Python Environment
This project uses a virtual environment to manage dependencies.

## 📦 Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eshangowdadk18-glitch/document-classifier.git
   cd document-classifier
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install pytesseract pillow
   ```

## 🖥️ Usage

To test the OCR functionality with the sample image:
```bash
python ocr_test.py
```

The script will:
1. Open `test.jpg`.
2. Extract text using Tesseract.
3. Print the results to the console.

## 📝 Troubleshooting

If you get a "Tesseract not found" error:
- Verify Tesseract is installed at `C:\Program Files\Tesseract-OCR`.
- The `ocr_test.py` script contains an explicit path setting for Windows users:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```
