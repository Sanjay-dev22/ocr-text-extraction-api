# server.py
import io
import os
import base64
import shutil
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import pytesseract

# Use whatever tesseract is on PATH in the container
tess_path = shutil.which("tesseract")
if tess_path:
    pytesseract.pytesseract.tesseract_cmd = tess_path  # usually /usr/bin/tesseract

app = Flask(__name__)
CORS(app)

# (Optional) limit request size to avoid abuse (1 MB)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.get("/healthz")
def healthz():
    return jsonify({
        "ok": True,
        "tesseract": bool(shutil.which("tesseract"))
    }), 200

@app.post("/solve")
def solve_captcha():
    try:
        data = request.get_json(force=True, silent=True) or {}
        image_base64 = data.get('image', '')

        if not image_base64:
            return jsonify({"error": "Missing image"}), 400

        # Strip data URL prefix if present
        if ',' in image_base64:
            image_base64 = image_base64.split(',', 1)[1]

        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data)).convert('L')  # grayscale

        # OCR config
        config = (
            '--psm 7 '
            '-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            'abcdefghijklmnopqrstuvwxyz0123456789@='
        )
        text = pytesseract.image_to_string(image, config=config)
        return jsonify({'text': text.strip()}), 200

    except Exception as e:
        print("❌ Error in /solve:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Local dev: curl http://localhost:3000/healthz
    app.run(host='0.0.0.0', port=3000)
