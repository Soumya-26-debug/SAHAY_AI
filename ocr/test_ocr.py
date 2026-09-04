from ocr import SahayOCR


def test_ocr_initialization():

    ocr = SahayOCR()

    assert ocr.reader is not None

    print("OCR initialization test passed.")


if __name__ == "__main__":
    test_ocr_initialization()
