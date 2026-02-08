import maya.cmds as cmds

search_fields = []
field_container = None  # To keep track of the layout for fields

def find_hairstrand_curves_recursive(parent, search_terms):
    found_curves = []
    children = cmds.listRelatives(parent, children=True, fullPath=True) or []
    
    for child in children:
        if any(term in child for term in search_terms):
            shapes = cmds.listRelatives(child, shapes=True, fullPath=True) or []
            for shape in shapes:
                if cmds.objectType(shape) == "nurbsCurve":
                    found_curves.append(child)
                    break
        found_curves.extend(find_hairstrand_curves_recursive(child, search_terms))
    
    return found_curves

def select_hairstrand_curves(search_terms):
    selection = cmds.ls(selection=True)
    
    if not selection:
        cmds.warning("No object selected.")
        return []
    
    all_matching_curves = []
    
    for sel in selection:
        all_matching_curves.extend(find_hairstrand_curves_recursive(sel, search_terms))
    
    if not all_matching_curves:
        cmds.warning(f"No matching curves found for: {', '.join(search_terms)}")
        cmds.select(clear=True)
    else:
        cmds.select(all_matching_curves, replace=True)
        print(f"Selected curves matching any of: {search_terms}\n", all_matching_curves)
    
    return all_matching_curves

def show_search_ui():
    """Displays a UI to input multiple search strings (with dynamic field layout)."""
    global search_fields, field_container

    if cmds.window("searchStrUI", exists=True):
        cmds.deleteUI("searchStrUI")

    search_fields = []

    window = cmds.window("searchStrUI", title="Search Curve Names", widthHeight=(300, 300))
    cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    
    cmds.text(label="Enter one or more strings to search for in curve names:")

    # Scroll layout in case many fields are added
    cmds.scrollLayout(height=150)
    field_container = cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    add_search_field()  # Start with one field
    cmds.setParent('..')  # Exit scrollLayout

    cmds.separator(style='in', height=10)

    cmds.rowLayout(numberOfColumns=2, adjustableColumn=True, columnWidth2=(145, 145))
    cmds.button(label="+ Add Another", command=lambda *_: add_search_field())
    cmds.button(label="Find and Select", command=lambda *_: collect_and_search())
    cmds.setParent('..')

    cmds.showWindow(window)

def add_search_field():
    """Adds a new text field inside the field container layout."""
    global search_fields, field_container
    cmds.setParent(field_container)
    field = cmds.textField()
    search_fields.append(field)

def collect_and_search():
    """Collects text from all text fields and runs the search."""
    search_terms = [cmds.textField(field, query=True, text=True).strip() for field in search_fields]
    search_terms = [term for term in search_terms if term]

    if not search_terms:
        cmds.warning("Please enter at least one search string.")
        return

    select_hairstrand_curves(search_terms)

# Launch the UI
show_search_ui()

