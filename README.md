# AI

Small PyQt5 desktop prototype with a circular transparent window that renders a metallic ring asset.

## Project Layout

- `AI/main.py`: application entry point
- `AI/gui/gui.py`: circular widget and painting logic
- `AI/assets/metallic_ring.png`: GUI asset
- `AI.sln` / `AI/AI.pyproj`: Visual Studio solution and Python project files

## Requirements

- Python 3.9+
- `pip`

Install dependencies:

```powershell
python -m pip install -r AI\requirements.txt
```

Run the app:

```powershell
python AI\main.py
```

## Notes

- The app now resolves assets relative to the source files, so it can be launched from either the repository root or the `AI` directory.
- Generated files like `.vs`, `__pycache__`, and local logs are ignored for GitHub.
