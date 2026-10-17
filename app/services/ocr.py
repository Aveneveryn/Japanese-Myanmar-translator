try:
    import pytesseract
    from PIL import Image
except Exception:
    pytesseract = None


def ocr_image(file_path: str) -> str:
    """Extract Japanese text from an image file path. Stubbed: requires pytesseract/Tesseract with Japanese data or PaddleOCR.
    """
    if not pytesseract:
        return ''
    try:
        text = pytesseract.image_to_string(Image.open(file_path), lang='jpn')
        return text
    except Exception:
        return ''
