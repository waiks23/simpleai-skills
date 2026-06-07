import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python3 vision_analyze.py /path/to/image.png")
    raise SystemExit(1)

img = sys.argv[1]

prompt = (
    "Describe only what is visible in this image. "
    "Include layout, objects, colours, text, and anything unusual. "
    "Do not guess beyond the image."
)

subprocess.run([
    "ollama",
    "run",
    "llava",
    f"{prompt}\nImage: {img}"
])
