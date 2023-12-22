#! /usr/bin/env python3.10
# -*- coding: utf-8 -*-

"""
Create a macOS menu bar bug that shows the status of the Indigo Reflector connection

Save this script to the Indigo Scripts folder at:
    /Library/Application Support/Perceptive Automation/Scripts/reflector.py
Can be installed anywhere, as long as Indigo can see it.

Install the `rumps` python library using the Terminal command:
    pip3.10 install rumps==0.4.0

Run the `reflector.py` file as a linked script using an Indigo method of choice. For
example, using a trigger:
    Type: "Indigo Server Startup"
    Condition: Always
    Actions: Server Actions > Script and File Actions > Execute Script > reflector.py

CAUTION: Do not run this script as an embedded script (because Indigo will kill it after
         10 seconds).
NOTE: This is designed to be run on the machine running the Indigo server. It will not
      interrogate the server from another machine/location.
"""

import sys
try:
    import rumps
except ImportError:
    indigo.server.log("You must install the `rumps` library --> pip3.10 install rumps==0.4.0", isError=True)
    sys.exit()

BASE_URL     = f"{indigo.server.getInstallFolderPath()}/Web Assets/images/controls/variables/"
CYCLE_TIME   = 60
OFFLINE_ICON = "Red Green Dot.png"
ONLINE_ICON  = "Red Green Dot+true.png"

class MyApp(rumps.App):
    """ rumps base class for the application"""
    def __init__(self):
        super().__init__(name="", title="Indigo", icon=None)

    @rumps.timer(CYCLE_TIME)  # cycle time in seconds
    def change_title(self, sender):
        """
        Change the icon based on server status.

        rumps timer runs automatically
        """
        reflector_url = indigo.server.getReflectorURL()
        self.icon = BASE_URL + (OFFLINE_ICON if not reflector_url else ONLINE_ICON)

if __name__ == "__main__":
    MyApp().run()
