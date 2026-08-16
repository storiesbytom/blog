import os
from PIL import Image

base_dir = os.path.join('assets', 'images')
max_width = 1920
quality = 82
# Schwellenwert in Bytes (1 MB = 1.048.576 Bytes)
size_threshold = 1000 * 1024

processed_count = 0
skipped_count = 0

print("Starte Bildoptimierung...")

for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(root, filename)

            # Prüfen, wie groß die Datei aktuell ist
            file_size = os.path.getsize(filepath)

            # Überspringen, wenn die Datei bereits unter 1 MB klein ist
            if file_size < size_threshold:
                print(f"Übersprungen (bereits klein genug): {filepath}")
                skipped_count += 1
                continue

            try:
                with Image.open(filepath) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    if img.width > max_width:
                        ratio = max_width / float(img.width)
                        new_height = int((float(img.height) * float(ratio)))
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                    img.save(filepath, 'JPEG', optimize=True, quality=quality)
                    processed_count += 1
                    print(f"Optimiert: {filepath}")
            except Exception as e:
                print(f"Fehler bei Datei {filepath}: {e}")

print(f"\nFertig! {processed_count} Bilder optimiert, {skipped_count} übersprungen.")