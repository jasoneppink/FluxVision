# FluxVision
FluxVision was built to support a collection of persistent video installations running on Raspberry Pis that automatically update themselves from a YouTube playlist. Anyone (with proper credentials) can add a video to the YouTube playlist. This allows for simple administration of a collaboratively-curated, ever-evolving, looping video installation.

#####Features:
* Videos are downloaded once, not streamed (light on bandwidth)
* New videos are downloaded in the background, usually available within one playthrough of the playlist
* Automatic muting at night (times can be edited)
* Support for a character LCD ticker that displays the title of the current video (requires [Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD))
* Support for an external skip button that advances to the next video
* Support for an external volume knob that adjusts video volume in real time (using a simple analog-to-digital converter with a linear potentiometer connected via GPIO pins)

#####Note:
* Recommended operating system is Raspbian Jessie, on which FluxVision was developed for and stress tested on. (Omxplayer was found to randomly hang between videos on Raspbian Wheezy.)

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
4. Update "config.txt" with your playlist ID and other details.

  ```
  cd FluxVision
  nano config.txt
  ```
5. (optional) Uncomment lines in "startup.sh" if you are using a ticker, skip button, or volume knob

  ```
  nano startup.sh
  ```
6. Open /etc/rc.local:

  ```
  sudo nano /etc/rc.local
  ```
and add this line so FluxVision starts at boot:

  ```
  sudo -u pi /home/pi/FluxVision/startup.sh
  ```
7. (optional) Clear disk space for downloaded videos. If you're running Raspbian, this command can remove up to 1GB of applications you probably don't use.

  ```
  sudo apt-get remove wolfram-engine minecraft-pi python-minecraftpi sonic-pi oracle-java8-jdk pistore scratch nuscratch python3-pygame
  ```
8. Reboot! Videos play as soon as they're downloaded.

  ```
  sudo reboot
  ```



![Installation at Silent Barn](/images/installation_shot_1.jpg?raw=true "Installation at Silent Barn")
