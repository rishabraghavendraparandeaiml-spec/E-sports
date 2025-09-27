#!/usr/bin/env python3
"""
Test script to verify the ESports Community Website setup
"""

import sys
import os

def test_python_version():
    """Test if Python version is compatible"""
    print("Testing Python version...")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required")
        return False
    else:
        print("✅ Python version is compatible")
        return True

def test_dependencies():
    """Test if all required dependencies can be imported"""
    print("\nTesting dependencies...")
    dependencies = [
        ('flask', 'Flask'),
        ('flask_sqlalchemy', 'Flask-SQLAlchemy'),
        ('flask_login', 'Flask-Login'),
        ('flask_wtf', 'Flask-WTF'),
        ('wtforms', 'WTForms'),
        ('werkzeug', 'Werkzeug')
    ]
    
    missing = []
    for module, name in dependencies:
        try:
            __import__(module)
            print(f"✅ {name} is available")
        except ImportError:
            print(f"❌ {name} is missing")
            missing.append(name)
    
    return len(missing) == 0, missing

def test_app_structure():
    """Test if application files exist"""
    print("\nTesting application structure...")
    required_files = [
        'run.py',
        'requirements.txt',
        'app/__init__.py',
        'app/models.py',
        'app/forms.py',
        'app/routes/__init__.py',
        'app/routes/auth.py',
        'app/routes/main.py',
        'app/routes/posts.py'
    ]
    
    missing = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} is missing")
            missing.append(file_path)
    
    return len(missing) == 0, missing

def test_syntax():
    """Test if Python files have correct syntax"""
    print("\nTesting Python syntax...")
    python_files = [
        'run.py',
        'app/__init__.py',
        'app/models.py',
        'app/forms.py',
        'app/routes/auth.py',
        'app/routes/main.py',
        'app/routes/posts.py'
    ]
    
    errors = []
    for file_path in python_files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                compile(content, file_path, 'exec')
                print(f"✅ {file_path} syntax is correct")
            except SyntaxError as e:
                print(f"❌ {file_path} has syntax error: {e}")
                errors.append((file_path, str(e)))
            except Exception as e:
                print(f"⚠️ {file_path} could not be checked: {e}")
        else:
            print(f"❌ {file_path} not found")
            errors.append((file_path, "File not found"))
    
    return len(errors) == 0, errors

def main():
    """Run all tests"""
    print("🚀 ESports Community Website Setup Test")
    print("=" * 50)
    
    all_good = True
    
    # Test Python version
    if not test_python_version():
        all_good = False
    
    # Test dependencies
    deps_ok, missing_deps = test_dependencies()
    if not deps_ok:
        all_good = False
        print(f"\n💡 To install missing packages, run:")
        print(f"   pip install {' '.join(missing_deps.lower() for missing_deps in missing_deps)}")
    
    # Test app structure
    structure_ok, missing_files = test_app_structure()
    if not structure_ok:
        all_good = False
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
    
    # Test syntax
    syntax_ok, syntax_errors = test_syntax()
    if not syntax_ok:
        all_good = False
        print(f"\n❌ Syntax errors found:")
        for file_path, error in syntax_errors:
            print(f"   {file_path}: {error}")
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 All tests passed! The application should be ready to run.")
        print("   You can start it with: python run.py")
    else:
        print("❌ Some issues were found. Please fix them before running the application.")
    
    return all_good

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)