#!/usr/bin/env python3
"""
World Plugin Standardization Tool

This script automates the process of standardizing all world plugins by generating
pyproject.toml and Register.py files for each world in the worlds/ directory.
"""

import os
import re
import ast
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class WorldMetadata:
    """Container for world metadata extracted from __init__.py files."""
    plugin_name: str
    game_name: str
    author: str
    version: str
    igdb_id: int
    world_class: str
    web_world_class: Optional[str]
    client_function: Optional[str]
    description: str
    requirements: List[str]


class WorldMetadataExtractor:
    """Extracts metadata from world __init__.py files."""
    
    def __init__(self, worlds_dir: str = "worlds"):
        self.worlds_dir = Path(worlds_dir)
        
    def extract_from_init_py(self, world_path: str) -> WorldMetadata:
        """Extract metadata from world's __init__.py file."""
        init_file = Path(world_path) / "__init__.py"
        
        if not init_file.exists():
            raise FileNotFoundError(f"__init__.py not found in {world_path}")
            
        with open(init_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract plugin name from directory
        plugin_name = Path(world_path).name
        
        # Extract metadata using various methods
        game_name = self._extract_game_name(content, plugin_name)
        author = self._extract_author(content)
        version = self._extract_version(content)
        igdb_id = self._extract_igdb_id(content)
        world_class = self._extract_world_class(content)
        web_world_class = self._extract_web_world_class(content)
        client_function = self._extract_client_function(content)
        description = self._extract_description(content, game_name)
        requirements = self._extract_requirements(world_path)
        
        return WorldMetadata(
            plugin_name=plugin_name,
            game_name=game_name,
            author=author,
            version=version,
            igdb_id=igdb_id,
            world_class=world_class,
            web_world_class=web_world_class,
            client_function=client_function,
            description=description,
            requirements=requirements
        )
    
    def _extract_game_name(self, content: str, plugin_name: str) -> str:
        """Extract game name from class attributes or docstring."""
        # Try to find game attribute in World class
        game_pattern = r'class\s+\w+World.*?game\s*=\s*["\']([^"\']+)["\']'
        match = re.search(game_pattern, content, re.DOTALL)
        if match:
            return match.group(1)
            
        # Try to find in docstring
        docstring_pattern = r'class\s+\w+World.*?"""(.*?)"""'
        match = re.search(docstring_pattern, content, re.DOTALL)
        if match:
            docstring = match.group(1).strip()
            # Extract first line as game name
            first_line = docstring.split('\n')[0].strip()
            if first_line:
                return first_line
                
        # Fallback: convert plugin name to title case
        return plugin_name.replace('_', ' ').title()
    
    def _extract_author(self, content: str) -> str:
        """Extract author from class attributes."""
        # Handle type-annotated assignments like "author: str = "beauxq""
        author_pattern = r'author\s*:?\s*\w*\s*[:=]\s*["\']([^"\']+)["\']'
        match = re.search(author_pattern, content)
        if match:
            return match.group(1)
            
        # Try alternative patterns
        author_patterns = [
            r'authors\s*=\s*\[["\']([^"\']+)["\']\]',
            r'author\s*=\s*["\']([^"\']+)["\']',
        ]
        
        for pattern in author_patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1)
                
        return "Unknown"
    
    def _extract_version(self, content: str) -> str:
        """Extract version from various possible locations."""
        version_patterns = [
            r'version\s*[:=]\s*["\']([^"\']+)["\']',
            r'__version__\s*[:=]\s*["\']([^"\']+)["\']',
            r'world_version\s*[:=]\s*["\']([^"\']+)["\']',
            r'ap_world_version\s*[:=]\s*["\']([^"\']+)["\']',
        ]
        
        for pattern in version_patterns:
            match = re.search(pattern, content)
            if match:
                version = match.group(1)
                # Ensure it's a valid semver
                if re.match(r'^\d+\.\d+\.\d+', version):
                    return version
                    
        return "1.0.0"
    
    def _extract_igdb_id(self, content: str) -> int:
        """Extract IGDB ID from class attributes."""
        igdb_pattern = r'igdb_id\s*[:=]\s*(\d+)'
        match = re.search(igdb_pattern, content)
        if match:
            return int(match.group(1))
        return 0
    
    def _extract_world_class(self, content: str) -> str:
        """Extract main World class name."""
        # Look for class that inherits from World
        world_class_pattern = r'class\s+(\w+World)\s*\(.*World.*\):'
        match = re.search(world_class_pattern, content)
        if match:
            return match.group(1)
            
        # Fallback: look for any class ending with World
        fallback_pattern = r'class\s+(\w*World)\s*[:\(]'
        match = re.search(fallback_pattern, content)
        if match:
            return match.group(1)
            
        return "World"
    
    def _extract_web_world_class(self, content: str) -> Optional[str]:
        """Extract WebWorld class name if present."""
        web_world_pattern = r'class\s+(\w+Web)\s*\(.*WebWorld.*\):'
        match = re.search(web_world_pattern, content)
        if match:
            return match.group(1)
        return None
    
    def _extract_client_function(self, content: str) -> Optional[str]:
        """Extract client launch function if present."""
        # Look for launch_client function
        client_pattern = r'def\s+(launch_client)\s*\('
        match = re.search(client_pattern, content)
        if match:
            return match.group(1)
        return None
    
    def _extract_description(self, content: str, game_name: str) -> str:
        """Extract description from class docstring."""
        docstring_pattern = r'class\s+\w+World.*?"""(.*?)"""'
        match = re.search(docstring_pattern, content, re.DOTALL)
        if match:
            docstring = match.group(1).strip()
            # Join all non-empty lines in the docstring
            lines = [line.strip() for line in docstring.split('\n') if line.strip()]
            if lines:
                return ' '.join(lines)
        return f"{game_name} randomizer for MultiworldGG"
    
    def _extract_requirements(self, world_path: str) -> List[str]:
        """Extract requirements from requirements.txt if present."""
        req_file = Path(world_path) / "requirements.txt"
        if req_file.exists():
            with open(req_file, 'r') as f:
                return [line.strip() for line in f if line.strip() and not line.startswith('#')]
        return []


