import easyocr
class SahayOCR:

    def __init__(self, languages=None):
        """
        Initialize EasyOCR.

        Default language:
        English
        """

        if languages is None:
            languages = ["en"]

        self.reader = easyocr.Reader(
            languages,
            gpu=False
        )

    def extract_text(self, image_path):
        """
        Extract text from an image.

        Returns:
            List of detected text strings.
        """

        results = self.reader.readtext(image_path)

        extracted_text = []

        for _, text, confidence in results:

            extracted_text.append({
                "text": text,
                "confidence": float(confidence)
            })

        return extracted_text


if __name__ == "__main__":

    ocr = SahayOCR()

    image_path = "input/sample.jpg"

    results = ocr.extract_text(image_path)

    print("\nDetected Text:\n")

    for result in results:

        print(
            f"{result['text']} "
            f"(confidence: {result['confidence']:.2f})"
        )
