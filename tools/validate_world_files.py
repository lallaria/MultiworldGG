#!/usr/bin/env python3
"""
World File Validation Tool

This script validates the generated pyproject.toml and Register.py files
to ensure they meet the standardization requirements.
"""

import os
import re
import ast
from pathlib import Path
from typing import Dict, Any, List, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class WorldFileValidator:
    """Validates generated world files against standardization requirements."""
    
    def __init__(self, worlds_dir: str = "worlds"):
        self.worlds_dir = Path(worlds_dir)
        self.errors = []
        self.warnings = []
        
    def validate_all_worlds(self) -> Tuple[List[str], List[str]]:
        """Validate all worlds and return errors and warnings."""
        world_dirs = [d for d in self.worlds_dir.iterdir() 
                     if d.is_dir() and not d.name.startswith('_') and not d.name.startswith('.')]
        
        logger.info(f"Validating {len(world_dirs)} worlds...")
        
        for world_dir in world_dirs:
            self._validate_world(world_dir)
        
        return self.errors, self.warnings
    
    def _validate_world(self, world_dir: Path) -> None:
        """Validate a single world directory."""
        world_name = world_dir.name
        logger.info(f"Validating {world_name}...")
        
        # Check required files exist
        pyproject_file = world_dir / "pyproject.toml"
        register_file = world_dir / "Register.py"
        init_file = world_dir / "__init__.py"
        
        if not pyproject_file.exists():
            self.errors.append(f"{world_name}: Missing pyproject.toml")
            return
        
        if not register_file.exists():
            self.errors.append(f"{world_name}: Missing Register.py")
            return
        
        if not init_file.exists():
            self.errors.append(f"{world_name}: Missing __init__.py")
            return
        
        # Validate pyproject.toml
        self._validate_pyproject_toml(world_name, pyproject_file)
        
        # Validate Register.py
        self._validate_register_py(world_name, register_file, init_file)
        
        # Validate consistency between files
        self._validate_consistency(world_name, pyproject_file, register_file)
    
    def _validate_pyproject_toml(self, world_name: str, pyproject_file: Path) -> None:
        """Validate pyproject.toml file structure and content."""
        try:
            with open(pyproject_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic TOML structure validation
            if '[project]' not in content:
                self.errors.append(f"{world_name}: Missing [project] section in pyproject.toml")
                return
            
            # Validate required fields using regex
            required_fields = {
                'name': r'name\s*=\s*["\']([^"\']+)["\']',
                'version': r'version\s*=\s*["\']([^"\']+)["\']',
                'description': r'description\s*=\s*["\']([^"\']+)["\']',
                'authors': r'authors\s*=\s*\[',
                'requires-python': r'requires-python\s*=\s*["\']([^"\']+)["\']'
            }
            
            for field, pattern in required_fields.items():
                if not re.search(pattern, content):
                    self.errors.append(f"{world_name}: Missing required field '{field}' in pyproject.toml")
            
            # Validate name matches directory
            name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
            if name_match and name_match.group(1) != world_name:
                self.errors.append(f"{world_name}: Package name '{name_match.group(1)}' doesn't match directory name")
            
            # Validate version format
            version_match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
            if version_match:
                version = version_match.group(1)
                if not re.match(r'^\d+\.\d+\.\d+', version):
                    self.errors.append(f"{world_name}: Invalid version format '{version}' in pyproject.toml")
            
            # Validate requires-python
            python_match = re.search(r'requires-python\s*=\s*["\']([^"\']+)["\']', content)
            if not python_match:
                self.warnings.append(f"{world_name}: Missing requires-python in pyproject.toml")
            elif python_match.group(1) != ">=3.12":
                self.warnings.append(f"{world_name}: requires-python should be '>=3.12'")
            
            # Validate entry points
            if '[project.entry-points."mwgg.plugins"]' not in content:
                self.errors.append(f"{world_name}: Missing entry-points section in pyproject.toml")
            else:
                required_entries = [
                    f"{world_name}.WorldClass",
                    f"{world_name}.WebWorldClass"
                ]
                for entry in required_entries:
                    if entry not in content:
                        self.errors.append(f"{world_name}: Missing entry point '{entry}'")
                    else:
                        # Validate entry point format
                        entry_pattern = rf'"{re.escape(entry)}"\s*=\s*"{re.escape(world_name)}\.Register:\w+"'
                        if not re.search(entry_pattern, content):
                            self.errors.append(f"{world_name}: Invalid entry point format for '{entry}'")
            
        except Exception as e:
            self.errors.append(f"{world_name}: Error reading pyproject.toml: {e}")
    
    def _validate_register_py(self, world_name: str, register_file: Path, init_file: Path) -> None:
        """Validate Register.py file structure and content."""
        try:
            with open(register_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # Parse Python file
            try:
                tree = ast.parse(content)
            except SyntaxError as e:
                self.errors.append(f"{world_name}: Invalid Python syntax in Register.py: {e}")
                return
            # Extract assignments using regex for simplicity
            assignments = {}
            for line in content.split('\n'):
                if '=' in line and not line.strip().startswith('#'):
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip().strip('"\'')
                        assignments[key] = value
            # Validate required metadata
            required_metadata = ['WORLD_NAME', 'GAME_NAME', 'AUTHOR', 'VERSION', 'WORLD_CLASS']
            for field in required_metadata:
                if field not in assignments:
                    self.errors.append(f"{world_name}: Missing required metadata '{field}' in Register.py")
            # Validate plugin name matches directory
            if 'WORLD_NAME' in assignments and assignments['WORLD_NAME'] != world_name:
                self.errors.append(f"{world_name}: WORLD_NAME '{assignments['WORLD_NAME']}' doesn't match directory name")
            # Validate game name is not empty
            if 'GAME_NAME' in assignments and not assignments['GAME_NAME']:
                self.errors.append(f"{world_name}: GAME_NAME is empty in Register.py")
            # Validate author is not empty or "Unknown"
            if 'AUTHOR' in assignments:
                author = assignments['AUTHOR']
                if not author or author == "Unknown":
                    self.warnings.append(f"{world_name}: AUTHOR is empty or 'Unknown' in Register.py")
            # Validate version format
            if 'VERSION' in assignments:
                version = str(assignments['VERSION'])
                if not re.match(r'^\d+\.\d+\.\d+', version):
                    self.errors.append(f"{world_name}: Invalid VERSION format '{version}' in Register.py")
            # Validate IGDB_ID is integer
            if 'IGDB_ID' in assignments:
                try:
                    igdb_id = int(assignments['IGDB_ID'])
                except ValueError:
                    self.errors.append(f"{world_name}: IGDB_ID must be an integer in Register.py")
            # Validate WORLD_CLASS is present (do not check if it exists in __init__.py)
            if 'WORLD_CLASS' not in assignments:
                self.errors.append(f"{world_name}: WORLD_CLASS missing in Register.py")
            # Validate WEB_WORLD_CLASS if present (do not check if it exists in __init__.py)
            
            # Parse imports first so they're available for validation
            imports = []
            for line in content.split('\n'):
                if line.strip().startswith('from .'):
                    import_part = line.strip()
                    if '#' in import_part:
                        import_part = import_part.split('#')[0].strip()
                    # Always split on 'import' and take everything after
                    if 'import' in import_part:
                        import_part = import_part.split('import', 1)[1].strip()
                    # Split by comma and clean up each import
                    for import_name in import_part.split(','):
                        clean_import = import_name.strip()
                        if clean_import:
                            imports.append(clean_import)
            
            # Validate CLIENT_FUNCTION if present
            if 'CLIENT_FUNCTION' in assignments:
                client_function = assignments['CLIENT_FUNCTION']
                # Allow None or valid function names (not empty strings)
                if client_function == "None":
                    # This is valid - no client function
                    pass
                elif not client_function or client_function.strip() == "":
                    self.errors.append(f"{world_name}: CLIENT_FUNCTION is empty in Register.py")
                else:
                    # Check if the function is imported
                    if client_function not in imports:
                        self.errors.append(f"{world_name}: CLIENT_FUNCTION '{client_function}' not imported in Register.py")
            
            # Validate imports (optional, but do not require matching to __init__.py)
            # Only check that import lines exist for WORLD_CLASS and WEB_WORLD_CLASS if present
            
            # Debug logging for import detection
            if ('WORLD_CLASS' in assignments or 
                ('WEB_WORLD_CLASS' in assignments and assignments['WEB_WORLD_CLASS'] != "None") or
                ('CLIENT_FUNCTION' in assignments and assignments['CLIENT_FUNCTION'] != "None")):
                logger.debug(f"{world_name}: Detected imports: {imports}")
                if 'WORLD_CLASS' in assignments:
                    logger.debug(f"{world_name}: WORLD_CLASS = {assignments['WORLD_CLASS']}")
                if 'WEB_WORLD_CLASS' in assignments and assignments['WEB_WORLD_CLASS'] != "None":
                    logger.debug(f"{world_name}: WEB_WORLD_CLASS = {assignments['WEB_WORLD_CLASS']}")
                if 'CLIENT_FUNCTION' in assignments and assignments['CLIENT_FUNCTION'] != "None":
                    logger.debug(f"{world_name}: CLIENT_FUNCTION = {assignments['CLIENT_FUNCTION']}")
            
            if 'WORLD_CLASS' in assignments:
                world_class = assignments['WORLD_CLASS']
                if world_class not in imports:
                    self.errors.append(f"{world_name}: WORLD_CLASS '{world_class}' not imported in Register.py")
            if 'WEB_WORLD_CLASS' in assignments and assignments['WEB_WORLD_CLASS'] != "None":
                web_world_class = assignments['WEB_WORLD_CLASS']
                if web_world_class not in imports:
                    self.errors.append(f"{world_name}: WEB_WORLD_CLASS '{web_world_class}' not imported in Register.py")
        except Exception as e:
            self.errors.append(f"{world_name}: Error reading Register.py: {e}")
    
    def _validate_consistency(self, world_name: str, pyproject_file: Path, register_file: Path) -> None:
        """Validate consistency between pyproject.toml and Register.py."""
        try:
            # Read pyproject.toml
            with open(pyproject_file, 'r', encoding='utf-8') as f:
                pyproject_content = f.read()
            
            # Read Register.py
            with open(register_file, 'r', encoding='utf-8') as f:
                register_content = f.read()
            
            # Extract metadata from Register.py
            register_metadata = {}
            for line in register_content.split('\n'):
                if '=' in line and not line.strip().startswith('#'):
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        key = parts[0].strip()
                        value = parts[1].strip().strip('"\'')
                        register_metadata[key] = value
            
            # Check package name consistency
            name_match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', pyproject_content)
            if name_match and 'WORLD_NAME' in register_metadata:
                pyproject_name = name_match.group(1)
                register_name = register_metadata['WORLD_NAME']
                if pyproject_name != register_name:
                    self.errors.append(f"{world_name}: Package name mismatch: pyproject.toml='{pyproject_name}', Register.py='{register_name}'")
            
            # Check version consistency
            version_match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', pyproject_content)
            if version_match and 'VERSION' in register_metadata:
                pyproject_version = version_match.group(1)
                register_version = register_metadata['VERSION']
                if pyproject_version != register_version:
                    self.errors.append(f"{world_name}: Version mismatch: pyproject.toml='{pyproject_version}', Register.py='{register_version}'")
            
            # Check author consistency
            author_match = re.search(r'\{name\s*=\s*["\']([^"\']+)["\']\}', pyproject_content)
            if author_match and 'AUTHOR' in register_metadata:
                pyproject_author = author_match.group(1)
                register_author = register_metadata['AUTHOR']
                if pyproject_author != register_author:
                    self.warnings.append(f"{world_name}: Author mismatch: pyproject.toml='{pyproject_author}', Register.py='{register_author}'")
            
        except Exception as e:
            self.errors.append(f"{world_name}: Error validating consistency: {e}")
    
    def _class_exists_in_init(self, class_name: str, init_file: Path) -> bool:
        """Check if a class exists in __init__.py file."""
        try:
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple regex check for class definition
            class_pattern = rf'class\s+{re.escape(class_name)}\s*[:\(]'
            return bool(re.search(class_pattern, content))
        except Exception:
            return False
    
    def _function_exists_in_init(self, function_name: str, init_file: Path) -> bool:
        """Check if a function exists in __init__.py file."""
        try:
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Simple regex check for function definition
            function_pattern = rf'def\s+{re.escape(function_name)}\s*\('
            return bool(re.search(function_pattern, content))
        except Exception:
            return False
    
    def generate_validation_report(self) -> str:
        """Generate a comprehensive validation report."""
        errors, warnings = self.validate_all_worlds()
        
        report = f"""
World File Validation Report
===========================

Summary:
- Total errors: {len(errors)}
- Total warnings: {len(warnings)}

"""
        
        if errors:
            report += "Errors:\n"
            for error in errors:
                report += f"- {error}\n"
            report += "\n"
        
        if warnings:
            report += "Warnings:\n"
            for warning in warnings:
                report += f"- {warning}\n"
            report += "\n"
        
        if not errors and not warnings:
            report += "All worlds passed validation!\n"
        elif not errors:
            report += "All worlds passed validation (warnings only)\n"
        else:
            report += "Validation failed - please fix errors above\n"
        
        return report


def main():
    """Main entry point for the validation tool."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Validate world plugin files")
    parser.add_argument("--worlds-dir", default="worlds", help="Path to worlds directory")
    parser.add_argument("--output", help="Output file for validation report")
    
    args = parser.parse_args()
    
    validator = WorldFileValidator(args.worlds_dir)
    report = validator.generate_validation_report()
    
    print(report)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        logger.info(f"Validation report saved to {args.output}")


if __name__ == "__main__":
    main() 