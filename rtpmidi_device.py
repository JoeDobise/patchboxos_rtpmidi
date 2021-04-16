class rtpmidi_device:
    def __init__(self):
        self.backupfiles="/tmp/rtpserviceinstall"
        self.rtpmidi_dir=[root for root,dir,file in walk("/opt") if "rtpmidi" in root if "bin" in root]
        if self.rtpmidi_dir:
            self.rtpmidi_dir=self.rtpmidi_dir[0]
        else:
            raise FileNotFoundError("A McLaren Labs RTPMIDI installation does not appear to be found under /opt, please install in this location or contact the developer of this script")
        self.instantiate_backupdir()

    def __del__(self):
        self.cleanup_on_exit()
    def cleanup_on_exit(self):
        rmdir self.rtp_backupfiles

    def instantiate_backupdir(self):
        mkdir -p self.rtp_backupfiles


# validation of environment installed with mclaren labs rtpmidi
# should be installed under /opt, and is not always added to path
def evaluate_rtp_install():
    if installation_test:
        return(installation_test[0])
    else:
        return(False)
