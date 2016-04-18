

sudo rmmod xpad
sudo xboxdrv --silent --detach-kernel-driver &

python3 carxboxdev.py

killall xboxdrv
