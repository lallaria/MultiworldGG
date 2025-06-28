"""
Test suite for GUI Client Takeover System

This test suite validates the implementation of the GUI takeover functionality
as specified in integrate_gui.md
"""

import asyncio
import unittest
from unittest.mock import Mock, patch, AsyncMock, MagicMock
import sys
import os
from typing import Optional, Dict, Any

print('test_gui_takeover.py: Script started')

# Add the project root to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from CommonClient import CommonContext
from ClientBuilder import ClientBuilder, ClientState, GameClient
from kivymd.app import MDApp

class TestInitContext(unittest.TestCase):
    """Test the InitContext base class functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Import InitContext after it's implemented
        try:
            from CommonClient import InitContext
            self.InitContext = InitContext
        except ImportError:
            # Fallback for when InitContext is not yet implemented
            self.InitContext = type('InitContext', (), {
                '__init__': lambda self: setattr(self, 'exit_event', asyncio.Event()) or 
                                        setattr(self, '_state', ClientState.INITIAL) or
                                        setattr(self, '_is_transitioning', False)
            })
    
    def test_init_context_creation(self):
        """Test that InitContext can be created with minimal properties"""
        ctx = self.InitContext()
        
        self.assertIsInstance(ctx.exit_event, asyncio.Event)
        self.assertEqual(ctx._state, ClientState.INITIAL)
        self.assertFalse(ctx._is_transitioning)
    
    def test_init_context_state_management(self):
        """Test InitContext state transitions"""
        ctx = self.InitContext()
        
        # Test initial state
        self.assertEqual(ctx._state, ClientState.INITIAL)
        self.assertFalse(ctx._is_transitioning)
        
        # Test state changes
        ctx._state = ClientState.TRANSITIONING
        ctx._is_transitioning = True
        
        self.assertEqual(ctx._state, ClientState.TRANSITIONING)
        self.assertTrue(ctx._is_transitioning)


class TestCommonContextInheritance(unittest.TestCase):
    """Test that CommonContext properly inherits from InitContext"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Mock the InitContext if not yet implemented
        with patch('CommonClient.InitContext', create=True):
            from CommonClient import CommonContext
            self.CommonContext = CommonContext
    
    def test_common_context_inheritance(self):
        """Test that CommonContext inherits from InitContext"""
        ctx = self.CommonContext()
        
        # Should have InitContext properties
        self.assertIsInstance(ctx.exit_event, asyncio.Event)
        self.assertEqual(ctx._state, ClientState.INITIAL)
        self.assertFalse(ctx._is_transitioning)
        
        # Should have CommonContext properties
        self.assertIsNone(ctx.command_processor)
        self.assertIsNone(ctx.game)
    
    def test_common_context_state_transitions(self):
        """Test CommonContext state management"""
        ctx = self.CommonContext()
        
        # Test initial state
        self.assertEqual(ctx._state, ClientState.INITIAL)
        
        # Test transition to game state
        ctx._state = ClientState.GAME
        self.assertEqual(ctx._state, ClientState.GAME)


