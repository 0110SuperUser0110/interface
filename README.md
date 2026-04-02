# interface

Small PyQt5 desktop prototype with a circular transparent window that renders a metallic ring asset.

## Project Layout

- `interface/main.py`: application entry point
- `interface/gui/gui.py`: circular widget and painting logic
- `interface/assets/metallic_ring.png`: GUI asset
- `interface.sln` / `interface/interface.pyproj`: Visual Studio solution and Python project files

## Requirements

- Python 3.9+
- `pip`

Install dependencies:

```powershell
python -m pip install -r interface\requirements.txt
```

Run the app:

```powershell
python interface\main.py
```

## Notes

- The app now resolves assets relative to the source files, so it can be launched from either the repository root or the `interface` directory.
- Generated files like `.vs`, `__pycache__`, and local logs are ignored for GitHub.
