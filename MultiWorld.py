import asyncio
import sys
import importlib.metadata
import logging

import gui.Gui

logger = logging.getLogger("MultiWorld")

def discover_and_launch_module(module_name: str, args):
    """Discover and launch module via entrypoints"""
    try:
        # Discover entrypoints for mwgg.plugins
        entry_points = importlib.metadata.entry_points()
        plugin_entry_points = entry_points.get("mwgg.plugins", {})
        
        client_entry_key = f"{module_name}.Client"
        if client_entry_key in plugin_entry_points:
            # Load and execute the CLIENT_FUNCTION entrypoint
            entry_point = plugin_entry_points[client_entry_key]
            launch_function = entry_point.load()
            return launch_function(args)
        else:
            raise ValueError(f"Client entrypoint for module {module_name} not found")
            
    except Exception as e:
        logger.error(f"Failed to launch module {module_name}: {e}")
        raise

def run_client(*args):
    """Run the client with the given arguments."""
    async def main(args):
        from CommonClient import InitContext
        ctx = InitContext()
        
        # Check if a specific module was requested
        if len(args) > 1 and args[1].startswith("--module="):
            module_name = args[1].split("=")[1]
            logger.info(f"Attempting to launch module: {module_name}")
            
            # Try to launch the module via entrypoints
            try:
                discover_and_launch_module(module_name, args)
                return  # Module takeover successful, exit initial client
            except Exception as e:
                logger.error(f"Module launch failed: {e}")
                # Fall back to initial client
                logger.info("Falling back to initial client")
        
        # Default initial client behavior
        ctx.run_gui()

        await ctx.exit_event.wait()
        await ctx.shutdown()
        sys.exit()

    asyncio.run(main(args))

if __name__ == "__main__":
   run_client(*sys.argv[1:])