# SahayAI - Optical Character Recognition (OCR)

## Overview

The Optical Character Recognition (OCR) module extracts text from images.

OCR allows SahayAI to process printed or digital text captured using the
device camera.

This can be useful for accessibility scenarios such as reading:

- Documents
- Notices
- Forms
- Signs
- Labels
- Printed information

---

## Role in SahayAI

The OCR module forms part of the vision processing component.

```text
Camera / Image
      ↓
Image Preprocessing
      ↓
OCR
      ↓
Extracted Text
      ↓
LLM / RAG
      ↓
Accessible Response
