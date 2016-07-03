# FluxVision
FluxVision was built to support a collection of persistent video installations running on Raspberry Pis that automatically update themselves from a YouTube playlist. Anyone (with proper credentials) can add a video to the YouTube playlist, allowing for simple administration of a collaboratively-curated, ever-evolving, looping video installation.

#####Features:
* Videos are downloaded once, not streamed (light on bandwidth)
* New videos are downloaded in the background, usually available within one playthrough of the playlist
* Automatic muting at night (times can be edited)
* Character LCD ticker displays title of current video (requires [Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD))
* Simple GPIO skip button advances to next video

#####Upcoming features:
* Volume knob support

##Installation

1. Install youtube-dl

  ```
  sudo pip install --upgrade youtube_dl
  ```
2. Install omxplayer (if necessary)

  ```
  sudo apt-get install omxplayer
  ```
3. Download FluxVision files to your Raspberry Pi

  ```
  git clone https://www.github.com/jasoneppink/FluxVision
  ```
4. Move everything to your home directory and delete the FluxVision directory

  ```
  cd FluxVision
  mv * ../
  cd ..
  rm -rf FluxVision
  ```

5. Update "config.txt" with your playlist ID and other details.

  ```
  nano config.txt
  ```

6. Open /etc/rc.local:

  ```
  sudo nano /etc/rc.local
  ```
and add this line so FluxVision starts at boot:

  ```
  sudo -u pi /home/pi/startup.sh
  ```
7. (optional) Clear disk space for downloaded videos. If you're running Raspbian, this command removes up to 1GB of applications you probably don't use.

  ```
  sudo apt-get remove wolfram-engine minecraft-pi python-minecraftpi sonic-pi oracle-java8-jdk pistore scratch nuscratch python3-pygame
  ```
8. Reboot! Videos play as soon as they're downloaded.

  ```
  sudo reboot
  ```



![Installation at Silent Barn](/images/installation_shot_1.jpg?raw=true "Installation at Silent Barn")
