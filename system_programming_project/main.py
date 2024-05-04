import gi
import os
import re
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import webbrowser

"""
Сделать выходящий список под ответами
"""

class SpotlightWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Spotlight Search")
        # self.integration = Integration()

        # Set window properties
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(700, 80)

        # Set transparency
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)
            self.set_app_paintable(True)
            self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 0, 0))

        # Create widgets
        self.grid = Gtk.Grid()
        self.search_entry = Gtk.Entry()
        self.treeview = Gtk.TreeView()
        self.grid.attach(self.search_entry, 0, 1, 1, 1)

        # Create a Gtk.Entry widget
        self.search_entry.set_placeholder_text("Search...")
        self.search_entry.connect("activate", self.on_search_activate)
        self.search_entry.set_activates_default(True)
        self.search_entry.set_size_request(700, 80)
        
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            entry {
                border-radius: 25px;
                font-size: 25px;
                color: white;
                background-color: rgba(0, 0, 0, 0.8);
            }
        """)

        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # Connect key-press-event signal
        self.connect("key-press-event", self.on_key_press)
        self.add(self.grid)

        self.show_all()

    def on_search_activate(self, entry):

        patterns = {
            # 'calculator': (r'(\d+\.?\d*)([+\-*/])(\d+\.?\d*)', calculate),
            # 'calendar': (r'\b(calendar|date)\b', show_calendar),
            # Add more patterns and actions here as needed
        }

        # if re.findall()
        search_text = entry.get_text()
        request = search_text.split(" ")
        webbrowser.open_new_tab(f'https://www.google.com/search?q={"+".join(request)}')

    def on_key_press(self, widget, event):
        # Close window when Escape key is pressed
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

if __name__ == "__main__":
    win = SpotlightWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
