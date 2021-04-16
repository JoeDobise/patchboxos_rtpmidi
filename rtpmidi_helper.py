class midi_device:
    def __init__(self, device_id):
        # this should be unique for each device 
        self.id=device_id
        if not self.id in midi_device.list_device_id():
            raise OSError("INVALID DEVICE ID: Incorrect device id should not be possible, please contact the developer")
        # raw device list containing device name
        self.raw=[x for x in midi_device.list_devices() if x.split()[0][:len(self.id)] == self.id][0].split('\n')
        # raw parsing, removing name and connected data
        self.rawparse=[[z.strip() for z in y.split("'") if z] for y in (x for x in self.raw[1:] if not "\tConnecting" in x if not "\tConnected" in x if x)]
        # descriptive name 
        self.name=self.raw[0].split()[0]+self.raw[0].split()[1]
        # dictionary of all devices
        self.subdevice={int(x[0]):x[1] for x in self.rawparse}
        # reverse dictionary for gits and shiggles 
        self.subdevicereverselookup={value:key for key, value in self.subdevice.items()}
        # list of the ports currently connected
        self.connected=[int(x.split("MIDI")[-1].split()[0]) for x in str(self.raw[1:]).split('\\t') if "MIDI" in x][:-1]
        # may want to validate what is currently available
        self.available=list(set(self.subdevice.keys()).difference(set(self.connected)))
    
    def __repr__(self):
        '''
        Pretty name for device
        '''
        return(self.name)

    def __len__(self):
        '''
        Total ports present
        '''
        return(len(self.subdevice.keys()))

    def list_ports(self):
        '''
        List names of all ports on the device
        '''
        for x in self.subdevice:
            print(str(self.id) +":"+ str(x), self.subdevice[x])
        return(True)

    @staticmethod
    def list_devices():
        '''
        Calls aconnect -l as a subprocess and evaluates the return for acceptable midi devices to be connected into rtpmidi
        This will prune out all rtpmidi devices, System devices including any device labeled "Through"
        Potential use cases exist outside the scope of rtpmidi where a slightly different pruning could be helpful 
        Most of this output will appear to be garbage if directly called, but it will contain all of the necessary data for future use
        '''
        import subprocess, os
        process_for_midi_port_list=subprocess.Popen(['aconnect', '-l'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return_of_midi_port_list=process_for_midi_port_list.communicate()[0]
        if process_for_midi_port_list.returncode != 0:
            return(False)
        midi_port_host_list=[x.decode("utf-8") for x in return_of_midi_port_list.split(b'client')]
        midi_port_host_list=[x for x in midi_port_host_list if x if 'rtpmidi' not in x if 'System' not in x if 'Through' not in x]
        return(midi_port_host_list)
    
    @staticmethod
    def list_device_id():
        '''
        Calls list_devices and parses the data for device id, mainly used for __init__ of the midi_device class 
        Has potential use cases outside the breadth of this method
        In general for the scope of the rtp midi project this method could be useful for generating a unique identifier for each validated midi device
        The output is assummed to be the main alsa midi device id
        '''
        return([x.split()[0][:-1] for x in midi_device.list_devices()])

class rtpmidi_device:
    from os import walk
    def __init__(self):
        self.rtp_backupfiles="/tmp/rtpserviceinstall"
        self.rtpmidi_dir=[root for root,dir,file in walk("/opt") if "rtpmidi" in root if "bin" in root]
        if self.rtpmidi_dir:
            self.rtpmidi_dir=self.rtpmidi_dir[0]
        else:
            raise FileNotFoundError("A McLaren Labs RTPMIDI installation does not appear to be found under /opt, please install in this location or contact the developer of this script")
        self.instantiate_backupdir()

    def __del__(self):
        self.cleanup_on_exit()

    def cleanup_on_exit(self):
        '''
        removes temporary file directory
        '''
        import subprocess, os
        process_to_validate_backupdir=subprocess.Popen(['rm', '-rf', self.rtp_backupfiles],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return_of_backup_creation=process_to_validate_backupdir.communicate()[0]
        if process_to_validate_backupdir.returncode != 0:
            return(False)
        else:
            return(True)

    def instantiate_backupdir(self):
        '''
        validates existence of temporary file directory
        '''
        import subprocess, os
        process_to_validate_backupdir=subprocess.Popen(['mkdir', '-p', self.rtp_backupfiles],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return_of_backup_creation=process_to_validate_backupdir.communicate()[0]
        if process_to_validate_backupdir.returncode != 0:
            return(False)
        else:
            return(True)


