# OCR Text Extraction API

## 🚀 Overview

A production-ready **Flask-based OCR microservice** that extracts text from images using Tesseract OCR.
The API accepts base64-encoded images and returns clean, processed text through simple REST endpoints.

This project demonstrates **backend API design, image preprocessing, OCR integration, and containerized deployment**.

---

## ⚙️ Features

* 📡 REST API for text extraction
* 🖼️ Accepts base64-encoded images
* 🔍 OCR using Tesseract engine
* 🎯 Character filtering for improved accuracy
* ⚡ Lightweight and fast processing
* 🐳 Dockerized for easy deployment
* ❤️ Health check endpoint for monitoring

---

## 🧠 How It Works

1. Client sends an image (base64 encoded)
2. Server decodes and preprocesses the image
3. Image is passed to Tesseract OCR
4. Extracted text is cleaned and returned as JSON

---

## 📡 API Endpoints

### 🔹 Health Check

```http
GET /healthz
```

Response:

```json
{
  "ok": true,
  "tesseract": true
}
```

---

### 🔹 Extract Text

```http
POST /extract-text
```

Request:

```json
{
  "image": "base64_encoded_image_here"
}
```

Response:

```json
{
  "text": "ExtractedText123"
}
```

---

## 🧪 Example (cURL)

```bash
curl -X POST http://localhost:3000/extract-text \
-H "Content-Type: application/json" \
-d '{"image":"<base64_string>"}'
```

---

## 🛠️ Tech Stack

* Python
* Flask
* Tesseract OCR
* Pillow (Image Processing)
* Docker

---

## 🐳 Running with Docker

```bash
docker build -t ocr-api .
docker run -p 3000:3000 ocr-api
```

---

## 🧩 Possible Improvements

* Advanced image preprocessing (thresholding, denoising)
* Multi-language OCR support
* Batch image processing
* Accuracy benchmarking
* Frontend demo interface

---

## 🎯 Use Cases

* Document digitization
* Form data extraction
* Image-based text recognition
* Automation pipelines

---

## 📌 Project Highlights

* Designed as a **stateless microservice**
* Handles **image decoding and OCR pipeline**
* Ready for **cloud deployment**
* Demonstrates **real-world backend engineering practices**

---

## 📄 License

MIT License
