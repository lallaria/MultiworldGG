"""
MultiworldGG Launcher for bundled app.

* If run with a patch file as argument, launch corresponding client with the patch file as an argument.
* If run with component name as argument, run it passing argv[2:] as arguments.
* If run without arguments or unknown arguments, open launcher GUI.

Additional components can be added to worlds.LauncherComponents.components.
"""

import argparse
import logging
import logging.handlers
import multiprocessing
import os
import shlex
import subprocess
import sys
import urllib.parse
import webbrowser
from collections.abc import Callable, Sequence
from os.path import isfile
from shutil import which
from typing import Any

if __name__ == "__main__":
    import ModuleUpdate

    ModuleUpdate.update()

import settings
import Utils
apname = Utils.instance_name if Utils.instance_name else "Archipelago"
from Utils import (init_logging, is_frozen, is_linux, is_macos, is_windows, local_path, messagebox, open_filename,
                   user_path)
from Updater import get_latest_release_info, download_and_install_win
from worlds.LauncherComponents import Component, components, icon_paths, SuffixIdentifier, Type

apname = "Archipelago" if not Utils.instance_name else Utils.instance_name

def open_host_yaml():
    s = settings.get_settings()
    file = s.filename
    s.save()
    assert file, "host.yaml missing"
    if is_linux:
        exe = which('sensible-editor') or which('gedit') or \
              which('xdg-open') or which('gnome-open') or which('kde-open')
    elif is_macos:
        exe = which("open")
    else:
        webbrowser.open(file)
        return

    env = os.environ
    if "LD_LIBRARY_PATH" in env:
        env = env.copy()
        del env["LD_LIBRARY_PATH"]  # exe is a system binary, so reset LD_LIBRARY_PATH
    subprocess.Popen([exe, file], env=env)

def open_patch():
    suffixes = []
    for c in components:
        if c.type == Type.CLIENT and \
                isinstance(c.file_identifier, SuffixIdentifier) and \
                (c.script_name is None or isfile(get_exe(c)[-1])):
            suffixes += c.file_identifier.suffixes
    try:
        filename = open_filename("Select patch", (("Patches", suffixes),))
    except Exception as e:
        messagebox("Error", str(e), error=True)
    else:
        file, component = identify(filename)
        if file and component:
            exe = get_exe(component)
            if exe is None or not isfile(exe[-1]):
                exe = get_exe("Launcher")

            launch([*exe, file], component.cli)


def generate_yamls():
    from Options import generate_yaml_templates

    target = Utils.user_path("Players", "Templates")
    generate_yaml_templates(target, False)
    open_folder(target)


def browse_files():
    open_folder(user_path())


def open_folder(folder_path):
    if is_linux:
        exe = which('xdg-open') or which('gnome-open') or which('kde-open')
    elif is_macos:
        exe = which("open")
    else:
        webbrowser.open(folder_path)
        return

    if exe:
        env = os.environ
        if "LD_LIBRARY_PATH" in env:
            env = env.copy()
            del env["LD_LIBRARY_PATH"]  # exe is a system binary, so reset LD_LIBRARY_PATH
        subprocess.Popen([exe, folder_path], env=env)
    else:
        logging.warning(f"No file browser available to open {folder_path}")


def update_settings():
    from settings import get_settings
    get_settings().save()


components.extend([
    # Functions
    Component("Open host.yaml", func=open_host_yaml,
                description="Open the host.yaml file to change settings for generation, games, and more."),
    Component("Open Patch", func=open_patch,
              description="Open a patch file, downloaded from the room page or provided by the host."),
    Component("Generate Template Options", func=generate_yamls,
              description="Generate template YAMLs for currently installed games."),
    Component("MultiworldGG Website", func=lambda: webbrowser.open("https://multiworld.gg/"),
              description="Open multiworld.gg in your browser."),
    Component("ZSR Discord", icon="discord", func=lambda: webbrowser.open("https://discord.gg/zsr"),
              description="Join the Discord server to play public multiworlds, report issues, or just chat!"),
    Component("Browse Files", func=browse_files,
              description="Open the Archipelago installation folder in your file browser."),
])


def handle_uri(path: str) -> tuple[list[Component], Component]:
    url = urllib.parse.urlparse(path)
    queries = urllib.parse.parse_qs(url.query)
    client_components = []
    text_client_component = None
    game = queries["game"][0]
    for component in components:
        if component.supports_uri and component.game_name == game:
            client_components.append(component)
        elif component.display_name == "Text Client":
            text_client_component = component
    return client_components, text_client_component


def build_uri_popup(component_list: list[Component], launch_args: tuple[str, ...]) -> None:
    from kvui import ButtonsPrompt
    component_options = {
        component.display_name: component for component in component_list
    }
    popup = ButtonsPrompt("Connect to Multiworld",
                          "Select client to open and connect with.",
                          lambda component_name: run_component(component_options[component_name], *launch_args),
                          *component_options.keys())
    popup.open()


