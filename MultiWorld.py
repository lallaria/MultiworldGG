import asyncio
import sys
import logging
import os
import re
from Utils import discover_and_launch_module

worlds_modules_dir = os.path.abspath(os.path.join("worlds", "Lib"))
if worlds_modules_dir not in sys.path:
    sys.path.insert(0, worlds_modules_dir)

import gui.Gui

logger = logging.getLogger("MultiWorld")

def run_client(*args):
    """Start the MWGG client"""
    async def main(args):
        from CommonClient import InitContext
        ctx = InitContext()
        
        # Check if a specific module was requested
        if len(args) > 1 and args[1].startswith("--game="):
            game_name = args[1].split("=")[1]
            logger.info(f"Attempting to launch game: {game_name}")
            
            # Try to launch the module via entrypoints
            try:
                discover_and_launch_module(game_name, args)
                return  # Module takeover successful, exit initial client
            except Exception as e:
                logger.error(f"Module launch failed: {e}")
                # Fall back to initial client
                logger.info("Falling back to initial client")
        
        # Default initial client behavior
        logger.info("Launching default GUI")
        ctx.run_gui()

        await ctx.exit_event.wait()
        await ctx.shutdown()
        sys.exit()

    asyncio.run(main(args))

if __name__ == "__main__":
   run_client(*sys.argv[1:])