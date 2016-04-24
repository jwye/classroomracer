##sudo nano /etc/profile  ## autostart on boot
## or add to /etc/rc.local

# add bluetooth echo "connect 14:10:9F:E0:7B:DE \nquit" | bluetoothctl
## add at end   = sudo sh /home/pi/Development/classroomracer/classroomracer.sh


cd /
cd home/pi/
python3 ./Development/classroomracer/carxboxdev.py
exit 0
cd /
