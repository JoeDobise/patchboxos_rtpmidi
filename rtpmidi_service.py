# this python script requires the jinja2 package for python3, the following command can install python3-jinja2 from apt
# sudo apt install python3-jinja2

import signal, sys
import rtpmidi_helper as rtpmidi
try:
    from jinja2 import Template, Environment, FileSystemLoader
except ImportError:
    sys.exit(3)

# initialize variables
rtp_locaiton=False
midi_devices=False
rtp_servers=False
rtp_hosts=False
rtp_backupfiles="/tmp/rtpserviceinstall"

# capture ctrl_c so that exits will clean up properly
def signal_handler(sig, frame):
    exit_poorly

def exit_poorly():
    cleanup_on_exit
    sys.exit(1)

def exit_properly():
    cleanup_on_exit
    sys.exit(0)

# # helper for modifications
# def backup_configuration_file():

# def evaluate_midi_configuration():

# def evaluate_rtp_servers():

# # used as a helper to validate configuration changes 
# # can be used to establish a potential troubleshooting scenario to restart any service available or reconfigure existing systemd service
# def evaluate_current_rtpmidi_systemd_services():

# # instructs user to plug in to out and reports the current latency / jitter(ms offset) / jitter(percentage) 
# # will need to grab from 
# def check_latency():

# instantiate signal_handler watching in order to capture ctrl-c
signal.signal(signal.SIGINT, signal_handler)
rtp_locaiton=evaluate_rtp_install()

if rtp_locaiton:
    print("Rtpmidi software was found at", rtp_locaiton)
else:
    print("Script assumes a directory containing the word rtpmidi is located under /opt.") 
    print("Please install McLaren Labs rtpmidi under /opt and rerun this script")

devices=[rtpmidi.midi_device(dev) for dev in rtpmidi.midi_device.list_device_id()]
devices
print(devices[0])
print(devices[0].list_ports())
# # exit incorrectly, as we should exit_properly, and never hit this line
# sys.exit(2)