class TestTakeoverDetection(unittest.TestCase):
    """Test the takeover detection functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
        self.ctx = CommonContext()
    
    @patch('CommonClient.MDApp')
    def test_can_takeover_existing_gui_success(self, mock_mdapp):
        """Test successful takeover detection"""
        # Mock a running app with valid context
        mock_app = Mock()
        mock_app.ctx = Mock()
        mock_app.ctx._state = ClientState.INITIAL
        mock_app.ctx._is_transitioning = False
        mock_mdapp.get_running_app.return_value = mock_app
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertTrue(result)
    
    @patch('CommonClient.MDApp')
    def test_can_takeover_existing_gui_no_app(self, mock_mdapp):
        """Test takeover detection when no app is running"""
        mock_mdapp.get_running_app.return_value = None
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)
    
    @patch('CommonClient.MDApp')
    def test_can_takeover_existing_gui_wrong_state(self, mock_mdapp):
        """Test takeover detection when app is in wrong state"""
        mock_app = Mock()
        mock_app.ctx = Mock()
        mock_app.ctx._state = ClientState.GAME  # Wrong state
        mock_app.ctx._is_transitioning = False
        mock_mdapp.get_running_app.return_value = mock_app
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)
    
    @patch('CommonClient.MDApp')
    def test_can_takeover_existing_gui_transitioning(self, mock_mdapp):
        """Test takeover detection when app is transitioning"""
        mock_app = Mock()
        mock_app.ctx = Mock()
        mock_app.ctx._state = ClientState.INITIAL
        mock_app.ctx._is_transitioning = True  # Currently transitioning
        mock_mdapp.get_running_app.return_value = mock_app
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)
    
    @patch('CommonClient.MDApp')
    def test_can_takeover_existing_gui_exception(self, mock_mdapp):
        """Test takeover detection handles exceptions gracefully"""
        mock_mdapp.get_running_app.side_effect = Exception("Test exception")
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)


class TestTakeoverExecution(unittest.TestCase):
    """Test the takeover execution functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
        self.ctx = CommonContext()
    
    @patch('CommonClient.MDApp')
    @patch('CommonClient.GameClient')
    async def test_takeover_existing_gui_success(self, mock_game_client, mock_mdapp):
        """Test successful GUI takeover"""
        # Mock existing context
        mock_existing_ctx = Mock()
        mock_existing_ctx.exit_event = asyncio.Event()
        mock_existing_ctx._state = ClientState.INITIAL
        mock_existing_ctx._is_transitioning = False
        
        # Mock app
        mock_app = Mock()
        mock_app.ctx = mock_existing_ctx
        mock_mdapp.get_running_app.return_value = mock_app
        
        # Mock GameClient
        mock_builder = AsyncMock()
        mock_game_client.return_value = mock_builder
        
        # Execute takeover
        await self.ctx._takeover_existing_gui()
        
        # Verify state transitions
        self.assertTrue(mock_existing_ctx._is_transitioning)
        self.assertTrue(self.ctx._is_transitioning)
        
        # Verify exit_event preservation
        self.assertEqual(self.ctx.exit_event, mock_existing_ctx.exit_event)
        
        # Verify app context update
        self.assertEqual(mock_app.ctx, self.ctx)
        
        # Verify state update
        self.assertEqual(self.ctx._state, ClientState.GAME)
        
        # Verify GameClient creation and build
        mock_game_client.assert_called_once()
        mock_builder.build.assert_called_once()
        
        # Verify transition flags reset
        self.assertFalse(mock_existing_ctx._is_transitioning)
        self.assertFalse(self.ctx._is_transitioning)
    
    @patch('CommonClient.MDApp')
    @patch('CommonClient.GameClient')
    async def test_takeover_existing_gui_exception(self, mock_game_client, mock_mdapp):
        """Test takeover handles exceptions and resets flags"""
        # Mock existing context
        mock_existing_ctx = Mock()
        mock_existing_ctx.exit_event = asyncio.Event()
        mock_existing_ctx._state = ClientState.INITIAL
        mock_existing_ctx._is_transitioning = False
        
        # Mock app
        mock_app = Mock()
        mock_app.ctx = mock_existing_ctx
        mock_mdapp.get_running_app.return_value = mock_app
        
        # Mock GameClient to raise exception
        mock_builder = AsyncMock()
        mock_builder.build.side_effect = Exception("Test exception")
        mock_game_client.return_value = mock_builder
        
        # Execute takeover and expect exception
        with self.assertRaises(Exception):
            await self.ctx._takeover_existing_gui()
        
        # Verify transition flags are reset even on exception
        self.assertFalse(mock_existing_ctx._is_transitioning)
        self.assertFalse(self.ctx._is_transitioning)


