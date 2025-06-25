#!/usr/bin/env python3
"""
Unit tests for world standardization tools.

These tests cover the metadata extraction, file generation, and validation
functionality for standardizing world plugins.
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from typing import Dict, Any

# Import the classes we'll be testing
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
from world_standardization import WorldMetadata, WorldMetadataExtractor, WorldFileGenerator, WorldBatchProcessor


class TestWorldMetadata:
    """Test the WorldMetadata dataclass."""
    
    def test_world_metadata_creation(self):
        """Test creating WorldMetadata with all required fields."""
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class="TestWeb",
            client_function=None,
            description="Test description",
            requirements=[]
        )
        assert metadata.plugin_name == "test_world"
        assert metadata.game_name == "Test Game"
        assert metadata.author == "Test Author"
        assert metadata.version == "1.0.0"
        assert metadata.igdb_id == 12345
        assert metadata.world_class == "TestWorld"
        assert metadata.web_world_class == "TestWeb"
        assert metadata.client_function is None
        assert metadata.description == "Test description"
        assert metadata.requirements == []


class TestWorldMetadataExtractor:
    """Test the WorldMetadataExtractor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.extractor = WorldMetadataExtractor()
        self.temp_dir = tempfile.mkdtemp()
        
    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_extract_game_name_from_class_attribute(self):
        """Test extracting game name from class game attribute."""
        content = '''
class TestWorld(World):
    game = "Test Game"
    author = "Test Author"
'''
        result = self.extractor._extract_game_name(content, "test_world")
        assert result == "Test Game"
    
    def test_extract_game_name_from_docstring(self):
        """Test extracting game name from class docstring."""
        content = '''
class TestWorld(World):
    """
    Test Game
    
    This is a test game description.
    """
    author = "Test Author"
'''
        result = self.extractor._extract_game_name(content, "test_world")
        assert result == "Test Game"
    
    def test_extract_game_name_fallback(self):
        """Test fallback to directory name when game name not found."""
        content = '''
class TestWorld(World):
    author = "Test Author"
'''
        result = self.extractor._extract_game_name(content, "test_world")
        assert result == "Test World"
    
    def test_extract_author_from_class_attribute(self):
        """Test extracting author from class author attribute."""
        content = '''
class TestWorld(World):
    game = "Test Game"
    author = "Test Author"
'''
        result = self.extractor._extract_author(content)
        assert result == "Test Author"
    
    def test_extract_author_from_authors_list(self):
        """Test extracting author from authors list attribute."""
        content = '''
class TestWorld(World):
    game = "Test Game"
    authors = ["Test Author"]
'''
        result = self.extractor._extract_author(content)
        assert result == "Test Author"
    
    def test_extract_author_fallback(self):
        """Test fallback to 'Unknown' when author not found."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_author(content)
        assert result == "Unknown"
    
    def test_extract_version_from_class_attribute(self):
        """Test extracting version from class version attribute."""
        content = '''
class TestWorld(World):
    game = "Test Game"
    version = "2.1.0"
'''
        result = self.extractor._extract_version(content)
        assert result == "2.1.0"
    
    def test_extract_version_from_version_variable(self):
        """Test extracting version from __version__ variable."""
        content = '''
__version__ = "1.5.2"

class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_version(content)
        assert result == "1.5.2"
    
    def test_extract_version_fallback(self):
        """Test fallback to '1.0.0' when version not found."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_version(content)
        assert result == "1.0.0"
    
    def test_extract_igdb_id_from_class_attribute(self):
        """Test extracting IGDB ID from class igdb_id attribute."""
        content = '''
class TestWorld(World):
    game = "Test Game"
    igdb_id = 12345
'''
        result = self.extractor._extract_igdb_id(content)
        assert result == 12345
    
    def test_extract_igdb_id_fallback(self):
        """Test fallback to 0 when IGDB ID not found."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_igdb_id(content)
        assert result == 0
    
    def test_extract_world_class_from_inheritance(self):
        """Test extracting world class that inherits from World."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_world_class(content)
        assert result == "TestWorld"
    
    def test_extract_world_class_fallback(self):
        """Test fallback when world class not found."""
        content = '''
class SomeOtherClass:
    pass
'''
        result = self.extractor._extract_world_class(content)
        assert result == "World"
    
    def test_extract_web_world_class_from_inheritance(self):
        """Test extracting web world class that inherits from WebWorld."""
        content = '''
class TestWeb(WebWorld):
    tutorials = []
'''
        result = self.extractor._extract_web_world_class(content)
        assert result == "TestWeb"
    
    def test_extract_web_world_class_not_found(self):
        """Test when web world class not found."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_web_world_class(content)
        assert result is None
    
    def test_extract_client_function_found(self):
        """Test extracting client function when present."""
        content = '''
def launch_client():
    pass
'''
        result = self.extractor._extract_client_function(content)
        assert result == "launch_client"
    
    def test_extract_client_function_not_found(self):
        """Test when client function not found."""
        content = '''
class TestWorld(World):
    game = "Test Game"
'''
        result = self.extractor._extract_client_function(content)
        assert result is None
    
    def test_extract_description_from_docstring(self):
        """Test extracting description from class docstring."""
        content = '''
class TestWorld(World):
    """
    Test Game
    
    This is a test game description that should be extracted.
    """
    game = "Test Game"
'''
        result = self.extractor._extract_description(content, "Test Game")
        assert "test game description" in result.lower()
        assert "this is a test game description" in result.lower()
    
    def test_extract_description_fallback(self):
        """Test fallback description when docstring not found."""
        result = self.extractor._extract_description("", "Test Game")
        assert result == "Test Game randomizer for MultiworldGG"
    
    def test_extract_requirements_from_file(self):
        """Test extracting requirements from requirements.txt."""
        world_path = Path(self.temp_dir) / "test_world"
        world_path.mkdir()
        req_file = world_path / "requirements.txt"
        req_file.write_text("pytest>=6.0\nrequests>=2.25.0\n")
        
        result = self.extractor._extract_requirements(str(world_path))
        assert result == ["pytest>=6.0", "requests>=2.25.0"]
    
    def test_extract_requirements_file_not_found(self):
        """Test when requirements.txt not found."""
        world_path = Path(self.temp_dir) / "test_world"
        world_path.mkdir()
        
        result = self.extractor._extract_requirements(str(world_path))
        assert result == []
    
    def test_extract_from_init_py_success(self):
        """Test successful extraction from __init__.py file."""
        world_path = Path(self.temp_dir) / "test_world"
        world_path.mkdir()
        init_file = world_path / "__init__.py"
        init_file.write_text('''
class TestWorld(World):
    """
    Test Game
    
    This is a test game description.
    """
    game = "Test Game"
    author = "Test Author"
    version = "1.2.3"
    igdb_id = 12345

class TestWeb(WebWorld):
    tutorials = []
''')
        
        metadata = self.extractor.extract_from_init_py(str(world_path))
        assert metadata.plugin_name == "test_world"
        assert metadata.game_name == "Test Game"
        assert metadata.author == "Test Author"
        assert metadata.version == "1.2.3"
        assert metadata.igdb_id == 12345
        assert metadata.world_class == "TestWorld"
        assert metadata.web_world_class == "TestWeb"
        assert metadata.client_function is None
    
    def test_extract_from_init_py_file_not_found(self):
        """Test error when __init__.py not found."""
        world_path = Path(self.temp_dir) / "nonexistent_world"
        
        with pytest.raises(FileNotFoundError):
            self.extractor.extract_from_init_py(str(world_path))


class TestWorldFileGenerator:
    """Test the WorldFileGenerator class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.generator = WorldFileGenerator()
        self.temp_dir = tempfile.mkdtemp()
        
    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_generate_pyproject_toml_basic(self):
        """Test generating basic pyproject.toml content."""
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class="TestWeb",
            client_function=None,
            description="Test description",
            requirements=[]
        )
        
        content = self.generator.generate_pyproject_toml(metadata)
        
        assert '[project]' in content
        assert 'name = "test_world"' in content
        assert 'version = "1.0.0"' in content
        assert 'description = "Test description"' in content
        assert 'authors = [' in content
        assert '{name = "Test Author"}' in content
        assert 'requires-python = ">=3.12"' in content
        assert '[project.entry-points."mwgg.plugins"]' in content
        assert '"test_world.WorldClass" = "test_world.Register:WORLD_CLASS"' in content
        assert '"test_world.WebWorldClass" = "test_world.Register:WEB_WORLD_CLASS"' in content
    
    def test_generate_pyproject_toml_with_requirements(self):
        """Test generating pyproject.toml with dependencies."""
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class="TestWeb",
            client_function=None,
            description="Test description",
            requirements=["pytest>=6.0", "requests>=2.25.0"]
        )
        
        content = self.generator.generate_pyproject_toml(metadata)
        
        assert 'dependencies = [' in content
        assert '"pytest>=6.0",' in content
        assert '"requests>=2.25.0",' in content
    
    def test_generate_register_py_basic(self):
        """Test generating basic Register.py content."""
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class="TestWeb",
            client_function=None,
            description="Test description",
            requirements=[]
        )
        
        content = self.generator.generate_register_py(metadata)
        
        assert 'from . import TestWorld' in content
        assert 'from . import TestWeb' in content
        assert 'WORLD_NAME = "test_world"' in content
        assert 'GAME_NAME = "Test Game"' in content
        assert 'IGDB_ID = 12345' in content
        assert 'AUTHOR = "Test Author"' in content
        assert 'VERSION = "1.0.0"' in content
        assert 'WORLD_CLASS = TestWorld' in content
        assert 'WEB_WORLD_CLASS = TestWeb' in content
        assert 'CLIENT_FUNCTION = None' in content
    
    def test_generate_register_py_no_web_world(self):
        """Test generating Register.py without web world class."""
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class=None,
            client_function=None,
            description="Test description",
            requirements=[]
        )
        
        content = self.generator.generate_register_py(metadata)
        
        assert 'from . import TestWorld' in content
        assert 'from . import TestWeb' not in content
        assert 'WEB_WORLD_CLASS = None' in content
    
    def test_generate_for_world(self):
        """Test generating both files for a world."""
        world_path = Path(self.temp_dir) / "test_world"
        world_path.mkdir()
        
        metadata = WorldMetadata(
            plugin_name="test_world",
            game_name="Test Game",
            author="Test Author",
            version="1.0.0",
            igdb_id=12345,
            world_class="TestWorld",
            web_world_class="TestWeb",
            client_function=None,
            description="Test description",
            requirements=[]
        )
        
        self.generator.generate_for_world(str(world_path), metadata)
        
        pyproject_file = world_path / "pyproject.toml"
        register_file = world_path / "Register.py"
        
        assert pyproject_file.exists()
        assert register_file.exists()
        
        pyproject_content = pyproject_file.read_text()
        register_content = register_file.read_text()
        
        assert '[project]' in pyproject_content
        assert 'WORLD_NAME = "test_world"' in register_content


