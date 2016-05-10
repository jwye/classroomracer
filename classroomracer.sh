##sudo nano /etc/profile  ## autostart on boot

## or add to /etc/rc.local  # ichoose this one

# add bluetooth= echo "connect 14:10:9F:E0:7B:DE \nquit" | bluetoothctl
## add at end   = sh /home/pi/Development/classroomracer/classroomracer.sh

#echo "connect 14:10:9F:E0:7B:DE \nquit" | bluetoothctl

cd /
cd home/pi/
#python3 ./Development/classroomracer/carxboxdev.py
python3 ./Development/classroomracer/carxboxdev2BDRIVEtbk.py

exit 0
cd /
