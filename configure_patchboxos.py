#!/usr/bin/python3

# validate all packages are present
# needed: ansible debhelper autotools-dev automake libasound2-dev vim jinja2 python3-jinja2 avahi-discover avahi-browse avahi-browser avahi-utils

# build lists of available midi devices and avahi rtpmidi devices

# build lists of current devices connected

# present question of what to do
# options that should be available are to 
#   reconfigure patchbox for no pisound present, reducing jitter 
#   show current config
#   modify current config
#       inclusive of : removing or changing connection settings
#   add new device

# once modifications are identified as being needed modify inventory for ansible and run ansible playbook

# TODO build methods for building out rtpmidi callers not just listeners