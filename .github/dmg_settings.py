import os

application = os.environ.get("MACOS_APP", "MultiworldGG.app")

files = [application]

symlinks = {'Applications': '/Applications'}

format = 'UDZO'
size = '500M'

window_rect = ((100, 100), (640, 280))
icon_locations = {
    application: (140, 120),
    'Applications': (500, 120)
}

background = 'builtin-arrow'