class TestWorldBatchProcessor:
    """Test the WorldBatchProcessor class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.worlds_dir = Path(self.temp_dir) / "worlds"
        self.worlds_dir.mkdir()
        
    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def create_test_world(self, world_name: str, content: str):
        """Helper to create a test world with __init__.py content."""
        world_path = self.worlds_dir / world_name
        world_path.mkdir()
        init_file = world_path / "__init__.py"
        init_file.write_text(content)
        return world_path
    
    def test_process_all_worlds_success(self):
        """Test processing all worlds successfully."""
        # Create test worlds
        self.create_test_world("world1", '''
class World1World(World):
    game = "World 1"
    author = "Author 1"
    version = "1.0.0"
    igdb_id = 1001
''')
        
        self.create_test_world("world2", '''
class World2World(World):
    game = "World 2"
    author = "Author 2"
    version = "2.0.0"
    igdb_id = 1002

class World2Web(WebWorld):
    tutorials = []
''')
        
        processor = WorldBatchProcessor(str(self.worlds_dir))
        processor.process_all_worlds()
        
        assert len(processor.results) == 2
        assert all(r['status'] == 'success' for r in processor.results)
        
        # Check that files were generated
        world1_pyproject = self.worlds_dir / "world1" / "pyproject.toml"
        world1_register = self.worlds_dir / "world1" / "Register.py"
        world2_pyproject = self.worlds_dir / "world2" / "pyproject.toml"
        world2_register = self.worlds_dir / "world2" / "Register.py"
        
        assert world1_pyproject.exists()
        assert world1_register.exists()
        assert world2_pyproject.exists()
        assert world2_register.exists()
    
    def test_process_all_worlds_with_errors(self):
        """Test processing worlds with some errors."""
        # Create a valid world
        self.create_test_world("valid_world", '''
class ValidWorld(World):
    game = "Valid Game"
    author = "Valid Author"
    version = "1.0.0"
    igdb_id = 1001
''')
        
        # Create an invalid world (no __init__.py)
        invalid_world = self.worlds_dir / "invalid_world"
        invalid_world.mkdir()
        
        processor = WorldBatchProcessor(str(self.worlds_dir))
        processor.process_all_worlds()
        
        assert len(processor.results) == 2
        
        valid_result = next(r for r in processor.results if r['world'] == 'valid_world')
        invalid_result = next(r for r in processor.results if r['world'] == 'invalid_world')
        
        assert valid_result['status'] == 'success'
        assert invalid_result['status'] == 'error'
        assert '__init__.py not found' in invalid_result['error']
    
    def test_validate_generated_files(self):
        """Test validation of generated files."""
        # Create a world with generated files
        world_path = self.create_test_world("test_world", '''
class TestWorld(World):
    game = "Test Game"
    author = "Test Author"
    version = "1.0.0"
    igdb_id = 1001
''')
        
        # Generate files
        pyproject_file = world_path / "pyproject.toml"
        register_file = world_path / "Register.py"
        
        pyproject_file.write_text('''
[project]
name = "test_world"
version = "1.0.0"
description = "Test description"
authors = [
    {name = "Test Author"}
]
requires-python = ">=3.12"

[project.entry-points."mwgg.plugins"]
"test_world.WorldClass" = "test_world.Register:WORLD_CLASS"
"test_world.WebWorldClass" = "test_world.Register:WEB_WORLD_CLASS"
''')
        
        register_file.write_text('''
from . import TestWorld

"""
Test Game World Registration

