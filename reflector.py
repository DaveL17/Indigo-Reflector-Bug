#! /usr/bin/env python3.10
# -*- coding: utf-8 -*-

"""
Create a macOS menu bar bug that shows the status of the Indigo Reflector connection

Save this script to the Indigo Scripts folder at:
    /Library/Application Support/Perceptive Automation/Scripts/reflector.py
Can be installed anywhere, as long as Indigo can see it.

Install the `rumps` python library using the Terminal command:
    pip3.10 install rumps==0.4.0

Run the `reflector.py` file as an linked script using an Indigo method of choice. For
example, using a trigger:
    Type: "Indigo Server Startup"
    Condition: Always
    Actions: Server Actions > Script and File Actions > Execute Script > reflector.py

CAUTION: Do not run this script as an embedded script (because Indigo will kill it after
         10 seconds).
NOTE: This is designed to be run on the machine running the Indigo server. It will not
      interrogate the server from another machine/location.
"""

try:
    import sys
    import rumps
except ImportError:
    indigo.server.log(f"You must install the `rumps` library --> pip3.10 install rumps==0.4.0", isError=True)
    sys.exit()

BASE_URL = f"{indigo.server.getInstallFolderPath()}/Web Assets/images/controls/variables/"

class MyApp(rumps.App):

    def __init__(self):
        super().__init__(name="", title="Indigo", icon=None)

    @rumps.timer(60)  # cycle time in seconds
    def change_title(self, sender):

        if not indigo.server.getReflectorURL():
            self.icon = BASE_URL + "Red Green Dot.png"  # Offline
        else:
            self.icon = BASE_URL + "Red Green Dot+true.png"  # Online

if __name__ == "__main__":
    MyApp().run()