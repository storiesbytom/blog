import os
from PIL import Image

# Hauptpfad zu deinem Bildverzeichnis
base_dir = os.path.join('assets', 'images')
max_width = 1920
quality = 82  # Sehr gute Balance aus Qualität und kleiner Dateigröße

# Zähler für die Statistik
processed_count = 0

print("Starte Bildoptimierung...")

# os.walk durchsucht den Ordner und ALLE Unterordner
for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(root, filename)

            try:
                with Image.open(filepath) as img:
                    # Farbmodus korrigieren, falls RGBA zu JPEG konvertiert wird
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    # Nur verkleinern, wenn das Bild breiter als max_width ist
                    if img.width > max_width:
                        ratio = max_width / float(img.width)
                        new_height = int((float(img.height) * float(ratio)))
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                    # Speicher als komprimiertes JPEG (überschreibt das Original)
                    img.save(filepath, 'JPEG', optimize=True, quality=quality)
                    processed_count += 1
                    print(f"Optimiert: {filepath}")
            except Exception as e:
                print(f"Fehler bei Datei {filepath}: {e}")

print(f"\nFertig! Insgesamt {processed_count} Bilder in allen Unterordnern optimiert.")