class WorldFileGenerator:
    """Generates pyproject.toml and Register.py files from metadata."""
    
    def __init__(self, write_files: bool = True):
        self.write_files = write_files

    def generate_pyproject_toml(self, metadata: WorldMetadata) -> str:
        """Generate pyproject.toml content from metadata."""
        template = f'''[project]
name = "{metadata.plugin_name}"
version = "{metadata.version}"
description = "{metadata.description}"
authors = [
    {{name = "{metadata.author}"}}
]
requires-python = ">=3.12"
'''
        
        if metadata.requirements:
            template += f'\ndependencies = [\n'
            for req in metadata.requirements:
                template += f'    "{req}",\n'
            template += ']\n'
        
        template += f'''
[project.entry-points."mwgg.plugins"]
"{metadata.plugin_name}.WorldClass" = "{metadata.plugin_name}.Register:WORLD_CLASS"
"{metadata.plugin_name}.WebWorldClass" = "{metadata.plugin_name}.Register:WEB_WORLD_CLASS"
'''
        
        return template
    
    def generate_register_py(self, metadata: WorldMetadata) -> str:
        """Generate Register.py content from metadata."""
        imports = [f"from . import {metadata.world_class}"]
        if metadata.web_world_class:
            imports.append(f"from . import {metadata.web_world_class}")
        
        template = f'''{"\n".join(imports)}

"""
{metadata.game_name} World Registration

This file contains the metadata and class references for the {metadata.plugin_name} world.
"""

# Required metadata
WORLD_NAME = "{metadata.plugin_name}"
GAME_NAME = "{metadata.game_name}"
IGDB_ID = {metadata.igdb_id}
AUTHOR = "{metadata.author}"
VERSION = "{metadata.version}"

# Plugin entry points
WORLD_CLASS = {metadata.world_class}
'''
        
        if metadata.web_world_class:
            template += f"WEB_WORLD_CLASS = {metadata.web_world_class}\n"
        else:
            template += "WEB_WORLD_CLASS = None\n"
            
        template += "CLIENT_FUNCTION = None\n"
        
        return template
    
    def generate_for_world(self, world_path: str, metadata: WorldMetadata) -> None:
        """Generate both files for a single world."""
        world_path = Path(world_path)
        pyproject_content = self.generate_pyproject_toml(metadata)
        pyproject_file = world_path / "pyproject.toml"
        register_content = self.generate_register_py(metadata)
        register_file = world_path / "Register.py"
        if self.write_files:
            with open(pyproject_file, 'w', encoding='utf-8') as f:
                f.write(pyproject_content)
            logger.info(f"Generated {pyproject_file}")
            with open(register_file, 'w', encoding='utf-8') as f:
                f.write(register_content)
            logger.info(f"Generated {register_file}")
        else:
            logger.info(f"[DRY-RUN] Would generate {pyproject_file}")
            logger.info(f"[DRY-RUN] Would generate {register_file}")


