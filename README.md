# Indigo Reflector Bug
A lightweight macOS menubar app displaying the status of the Indigo reflector connection

Up: ![alt text](reflector_up.png)
Down: ![alt text](reflector_down.png)

Download the file `reflector.py` above and save it to the Indigo Scripts folder at:
```text
/Library/Application Support/Perceptive Automation/Scripts/reflector.py
```
Can be installed anywhere, as long as Indigo can see it.

Install the [`rumps`](https://github.com/jaredks/rumps) python library using the Terminal command:
```bash
pip3.10 install rumps==0.4.0
```

Run the `reflector.py` file as an linked script using an Indigo method of choice. For
example, using a trigger:
  * Type: "Indigo Server Startup"
  * Condition: Always
  * Actions: Server Actions > Script and File Actions > Execute Script > reflector.py

***CAUTION: Do not run this script as an embedded script (because Indigo will kill it after 10 seconds).***  

NOTE: This is designed to be run on the machine running the Indigo server. It will not interrogate the server from 
another machine/location.
