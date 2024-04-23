import gi
import os
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class SpotlightWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Spotlight Search")

        # Set window properties
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_default_size(700, 80)

        # Add CSS to customize appearance
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            window {
                background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
                border-radius: 20px; /* Rounded corners */

            }
            entry {
                background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
                border-radius: 20px; /* Rounded corners */
            }
        """)
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        # Create search entry
        self.search_entry = Gtk.Entry()
        self.search_entry.set_placeholder_text("Search...")
        self.search_entry.connect("activate", self.on_search_activate)

        # Add search entry to window
        self.add(self.search_entry)

        # Connect key-press-event signal
        self.connect("key-press-event", self.on_key_press)

        # Show all widgets
        self.show_all()

    def on_search_activate(self, entry):
        search_text = entry.get_text()
        request = search_text.split(" ")
        subprocess.run(['gio', 'open', f'https://www.google.com/search?q={"+".join(request)}'])

    def on_key_press(self, widget, event):
        # Close window when Escape key is pressed
        if event.keyval == Gdk.KEY_Escape:
            Gtk.main_quit()

if __name__ == "__main__":
    win = SpotlightWindow()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
