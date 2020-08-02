#!/bin/bash
./airpods_mac.sh
for i in {0..20}
do
	deviceIndex=$(pactl list short sinks | grep bluez | cut -f1)
	if [ -z "$deviceIndex" ]
	then
		echo "bluetooth not ready, wait 1s"
		sleep 1
	else
		echo Connecting to index $deviceIndex
		pacmd set-card-profile $deviceIndex a2dp_sink
		echo "connected and set!"
		exit 0
	fi
done
echo "timeout!"
exit 1
