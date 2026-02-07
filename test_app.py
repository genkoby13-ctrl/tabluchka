"""
Script di test per verificare che il codice sia corretto
Questo script controlla la sintassi e le importazioni base
"""
import sys
import importlib.util

def test_imports():
    """Testa se tutte le importazioni sono corrette"""
    print("Testing imports...")
    
    # Testa le importazioni standard
    try:
        import random
        import time
        print("✓ Standard library imports OK")
    except ImportError as e:
        print(f"✗ Error importing standard library: {e}")
        return False
    
    # Testa le importazioni Kivy (se disponibili)
    kivy_modules = [
        'kivy.app',
        'kivy.uix.screenmanager',
        'kivy.uix.boxlayout',
        'kivy.uix.label',
        'kivy.uix.button',
        'kivy.uix.textinput',
        'kivy.uix.checkbox',
        'kivy.clock',
        'kivy.core.window',
        'kivy.uix.popup',
        'kivy.graphics',
        'kivy.properties'
    ]
    
    kivy_available = True
    for module in kivy_modules:
        try:
            spec = importlib.util.find_spec(module)
            if spec is None:
                kivy_available = False
                break
        except Exception:
            kivy_available = False
            break
    
    if kivy_available:
        print("✓ Kivy imports OK")
    else:
        print("⚠ Kivy not installed (Python 3.14 not supported)")
        print("  Install Python 3.11 or 3.12 to use Kivy")
    
    return True

def test_syntax():
    """Testa la sintassi del file main.py"""
    print("\nTesting syntax...")
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        compile(code, 'main.py', 'exec')
        print("✓ Syntax OK")
        return True
    except SyntaxError as e:
        print(f"✗ Syntax error: {e}")
        return False
    except FileNotFoundError:
        print("✗ main.py not found")
        return False

def test_code_structure():
    """Testa la struttura base del codice"""
    print("\nTesting code structure...")
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Verifica che le classi principali esistano
        required_classes = [
            'ColoredBoxLayout',
            'MenuScreen',
            'TrainingScreen',
            'ResultsScreen',
            'MultiplicationTableApp'
        ]
        
        for cls in required_classes:
            if f'class {cls}' in code:
                print(f"✓ Class {cls} found")
            else:
                print(f"✗ Class {cls} not found")
                return False
        
        # Verifica che ci sia il main
        if 'if __name__ == \'__main__\':' in code:
            print("✓ Main entry point found")
        else:
            print("✗ Main entry point not found")
            return False
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == '__main__':
    import io
    import sys
    # Fix encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    print("=" * 50)
    print("Testing Tabluchka Application")
    print("=" * 50)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Syntax", test_syntax()))
    results.append(("Structure", test_code_structure()))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("✓ All tests passed!")
        print("\nNote: Kivy installation required to run the app.")
        print("Use Python 3.11 or 3.12 for Kivy support.")
    else:
        print("✗ Some tests failed!")
        sys.exit(1)

