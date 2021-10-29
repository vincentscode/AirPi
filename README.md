# AirPi
A cheap DIY USB AirDrop Receiver

## Hardware
 - Raspberry Pi Zero W
 - UART <-> USB Cable
 - Micro SD Card (>=8GB)
 - USB Micro <-> USB A Cable

## Setup
Execute through UART / Serial Connection.
Inspired by https://owlink.org/2019/05/16/howto-use-airdrop-on-raspberry-pi-3.html.

### Dependencies & Repos
```bash
echo "update & install dependencies"
sudo apt update && apt upgrade
sudo apt install raspberrypi-kernel-headers git libgmp3-dev gawk qpdf bison flex make -y
sudo apt install libpcap-dev libev-dev libnl-3-dev libnl-genl-3-dev libnl-route-3-dev -y
sudo apt install python3 python3-pip libjpeg-dev libopenjp2-7-dev -y

echo "clone repos"
git clone https://github.com/seemoo-lab/nexmon.git
git clone https://github.com/seemoo-lab/owl.git
git clone https://github.com/seemoo-lab/opendrop.git
git clone https://github.com/vincentscode/AirPi.git
```

### Nexmon
```bash
cd ~
cd nexmon
touch DISABLE_STATISTICS

echo "setup build env and make nexutil"
sudo su
if [[ ! -f /usr/lib/arm-linux-gnueabihf/libisl.so.10 ]]; then \
   cd buildtools/isl-0.10/ && ./configure && make && make install && \
   ln -s /usr/local/lib/libisl.so \
         /usr/lib/arm-linux-gnueabihf/libisl.so.10 && \
   cd ../../ ; fi
source setup_env.sh
make
cd utilities/nexutil/ && make && make install && cd ../../

echo "install patch (kernel 4.19.66+)"
cd patches/bcm43455c0/7_45_189/nexmon/
make
make backup-firmware
make install-firmware
mv /lib/modules/4.19.66+/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/ old.bak
cp /home/pi/nexmon/patches/bcm43455c0/7_45_189/nexmon/brcmfmac_4.19.y-nexmon/brcmfmac.ko /lib/modules/4.19.66+/kernel/drivers/net/wireless/broadcom/brcm80211/brcmfmac/
```

### OWL
```bash
cd ~
cd owl
git submodule update --init
mkdir build
cd build
cmake ..
make
sudo make install
```

### OpenDrop
```bash
cd ~
sudo pip3 install ./opendrop
```

### AirPi
```bash
cd ~
cd AirPi
chmod +x airpi.sh
```

### Final Steps
Disable default networking
```bash
cd ~
sudo apt remove wpasupplicant
```

## Usage
```bash
cd AirPi
./airpi.sh
```
