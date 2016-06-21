# FluxVision
FluxVision was built to support a collection of persistent video installations running on Raspberry Pis that automatically update themselves from a YouTube playlist. Anyone (with proper credentials) can add a video to the YouTube playlist, allowing for simple administration of a collaboratively-curated, ever-evolving, looping video installation.

#####Features:
* Videos are downaloded once, not streamed (light on bandwidth)
* New videos are downloaded in the background, available within one playthrough of the playlist
* Automatic muting at night
* Character LCD ticker displays title of currently-playing video

#####Upcoming features:
* Skip button support
* Volume knob support

##Installation

1. Install youtube-dl

  ```
  sudo apt-get update
  sudo apt-get install youtube-dl
  ```
2. Install omxplayer (if necessary)

  ```
  sudo apt-get install omxplayer
  ```
3. Copy all files into your home directory (usually /home/pi/).
4. Add your YouTube playlist ID to startup.sh (and update location of play_youtube.py if necessary)

  ```
  nano startup.sh
  /usr/bin/python /home/pi/play_youtube.py YOUR_PLAYLIST_ID_HERE
  [ctrl-X] [y] [enter]
  ```
5. Add line to /etc/rc.local so FluxVision starts at boot. (Update location of script and username - "/home/pi/" and "pi", respectively - if necessary.)

  ```
  sudo nano /etc/rc.local
  sudo -u pi /home/pi/startup.sh >/dev/null 2>&1 &
  [ctrl-x] [y] [enter]
  ```
6. (Optional) Add line to /etc/rc.local so ticker starts at boot. (Update location of script if necessary.) Note: "ticker.py" requires [Adafruit_Python_CharLCD](https://github.com/adafruit/Adafruit_Python_CharLCD). 
 
  ```
  sudo nano /etc/rc.local
  /usr/bin/python /home/pi/ticker.py >/dev/null 2>&1 &
  [ctrl-x] [y] [enter]
  ```

7. Reboot! Note: it may take a minute before you see anything because videos are being downloaded. Check the newly created "~/media" directory to ensure downloading is happening.

  ```
  sudo reboot
  ```



![Installation at Silent Barn](/images/installation_shot_1.jpg?raw=true "Installation at Silent Barn")
