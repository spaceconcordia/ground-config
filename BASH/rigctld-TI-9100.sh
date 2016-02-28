#!/bin/bash
#/etc/init.d/ic9100_Net

# chkconfig: 35 90 12
# description: Rig Control Daemom customized to connect to Icom IC-9100 Tranceiver
#
# Get function from functions library
#. /etc/init.d/functions
# Start the service rigctld
start() {
        logger -s "Starting rigctld server..."
        # Give the ICOM serial port a chance to get comfortable with its new surroundings before attaching a service to it
        sleep 5
        # ToDo Need to figure out how to use a config file with this call
        /usr/local/bin/rigctld -m 368 -r /dev/ttyIC9100A -s 19200 None &
        ### Create the lock file ###
        touch /var/lock/rigctld
}
# Restart the service rigctld
stop() {
        logger -s "Stopping rigctld server..."
        killall rigctld
        ### Now, delete the lock file ###
        rm -f /var/lock/rigctld
}
### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  status)
        status rigctld
        ;;
  restart|reload|condrestart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart|reload|status}"
        exit 1
esac

exit 0