def identify(path: None | str) -> tuple[None | str, None | Component]:
    if path is None:
        return None, None
    for component in components:
        if component.handles_file(path):
            return path, component
        elif path == component.display_name or path == component.script_name:
            return None, component
    return None, None


def get_exe(component: str | Component) -> Sequence[str] | None:
    if isinstance(component, str):
        name = component
        component = None
        if name.startswith(apname):
            name = name[len(apname):]
        if name.endswith(".exe"):
            name = name[:-4]
        if name.endswith(".py"):
            name = name[:-3]
        if not name:
            return None
        for c in components:
            if c.script_name == name or c.frozen_name == apname + name:
                component = c
                break
        if not component:
            return None
    if is_frozen():
        suffix = ".exe" if is_windows else ""
        return [local_path(f"{component.frozen_name}{suffix}")] if component.frozen_name else None
    else:
        return [sys.executable, local_path(f"{component.script_name}.py")] if component.script_name else None


def launch(exe, in_terminal=False):
    if in_terminal:
        if is_windows:
            # intentionally using a window title with a space so it gets quoted and treated as a title
            subprocess.Popen(["start", f"Running {apname}", *exe], shell=True)
            return
        elif is_linux:
            terminal = which('x-terminal-emulator') or which('gnome-terminal') or which('xterm')
            if terminal:
                subprocess.Popen([terminal, '-e', shlex.join(exe)])
                return
        elif is_macos:
            terminal = [which('open'), '-W', '-a', 'Terminal.app']
            subprocess.Popen([*terminal, *exe])
            return
    subprocess.Popen(exe)


def create_shortcut(button: Any, component: Component) -> None:
    from pyshortcuts import make_shortcut
    script = sys.argv[0]
    wkdir = Utils.local_path()

    script = f"{script} \"{component.display_name}\""
    make_shortcut(script, name=f"MultiworldGG {component.display_name}", icon=local_path("data", "icon.ico"),
                  startmenu=False, terminal=False, working_dir=wkdir)
    button.menu.dismiss()


refresh_components: Callable[[], None] | None = None