This file contains the metadata and class references for the test_world world.
"""

# Required metadata
WORLD_NAME = "test_world"
GAME_NAME = "Test Game"
IGDB_ID = 1001
AUTHOR = "Test Author"
VERSION = "1.0.0"

# Plugin entry points
WORLD_CLASS = TestWorld
WEB_WORLD_CLASS = None
CLIENT_FUNCTION = None
''')
        
        processor = WorldBatchProcessor(str(self.worlds_dir))
        processor.results = [{
            'world': 'test_world',
            'status': 'success',
            'metadata': WorldMetadata(
                plugin_name="test_world",
                game_name="Test Game",
                author="Test Author",
                version="1.0.0",
                igdb_id=1001,
                world_class="TestWorld",
                web_world_class=None,
                client_function=None,
                description="Test description",
                requirements=[]
            )
        }]
        
        errors = processor.validate_generated_files()
        assert len(errors) == 0
    
    def test_create_migration_report(self):
        """Test creating migration report."""
        processor = WorldBatchProcessor(str(self.worlds_dir))
        processor.results = [
            {
                'world': 'world1',
                'status': 'success',
                'metadata': WorldMetadata(
                    plugin_name="world1",
                    game_name="World 1",
                    author="Author 1",
                    version="1.0.0",
                    igdb_id=1001,
                    world_class="World1World",
                    web_world_class=None,
                    client_function=None,
                    description="World 1 description",
                    requirements=[]
                )
            },
            {
                'world': 'world2',
                'status': 'error',
                'error': 'File not found'
            }
        ]
        
        report = processor.create_migration_report()
        
        assert 'Total worlds processed: 2' in report
        assert 'Successful: 1' in report
        assert 'Failed: 1' in report
        assert 'world1: World 1 by Author 1' in report
        assert 'world2: File not found' in report


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.worlds_dir = Path(self.temp_dir) / "worlds"
        self.worlds_dir.mkdir()
        
    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_complete_workflow(self):
        """Test the complete workflow from extraction to generation."""
        # Create a test world
        world_path = self.worlds_dir / "test_world"
        world_path.mkdir()
        init_file = world_path / "__init__.py"
        init_file.write_text('''
class TestWorld(World):
    """
    Test Game
    
    This is a test game for integration testing.
    """
    game = "Test Game"
    author = "Test Author"
    version = "1.2.3"
    igdb_id = 12345

class TestWeb(WebWorld):
    tutorials = []
''')
        
        # Create requirements.txt
        req_file = world_path / "requirements.txt"
        req_file.write_text("pytest>=6.0\nrequests>=2.25.0\n")
        
        # Test the complete workflow
        extractor = WorldMetadataExtractor(str(self.worlds_dir))
        generator = WorldFileGenerator()
        processor = WorldBatchProcessor(str(self.worlds_dir))
        
        # Extract metadata
        metadata = extractor.extract_from_init_py(str(world_path))
        assert metadata.plugin_name == "test_world"
        assert metadata.game_name == "Test Game"
        assert metadata.author == "Test Author"
        assert metadata.version == "1.2.3"
        assert metadata.igdb_id == 12345
        assert metadata.world_class == "TestWorld"
        assert metadata.web_world_class == "TestWeb"
        assert metadata.client_function is None
        assert len(metadata.requirements) == 2
        
        # Generate files
        generator.generate_for_world(str(world_path), metadata)
        
        # Verify files were created
        pyproject_file = world_path / "pyproject.toml"
        register_file = world_path / "Register.py"
        
        assert pyproject_file.exists()
        assert register_file.exists()
        
        # Verify content
        pyproject_content = pyproject_file.read_text()
        register_content = register_file.read_text()
        
        assert 'name = "test_world"' in pyproject_content
        assert 'version = "1.2.3"' in pyproject_content
        assert 'WORLD_NAME = "test_world"' in register_content
        assert 'GAME_NAME = "Test Game"' in register_content
        assert 'CLIENT_FUNCTION = None' in register_content
        
        # Test validation
        processor.results = [{
            'world': 'test_world',
            'status': 'success',
            'metadata': metadata
        }]
        
        errors = processor.validate_generated_files()
        assert len(errors) == 0


if __name__ == "__main__":
    pytest.main([__file__]) 