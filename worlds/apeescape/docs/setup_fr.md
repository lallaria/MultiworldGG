# Ape Escape - Guide de configuration

## Logiciels Requis

- [MultiworldGG](https://github.com/MultiworldGG/MultiworldGG/releases). Veuillez utiliser la version 0.7.80 ou ultérieure pour le support intégré dans Bizhawk.

- Fichier ISO ou BIN/CUE Ape Escape (USA).

- [BizHawk](https://tasvideos.org/BizHawk/ReleaseHistory) version 2.7 à 2.9.1. La version 2.10 de BizHawk ou tout autre émulateur n'est pas pris en charge.

- (N'est pas necessaire avec MWGG:) Le fichier `apeescape.apworld` le plus récent. Vous pouvez le trouver sur la [page GitHub](https://github.com/Thedragon005/Archipelago-Ape-Escape/releases/latest). Déposer le fichier dans le dossier `MultiworldGG/custom_worlds`.

### Configuration de BizHawk

Après avoir installé BizHawk, ouvrez `EmuHawk.exe` et allez changer les configurations suivantes :

- Si vous utilisez la version 2.7 ou 2.8 de Bizhawk, naviguez jusqu'à `Config > Customize`. Dans l'onglet `Advanced`, changez le paramètre Lua Core de `NLua+KopiLua` à `Lua+LuaInterface`, ensuite redémarrer EmuHawk. (Si vous utilisez la version 2.9 de BizHawk, vous pouvez passer cette étape.)

- Sous `Config > Customize`, cochez la case "Run in background" pour empêcher la déconnexion du client quand Bizhawk s'exécute en arrière-plan.

- Ouvrez n'importe quel jeu PlayStation dans EmuHawk et allez dans `Config > Controllers…` pour configurer les entrées. Si vous ne pouvez pas cliquer sur `Controllers…`, c'est parce qu'il faut charger un jeu d'abord.

- Envisagez d'effacer les raccourcis clavier dans `Config > Hotkeys…` si vous ne prévoyez pas les utiliser. Sélectionnez le raccourci, puis appuyez sur Esc pour l'effacer.

## Générer une partie

1. Créez votre fichier de configuration (YAML). Après avoir installé le fichier `apeescape.apworld`, vous pouvez générer un modèle dans le menu MultiworldGG Launcher en cliquant sur l'option `Generate Template Settings`.

2. Suivez les instructions générales d'MultiworldGG pour [Générer une partie](https://multiworld.gg/tutorial/Archipelago/setup/en#generating-a-game) (En anglais).

3. Ouvrez `MultiworldGGLauncher.exe`

4. Sélectionnez "BizHawk Client" dans la colonne de droite. À la première ouverture, on vous demandera également de repérer `EmuHawk.exe` dans votre installation de Bizhawk.

## Se connecter à un Serveur

1. Si EmuHawk n'a pas démarré automatiquement, ouvrez-le manuellement.

2. Ouvrez votre fichier ISO ou CUE d'Ape Escape (USA) dans EmuHawk.

3. Dans EmuHawk, allez à `Tools > Lua Console`. Cette fenêtre doit rester ouverte quand vous jouez. Faites attention de ne pas cliquer sur "TAStudio" directement en dessous, car cela est connu pour supprimer votre sauvegarde.

4. Dans la fenêtre Lua Console, allez à `Script > Open Script…`.

5. Naviguez jusqu'à votre répertoire d'installation MultiworldGG et ouvrez `data/lua/connector_bizhawk_generic.lua`.

6. L'émulateur et le client vont éventuellement se connecter l'un à l'autre. La fenêtre Bizhawk Client devrait indiquer qu'il s'est connecté et a reconnu Ape Escape.

7. Pour connecter le client au serveur, entrez l'adresse de la salle et le port (ex. `multiworld.gg:38281`) dans le champ situé en haut du client et appuyez sur Connect.

Vous devriez maintenant être en mesure de recevoir et d'envoyer des objets. Vous devrez faire ces étapes chaque fois que vous voulez vous reconnecter.

## Conseils sur la configuration des joysticks pour Ape Escape dans Bizhawk

La sensibilité des joysticks dans Bizhawk peut être un peu difficile à faire fonctionner au début. Vous pourriez avoir besoin de les relier à l'inverse de ce à quoi vous pourriez vous attendre.La première fois, vous voudrez aller au menu en haut de Bizhawk, cliquer sur PSX, ouvrir Settings,aller à l'onglet Sync Settings, défiler légèrement vers le bas, et s'assurer que l'option Virtual Port 1 est réglée sur dualanalog. Si vous ne le faites pas, les joysticks vont être un peu étranges quand vous allez courir exactement vers la droite.
