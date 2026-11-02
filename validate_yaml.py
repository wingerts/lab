#!/usr/bin/env python3
"""Validate all YAML files in the kubernetes directory."""

import sys
import yaml
from pathlib import Path

def validate_yaml_files(directory: str = "kubernetes") -> bool:
    """
    Validate all YAML files in the specified directory.
    
    Args:
        directory: Path to the directory containing YAML files
        
    Returns:
        True if all files are valid, False otherwise
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"Error: Directory '{directory}' not found")
        return False
    
    yaml_files = sorted(dir_path.glob("*.yaml"))
    if not yaml_files:
        print(f"No YAML files found in '{directory}'")
        return False
    
    all_valid = True
    for yaml_file in yaml_files:
        try:
            with open(yaml_file, 'r') as f:
                content = f.read()
                # Skip empty files or files with only comments
                if not content.strip() or content.strip().startswith('#'):
                    print(f"✓ {yaml_file.name}: Empty or comment-only file (skipped)")
                    continue
                
                # Try to parse as YAML
                yaml.safe_load(content)
                print(f"✓ {yaml_file.name}: Valid")
        except yaml.YAMLError as e:
            print(f"✗ {yaml_file.name}: Invalid YAML")
            print(f"  Error: {e}")
            all_valid = False
        except Exception as e:
            print(f"✗ {yaml_file.name}: Error reading file")
            print(f"  Error: {e}")
            all_valid = False
    
    return all_valid

if __name__ == "__main__":
    success = validate_yaml_files()
    sys.exit(0 if success else 1)