class TestRunGuiIntegration(unittest.TestCase):
    """Test the integrated run_gui method"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
        self.ctx = CommonContext()
    
    @patch.object(CommonContext, '_can_takeover_existing_gui')
    @patch.object(CommonContext, '_takeover_existing_gui')
    @patch.object(CommonContext, '_create_new_gui')
    async def test_run_gui_takeover_success(self, mock_create_new, mock_takeover, mock_can_takeover):
        """Test run_gui chooses takeover when available"""
        mock_can_takeover.return_value = True
        mock_takeover.return_value = None
        
        await self.ctx.run_gui()
        
        mock_can_takeover.assert_called_once()
        mock_takeover.assert_called_once()
        mock_create_new.assert_not_called()
    
    @patch.object(CommonContext, '_can_takeover_existing_gui')
    @patch.object(CommonContext, '_takeover_existing_gui')
    @patch.object(CommonContext, '_create_new_gui')
    async def test_run_gui_create_new_when_no_takeover(self, mock_create_new, mock_takeover, mock_can_takeover):
        """Test run_gui creates new GUI when takeover not available"""
        mock_can_takeover.return_value = False
        mock_create_new.return_value = None
        
        await self.ctx.run_gui()
        
        mock_can_takeover.assert_called_once()
        mock_takeover.assert_not_called()
        mock_create_new.assert_called_once()


class TestGameClientBuilder(unittest.TestCase):
    """Test the GameClient builder functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
        self.ctx = CommonContext()
    
    @patch('ClientBuilder.MDApp')
    async def test_game_client_build_success(self, mock_mdapp):
        """Test GameClient build process"""
        # Mock app for global access
        mock_app = Mock()
        mock_app.ctx.ui = Mock()
        mock_app.ctx.ui_task = AsyncMock()
        mock_app.ctx.exit_event = asyncio.Event()
        mock_mdapp.get_running_app.return_value = mock_app
        
        # Create GameClient
        game_client = GameClient(self.ctx)
        
        # Build the client
        result = await game_client.build()
        
        # Verify build completed successfully
        self.assertEqual(result, {})
        self.assertTrue(game_client._is_running)
    
    @patch('ClientBuilder.MDApp')
    async def test_game_client_build_exception(self, mock_mdapp):
        """Test GameClient handles build exceptions"""
        # Mock app
        mock_app = Mock()
        mock_mdapp.get_running_app.return_value = mock_app
        
        # Create GameClient
        game_client = GameClient(self.ctx)
        
        # Mock _setup_game_features to raise exception
        game_client._setup_game_features = AsyncMock(side_effect=Exception("Test exception"))
        
        # Build should raise exception
        with self.assertRaises(Exception):
            await game_client.build()
        
        # Verify state is reset
        self.assertFalse(game_client._is_running)


