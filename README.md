# Maya Select by String

A PyMEL script for Autodesk Maya that allows you to recursively select animation curves or objects based on name patterns. This tool streamlines workflows when dealing with large hierarchies, or multiple animation curves that share naming conventions.

---

## Features

- Recursively searches selected objects and their children for names matching user-defined strings.  
- Dynamically adds multiple search terms for flexible selection.  
- Selects NURBS curves, locators, or any objects whose names contain the search strings.  
- Provides a simple UI for inputting search patterns.  
- Ideal for rig cleanup, batch selection, or managing complex animation setups.

---

## Installation

1. Place `SelectByString.py` in your Maya scripts folder:  
   - Windows: `Documents\maya\scripts\`  
   - macOS: `~/Library/Preferences/Autodesk/maya/scripts/`  
   - Linux: `~/maya/scripts/`

2. Start Maya and open the Script Editor.

3. Import the script:
```python
import SelectByString