def run_gui(launch_components: list[Component], args: Any) -> None:
    from kvui import (ThemedApp, MDFloatLayout, MDGridLayout, ScrollBox)
    from kivy.properties import ObjectProperty
    from kivy.core.window import Window
    from kivy.metrics import dp
    from kivymd.uix.button import MDIconButton, MDButton, MDButtonText
    from kivymd.uix.card import MDCard
    from kivymd.uix.menu import MDDropdownMenu
    from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
    from kivymd.uix.textfield import MDTextField
    from kivy.clock import Clock
    from kivy.uix.widget import Widget
    from kivymd.uix.dialog import (
        MDDialog,
        MDDialogHeadlineText,
        MDDialogSupportingText,
        MDDialogButtonContainer,
        MDDialogSupportingText
    )
    from kivy.app import App
    from kivy.lang.builder import Builder

    class LauncherCard(MDCard):
        component: Component | None
        image: str
        context_button: MDIconButton = ObjectProperty(None)

        def __init__(self, *args, component: Component | None = None, image_path: str = "", **kwargs):
            self.component = component
            self.image = image_path
            super().__init__(args, kwargs)

    class Launcher(ThemedApp):
        base_title: str = apname + " Launcher"
        top_screen: MDFloatLayout = ObjectProperty(None)
        navigation: MDGridLayout = ObjectProperty(None)
        grid: MDGridLayout = ObjectProperty(None)
        button_layout: ScrollBox = ObjectProperty(None)
        search_box: MDTextField = ObjectProperty(None)
        cards: list[LauncherCard]
        current_filter: Sequence[str | Type] | None

        def __init__(self, ctx=None, components=None, args=None):
            self.title = self.base_title + " " + Utils.__version__
            self.ctx = ctx
            self.icon = r"data/icon.png"
            self.favorites = []
            self.launch_components = components
            self.launch_args = args
            self.cards = []
            self.current_filter = (Type.CLIENT, Type.TOOL, Type.ADJUSTER, Type.MISC)
            persistent = Utils.persistent_load()
            if "launcher" in persistent:
                if "favorites" in persistent["launcher"]:
                    self.favorites.extend(persistent["launcher"]["favorites"])
                if "filter" in persistent["launcher"]:
                    if persistent["launcher"]["filter"]:
                        filters = []
                        for filter in persistent["launcher"]["filter"].split(", "):
                            if filter == "favorites":
                                filters.append(filter)
                            else:
                                filters.append(Type[filter])
                        self.current_filter = filters
            super().__init__()

        def set_favorite(self, caller):
            if caller.component.display_name in self.favorites:
                self.favorites.remove(caller.component.display_name)
                caller.icon = "star-outline"
            else:
                self.favorites.append(caller.component.display_name)
                caller.icon = "star"

        def build_card(self, component: Component) -> LauncherCard:
            """
                Builds a card widget for a given component.

                :param component: The component associated with the button.

                :return: The created Card Widget.
                """
            button_card = LauncherCard(component=component,
                                       image_path=icon_paths[component.icon])

            def open_menu(caller):
                caller.menu.open()

            menu_items = [
                {
                    "text": "Add shortcut on desktop",
                    "leading_icon": "laptop",
                    "on_release": lambda: create_shortcut(button_card.context_button, component)
                }
            ]
            button_card.context_button.menu = MDDropdownMenu(caller=button_card.context_button, items=menu_items)
            button_card.context_button.bind(on_release=open_menu)

            return button_card

        def _refresh_components(self, type_filter: Sequence[str | Type] | None = None) -> None:
            if not type_filter:
                type_filter = [Type.CLIENT, Type.ADJUSTER, Type.TOOL, Type.MISC]
            favorites = "favorites" in type_filter

            # clear before repopulating
            assert self.button_layout, "must call `build` first"
            tool_children = reversed(self.button_layout.layout.children)
            for child in tool_children:
                self.button_layout.layout.remove_widget(child)

            cards = [card for card in self.cards if card.component.type in type_filter
                     or favorites and card.component.display_name in self.favorites]

            self.current_filter = type_filter

            for card in cards:
                self.button_layout.layout.add_widget(card)

            top = self.button_layout.children[0].y + self.button_layout.children[0].height \
                           - self.button_layout.height
            scroll_percent = self.button_layout.convert_distance_to_scroll(0, top)
            self.button_layout.scroll_y = max(0, min(1, scroll_percent[1]))

        def filter_clients_by_type(self, caller: MDButton):
            self._refresh_components(caller.type)
            self.search_box.text = ""

        def filter_clients_by_name(self, caller: MDTextField, name: str) -> None:
            if len(name) == 0:
                self._refresh_components(self.current_filter)
                return

            sub_matches = [
                card for card in self.cards
                if name.lower() in card.component.display_name.lower() and card.component.type != Type.HIDDEN
            ]
            self.button_layout.layout.clear_widgets()
            for card in sub_matches:
                self.button_layout.layout.add_widget(card)

        def build(self):
            self.top_screen = Builder.load_file(Utils.local_path("data/launcher.kv"))
            self.grid = self.top_screen.ids.grid
            self.navigation = self.top_screen.ids.navigation
            self.button_layout = self.top_screen.ids.button_layout
            self.search_box = self.top_screen.ids.search_box
            self.set_colors()
            self.top_screen.md_bg_color = self.theme_cls.backgroundColor

            global refresh_components
            refresh_components = self._refresh_components
            Window.size = (1100, 920)
            Window.bind(on_drop_file=self._on_drop_file)
            Window.bind(on_keyboard=self._on_keyboard)

            for component in components:
                self.cards.append(self.build_card(component))

            self._refresh_components(self.current_filter)

            # Uncomment to re-enable the Kivy console/live editor
            # Ctrl-E to enable it, make sure numlock/capslock is disabled
            # from kivy.modules.console import create_console
            # create_console(Window, self.top_screen)

            return self.top_screen

        def on_start(self):
            if self.launch_components:
                build_uri_popup(self.launch_components, self.launch_args)
                self.launch_components = None
                self.launch_args = None

            if is_frozen() and is_windows:
                Clock.schedule_once(self._maybe_show_update_dialog, 1.0)

        def _maybe_show_update_dialog(self, dt):
            try:
                latest_ver, download_url = get_latest_release_info()
            except Exception as e:
                logging.warning("Launcher update check failed: %s", e)
                return

            if latest_ver > Utils.version_tuple:

                dialog = MDDialog(
                    MDDialogHeadlineText(
                        text="Update Available",
                        halign="center",
                    ),
                    MDDialogSupportingText(
                        text=(
                            f"A new version of {Utils.instance_name} is available: "
                            f"{latest_ver.as_simple_string()}\n\n"
                            f"You are currently running version {Utils.version_tuple.as_simple_string()}.\n\n"
                            "Download and install the update now?"
                        ),
                        halign="left",
                    ),
                    MDDialogButtonContainer(
                        Widget(),
                        MDButton(
                            MDButtonText(text="Later"),
                            style="text",
                            on_release=lambda *a: dialog.dismiss()
                        ),

                        MDButton(
                            MDButtonText(text="Update Now"),
                            style="filled",
                            on_release=lambda *a: self._on_user_requested_update(dialog, download_url)
                        ),
                        spacing="8dp",
                    ),
                    size_hint=(0.8, None),
                )

                dialog.height = dp(200)
                dialog.open()

        def _on_user_requested_update(self, dialog, download_url):
            dialog.dismiss()

            downloading = MDDialog(
                MDDialogSupportingText(
                    text="Downloading update…",
                    halign="center"
                ),
                size_hint=(0.6, None),
            )
            downloading.height = dp(100)
            downloading.open()

            Clock.schedule_once(lambda dt: self._finalize_update(dialog, download_url), 0.5)

        def _finalize_update(self, dialog: MDDialog, download_url: str):
            dialog.dismiss()
            download_and_install_win(download_url)
            self.stop()

        @staticmethod
        def component_action(button):
            MDSnackbar(MDSnackbarText(text="Opening in a new window..."), y=dp(24), pos_hint={"center_x": 0.5},
                       size_hint_x=0.5).open()
            if button.component.func:
                button.component.func()
            else:
                launch(get_exe(button.component), button.component.cli)

        def _on_drop_file(self, window: Window, filename: bytes, x: int, y: int) -> None:
            """ When a patch file is dropped into the window, run the associated component. """
            file, component = identify(filename.decode())
            if file and component:
                run_component(component, file)
            else:
                logging.warning(f"unable to identify component for {filename}")

        def _on_keyboard(self, window: Window, key: int, scancode: int, codepoint: str, modifier: list[str]):
            # Activate search as soon as we start typing, no matter if we are focused on the search box or not.
            # Focus first, then capture the first character we type, otherwise it gets swallowed and lost.
            # Limit text input to ASCII non-control characters (space bar to tilde).
            if not self.search_box.focus:
                self.search_box.focus = True
                if key in range(32, 126):
                    self.search_box.text += codepoint

        def _stop(self, *largs):
            # ran into what appears to be https://groups.google.com/g/kivy-users/c/saWDLoYCSZ4 with PyCharm.
            # Closing the window explicitly cleans it up.
            self.root_window.close()
            super()._stop(*largs)

        def on_stop(self):
            Utils.persistent_store("launcher", "favorites", self.favorites)
            Utils.persistent_store("launcher", "filter", ", ".join(filter.name if isinstance(filter, Type) else filter
                                                                   for filter in self.current_filter))
            super().on_stop()

    Launcher(components=launch_components, args=args).run()

    # avoiding Launcher reference leak
    # and don't try to do something with widgets after window closed
    global refresh_components
    refresh_components = None