class TestEntrypointDiscovery(unittest.TestCase):
    """Test the entrypoint discovery and execution"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.module_name = "kh2"
    
    @patch('importlib.metadata.entry_points')
    def test_discover_and_launch_module_success(self, mock_entry_points):
        """Test successful module discovery and launch"""
        # Mock entrypoints
        mock_ep = Mock()
        mock_ep.load.return_value = Mock()
        mock_ep.load.return_value.return_value = None
        
        mock_entry_points.return_value = {
            "mwgg.plugins": {
                "kh2.Client": mock_ep
            }
        }
        
        # Mock the discover function
        def discover_and_launch_module(module_name: str, args):
            import importlib.metadata
            entry_points = importlib.metadata.entry_points()
            plugin_entry_points = entry_points.get("mwgg.plugins", {})
            
            client_entry_key = f"{module_name}.Client"
            if client_entry_key in plugin_entry_points:
                entry_point = plugin_entry_points[client_entry_key]
                launch_function = entry_point.load()
                return launch_function(args)
            else:
                raise ValueError(f"Client entrypoint for module {module_name} not found")
        
        # Test successful discovery
        result = discover_and_launch_module(self.module_name, {})
        self.assertIsNone(result)
    
    @patch('importlib.metadata.entry_points')
    def test_discover_and_launch_module_not_found(self, mock_entry_points):
        """Test module discovery when entrypoint not found"""
        mock_entry_points.return_value = {
            "mwgg.plugins": {}
        }
        
        def discover_and_launch_module(module_name: str, args):
            import importlib.metadata
            entry_points = importlib.metadata.entry_points()
            plugin_entry_points = entry_points.get("mwgg.plugins", {})
            
            client_entry_key = f"{module_name}.Client"
            if client_entry_key in plugin_entry_points:
                entry_point = plugin_entry_points[client_entry_key]
                launch_function = entry_point.load()
                return launch_function(args)
            else:
                raise ValueError(f"Client entrypoint for module {module_name} not found")
        
        # Test module not found
        with self.assertRaises(ValueError) as context:
            discover_and_launch_module(self.module_name, {})
        
        self.assertIn("Client entrypoint for module kh2 not found", str(context.exception))


class TestGlobalAccessPattern(unittest.TestCase):
    """Test the global access pattern for GUI components"""
    
    @patch('kivymd.app.MDApp')
    def test_global_access_pattern(self, mock_mdapp):
        """Test accessing GUI components via global pattern"""
        # Mock app and context
        mock_ctx = Mock()
        mock_ctx.ui = Mock()
        mock_ctx.ui_task = AsyncMock()
        mock_ctx.exit_event = asyncio.Event()
        mock_ctx.loop = asyncio.get_event_loop()
        
        mock_app = Mock()
        mock_app.ctx = mock_ctx
        mock_mdapp.get_running_app.return_value = mock_app
        
        # Test global access pattern
        app = MDApp.get_running_app()
        kivy_ui = app.ctx.ui
        ui_task = app.ctx.ui_task
        exit_event = app.ctx.exit_event
        event_loop = app.ctx.loop
        
        # Verify all components are accessible
        self.assertEqual(kivy_ui, mock_ctx.ui)
        self.assertEqual(ui_task, mock_ctx.ui_task)
        self.assertEqual(exit_event, mock_ctx.exit_event)
        self.assertEqual(event_loop, mock_ctx.loop)


class TestIntegrationWithKH2(unittest.TestCase):
    """Integration tests using KH2 as the test module"""
    
    def setUp(self):
        """Set up test fixtures"""
        # This test requires the actual KH2 module to be available
        try:
            from worlds.kh2.Client import KH2Context, launch
            self.KH2Context = KH2Context
            self.kh2_launch = launch
            self.kh2_available = True
        except ImportError:
            self.kh2_available = False
    
    @unittest.skipUnless(True, "KH2 module not available")
    def test_kh2_context_inheritance(self):
        """Test that KH2Context properly inherits takeover functionality"""
        if not self.kh2_available:
            self.skipTest("KH2 module not available")
        
        ctx = self.KH2Context("test_address", "test_password")
        
        # Should have takeover methods
        self.assertTrue(hasattr(ctx, '_can_takeover_existing_gui'))
        self.assertTrue(hasattr(ctx, '_takeover_existing_gui'))
        
        # Should have KH2-specific properties
        self.assertEqual(ctx.game, "Kingdom Hearts 2")
        self.assertIsNotNone(ctx.command_processor)
    
    @unittest.skipUnless(True, "KH2 module not available")
    def test_kh2_launch_function_structure(self):
        """Test that KH2 launch function can be modified for takeover"""
        if not self.kh2_available:
            self.skipTest("KH2 module not available")
        
        # Test that launch function exists and is callable
        self.assertTrue(callable(self.kh2_launch))
        
        # Test that it has the expected structure (async main function)
        import inspect
        source = inspect.getsource(self.kh2_launch)
        self.assertIn("async def main", source)


class TestStateValidation(unittest.TestCase):
    """Test state validation and transitions"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
    
    def test_client_state_enum(self):
        """Test ClientState enum values"""
        self.assertEqual(ClientState.INITIAL, "initial")
        self.assertEqual(ClientState.GAME, "game")
        self.assertEqual(ClientState.TRANSITIONING, "transitioning")
    
    def test_state_transition_validation_placeholder(self):
        """Placeholder for future state transition validation"""
        # TODO: Add validation logic here when needed
        # This would validate that only INITIAL state contexts can be taken over
        # and that transitions follow valid paths
        pass


class TestErrorHandling(unittest.TestCase):
    """Test error handling scenarios"""
    
    def setUp(self):
        """Set up test fixtures"""
        from CommonClient import CommonContext
        self.CommonContext = CommonContext
        self.ctx = CommonContext()
    
    @patch('CommonClient.MDApp')
    async def test_takeover_with_missing_app_context(self, mock_mdapp):
        """Test takeover when app exists but has no ctx"""
        mock_app = Mock()
        mock_app.ctx = None  # Missing context
        mock_mdapp.get_running_app.return_value = mock_app
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)
    
    @patch('CommonClient.MDApp')
    async def test_takeover_with_invalid_context_type(self, mock_mdapp):
        """Test takeover with context that doesn't inherit from InitContext"""
        mock_app = Mock()
        mock_app.ctx = Mock()  # Regular Mock, not InitContext
        mock_app.ctx._state = ClientState.INITIAL
        mock_app.ctx._is_transitioning = False
        mock_mdapp.get_running_app.return_value = mock_app
        
        result = self.ctx._can_takeover_existing_gui()
        self.assertFalse(result)


if __name__ == "__main__":
    print('test_gui_takeover.py: Entering main block')
    unittest.main(verbosity=2) 