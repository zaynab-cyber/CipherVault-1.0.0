"""
CipherVault One-Click Installer
Installs dependencies and launches the app
"""

import subprocess
import sys

def main():
    print("\n🔐 CipherVault Auto-Installer\n" + "="*50)
    
    # Check Python
    if sys.version_info < (3, 8):
        print("❌ Need Python 3.8+")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Install dependencies
    print("\n🔧 Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "-q"
        ])
        print("✅ Dependencies installed!")
    except:
        print("❌ Install failed. Run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Launch
    print("\nLaunching CipherVault...")
    try:
        import main
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()