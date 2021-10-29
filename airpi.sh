sudo iw phy `iw dev wlan0 info | gawk '/wiphy/ {printf "phy" $2}'` interface add mon0 type monitor
sudo ifconfig mon0 up
sudo nexutil -k6

sudo nohup owl -i mon0 -v -N &
nohup opendrop receive -n "Raspberry Pi" -d -i awdl0 &
sudo nohup python3 airpi.py &