class WorldBatchProcessor:
    """Processes all worlds in batch."""
    
    def __init__(self, worlds_dir: str = "worlds", write_files: bool = True):
        self.worlds_dir = Path(worlds_dir)
        self.extractor = WorldMetadataExtractor(worlds_dir)
        self.generator = WorldFileGenerator(write_files=write_files)
        self.results = []
        self.write_files = write_files
        
    def process_all_worlds(self) -> None:
        """Process all worlds in parallel."""
        world_dirs = [d for d in self.worlds_dir.iterdir() 
                     if d.is_dir() and not d.name.startswith('_') and not d.name.startswith('.')]
        logger.info(f"Found {len(world_dirs)} worlds to process")
        for world_dir in world_dirs:
            try:
                logger.info(f"Processing {world_dir.name}...")
                metadata = self.extractor.extract_from_init_py(str(world_dir))
                self.generator.generate_for_world(str(world_dir), metadata)
                self.results.append({
                    'world': world_dir.name,
                    'status': 'success',
                    'metadata': metadata
                })
            except Exception as e:
                logger.error(f"Failed to process {world_dir.name}: {e}")
                self.results.append({
                    'world': world_dir.name,
                    'status': 'error',
                    'error': str(e)
                })
    
    def validate_generated_files(self) -> List[str]:
        """Validate all generated files and return errors."""
        errors = []
        
        for result in self.results:
            if result['status'] == 'success':
                world_dir = self.worlds_dir / result['world']
                
                # Check if files exist
                pyproject_file = world_dir / "pyproject.toml"
                register_file = world_dir / "Register.py"
                
                if not pyproject_file.exists():
                    errors.append(f"{result['world']}: pyproject.toml not found")
                if not register_file.exists():
                    errors.append(f"{result['world']}: Register.py not found")
                
                # Validate metadata
                metadata = result['metadata']
                if not metadata.game_name:
                    errors.append(f"{result['world']}: Missing game name")
                if not metadata.author or metadata.author == "Unknown":
                    errors.append(f"{result['world']}: Missing or unknown author")
                if not metadata.world_class:
                    errors.append(f"{result['world']}: Missing world class")
        
        return errors
    
    def create_migration_report(self) -> str:
        """Generate report of migration results including missing metadata list."""
        successful = [r for r in self.results if r['status'] == 'success']
        failed = [r for r in self.results if r['status'] == 'error']
        
        # Identify worlds with missing metadata
        missing_metadata = []
        for result in successful:
            metadata = result['metadata']
            if metadata.author == "Unknown" or not metadata.game_name or metadata.game_name == metadata.plugin_name.replace('_', ' ').title():
                missing_metadata.append(result['world'])
        
        report = f"""
World Standardization Migration Report
====================================

Summary:
- Total worlds processed: {len(self.results)}
- Successful: {len(successful)}
- Failed: {len(failed)}
- Worlds with missing metadata: {len(missing_metadata)}

Successful Migrations:
"""
        
        for result in successful:
            metadata = result['metadata']
            report += f"- {result['world']}: {metadata.game_name} by {metadata.author}\n"
        
        if failed:
            report += "\nFailed Migrations:\n"
            for result in failed:
                report += f"- {result['world']}: {result['error']}\n"
        
        if missing_metadata:
            report += "\nWorlds with Missing Metadata (require manual review):\n"
            for world in missing_metadata:
                report += f"- {world}\n"
        
        # Validation errors
        validation_errors = self.validate_generated_files()
        if validation_errors:
            report += "\nValidation Errors:\n"
            for error in validation_errors:
                report += f"- {error}\n"
        
        return report


def main():
    """Main entry point for the standardization tool."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Standardize world plugins")
    parser.add_argument("--worlds-dir", default="worlds", help="Path to worlds directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated without writing files")
    parser.add_argument("--report-only", action="store_true", help="Generate report only")
    
    args = parser.parse_args()
    write_files = not (args.dry_run or args.report_only)
    processor = WorldBatchProcessor(args.worlds_dir, write_files=write_files)
    
    if args.report_only:
        # Just analyze existing files
        logger.info("Analyzing existing worlds...")
        processor.process_all_worlds()
    else:
        # Generate files
        logger.info("Starting world standardization...")
        processor.process_all_worlds()
        
        if not args.dry_run:
            # Validate results
            errors = processor.validate_generated_files()
            if errors:
                logger.warning(f"Found {len(errors)} validation errors")
                for error in errors:
                    logger.warning(error)
    
    # Generate report
    report = processor.create_migration_report()
    print(report)
    
    # Save report to file
    report_file = Path("world_standardization_report.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    logger.info(f"Report saved to {report_file}")


if __name__ == "__main__":
    main() 