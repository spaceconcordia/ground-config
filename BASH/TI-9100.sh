#/etc/udev/rules.d/49-IC-9100.rules
#command #1 - If the USB device that has just connected, then jump to the end of this rule. No work needs to be done.
SUBSYSTEM!="tty",GOTO="hamlib_end"

#As of January, 2015, this set of comments describes what the serial ports look like to Linux
#Icom IC-9100 USB Connection
# 10c4:ea60 Cygnal Integrated Products, Inc. CP210x UART Bridge / myAVR mySmartUSB light

#Icom's Serial Port "A" the one we are looking to use
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="IC-9100 02002005 A", TEST!="/dev/ttyIC9100A", SYMLINK+="ttyIC9100A"

#Icom's Serial port "B" Not really needed for HamLib, but if we are anchoring one, we should anchor both. Consider this as 'future'
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="IC-9100 02002005 B", TEST!="/dev/ttyIC9100B", SYMLINK+="ttyIC9100B"

#So now, if the ICom Port "A" hardware was detected and the simlink created, now fire off an instance of rigctld
#start rigctld for an Icom IC-9100 Transceiver "if" the simlink to port "A" above was created
ATTRS{idVendor}=="10c4", ATTRS{idProduct}=="ea60", ATTRS{serial}=="IC-9100 02002005 A", RUN+="/etc/init.d/ic9100_Net restart"

LABEL="hamlib_end"
