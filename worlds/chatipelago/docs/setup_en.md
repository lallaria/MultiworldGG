# Chatipeligo Start Guide

Install the Chatipelago Client via https://www.github.com/lallaria/Chatipelago/ - currently you will have to download the zip of 
the code and extract it to a folder.

This requires installing node.js and npm, which you can find at https://nodejs.org/en/. Once you have it installed, you can run the following:

npm install 

This is still in development, so you should have some experience with node and be comfortable with the command line.

Import all of the files in the 'mixitup' folder into MixItUp chatbot. They are named in accordance with the Menu item that they need to 
be imported into (Command, Webhook, etc), ensure that the URL is set to wherever you're hosting the Chatipelago Client (probably localhost).
Check through all of the imports to ensure they're hooked in correctly - some of them need to be re-referenced to the correct command.

If you don't want to use the mixitup chatbot, you can use anything with a webhook. It's still in development, but streamer.bot would
also work. You will need to set up the commands and webhooks manually.

Retrieve the webhook URL from MixItUp (or elsewhere) and paste it into the config.json file in the Chatipelago Client folder.  Additionally, 
set the hostname and port to the Multiworld.gg hostname and port (or archipelago, or localhost, etc)

Once configured, you can run the client with the command:
npm run

