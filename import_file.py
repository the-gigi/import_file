import os
import sys

def import_file(filename):
    """Import a module given its filename

    Usage:

    m = import_file('../../m.py')

    This is equivalent to:

    import m # if ../.. is in sys.path
    """
    # Save original sys.path
    sys_path = sys.path
    try:
        # Make sure the filename is absolute
        filename = os.path.abspath(filename)
        sys.path.insert(0, os.path.dirname(filename))

        # Get the module name (no extension)
        module_name = os.path.basename(filename)
        module_name = os.path.splitext(module_name)[0]
        module = __import__(module_name, {})
        return module
    finally:
        # Restore original sys.path
        sys.path = sys_path