def run_component(component: Component, *args):
    if component.func:
        component.func(*args)
        if refresh_components:
            refresh_components()
    elif component.script_name:
        subprocess.run([*get_exe(component.script_name), *args])
    else:
        logging.warning(f"Component {component} does not appear to be executable.")


def main(args: argparse.Namespace | dict | None = None):
    if isinstance(args, argparse.Namespace):
        args = {k: v for k, v in args._get_kwargs()}
    elif not args:
        args = {}

    path = args.get("Patch|Game|Component|url", None)
    if path is not None:
        if path.startswith("archipelago://") or path.startswith("mwgg://"):
            args["args"] = (path, *args.get("args", ()))
            # add the url arg to the passthrough args
            components, text_client_component = handle_uri(path)
            if not components:
                args["component"] = text_client_component
            else:
                args['launch_components'] = [text_client_component, *components]
        else:
            file, component = identify(path)
            if file:
                args['file'] = file
            if component:
                args['component'] = component
            if not component:
                logging.warning(f"Could not identify Component responsible for {path}")

    if args["update_settings"]:
        update_settings()
    if "file" in args:
        run_component(args["component"], args["file"], *args["args"])
    elif "component" in args:
        run_component(args["component"], *args["args"])
    elif not args["update_settings"]:
        run_gui(args.get("launch_components", None), args.get("args", ()))


if __name__ == '__main__':
    init_logging('Launcher')
    Utils.freeze_support()
    multiprocessing.set_start_method("spawn")  # if launched process uses kivy, fork won't work
    parser = argparse.ArgumentParser(
        description=f'{apname} Launcher',
        usage="[-h] [--update_settings] [Patch|Game|Component] [-- component args here]"
    )
    run_group = parser.add_argument_group("Run")
    run_group.add_argument("--update_settings", action="store_true",
                           help="Update host.yaml and exit.")
    run_group.add_argument("Patch|Game|Component|url", type=str, nargs="?",
                           help="Pass either a patch file, a generated game, the component name to run, or a url to "
                                "connect with.")
    run_group.add_argument("args", nargs="*",
                           help="Arguments to pass to component.")
    main(parser.parse_args())

    from worlds.LauncherComponents import processes

    for process in processes:
        # we await all child processes to close before we tear down the process host
        # this makes it feel like each one is its own program, as the Launcher is closed now
        process.join()
