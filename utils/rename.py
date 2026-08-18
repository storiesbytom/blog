import sys
from pathlib import Path

def rename_images(folder_path=".", prefix="wald"):
    target_dir = Path(folder_path).resolve()

    # Unterstützte Bild-Endungen erfassen und alphabetisch sortieren
    extensions = {".jpg", ".jpeg", ".png", ".webp"}
    files = sorted([f for f in target_dir.iterdir() if f.suffix.lower() in extensions])

    if not files:
        print(f"Keine passenden Bilder in '{target_dir}' gefunden.")
        return

    print(f"Benenne {len(files)} Bilder in '{target_dir}' um...")

    for i, file_path in enumerate(files):
        new_name = f"{prefix}-{i}{file_path.suffix.lower()}"
        new_path = target_dir / new_name
        file_path.rename(new_path)
        print(f"  {file_path.name} -> {new_name}")

if __name__ == "__main__":
    # Pfad aus Argument lesen oder Fallback auf aktuellen Ordner
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    rename_images(path_arg)