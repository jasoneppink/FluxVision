# FluxVision
FluxVision was built to support a collection of persistent video installations running on Raspberry Pis that automatically update themselves from a YouTube playlist. Anyone (with proper credentials) can add a video to the YouTube playlist, allowing for simple administration of a collaboratively-curated, ever-evolving, looping video installation.

#####Features:
* Videos are downloaded once, not streamed (light on bandwidth)
* New videos are downloaded in the background, available within one playthrough of the playlist
* Automatic muting at night
* Character LCD ticker displays title of currently-playing video (requires [Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD))

#####Upcoming features:
* Skip button support
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
3. Copy all files into your home directory (usually /home/pi/).
4. Update "config.txt" with your playlist ID, mute and unmute times, and use of ticker
5. Add this line to /etc/rc.local so FluxVision starts at boot (change directory if necessary):

  ```
  sudo -u pi /home/pi/startup.sh
  ```
7. Reboot! Videos play as soon as they're downloaded.

  ```
  sudo reboot
  ```



![Installation at Silent Barn](/images/installation_shot_1.jpg?raw=true "Installation at Silent Barn")
