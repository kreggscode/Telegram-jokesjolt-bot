"""
Quick Fix Script - Repair .env file
This script will fix the corrupted TIMEZONE_OFFSET_HOURS value in your .env file
"""
import os
import shutil

def fix_env_file():
    """Fix the corrupted .env file"""
    env_path = ".env"
    
    if not os.path.exists(env_path):
        print("❌ .env file not found!")
        print("Please create a .env file with your credentials.")
        return
    
    # Backup the original file
    backup_path = ".env.backup"
    shutil.copy(env_path, backup_path)
    print(f"✅ Backed up .env to {backup_path}")
    
    # Read the current .env file
    with open(env_path, 'r') as f:
        lines = f.readlines()
    
    # Fix the TIMEZONE_OFFSET_HOURS line
    fixed_lines = []
    for line in lines:
        if line.startswith("TIMEZONE_OFFSET_HOURS"):
            # Replace with correct value
            fixed_lines.append("TIMEZONE_OFFSET_HOURS=5.5\n")
            print(f"✅ Fixed: {line.strip()} → TIMEZONE_OFFSET_HOURS=5.5")
        else:
            fixed_lines.append(line)
    
    # Write the fixed content back
    with open(env_path, 'w') as f:
        f.writelines(fixed_lines)
    
    print("\n✅ .env file has been fixed!")
    print("\nYou can now run: python -m src.main")

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 Fixing .env File")
    print("=" * 60)
    print()
    
    try:
        fix_env_file()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease manually edit your .env file and change:")
        print("  TIMEZONE_OFFSET_HOURS= Vito Kalava.5")
        print("to:")
        print("  TIMEZONE_OFFSET_HOURS=5.5")
