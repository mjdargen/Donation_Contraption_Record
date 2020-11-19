# Donation Contraption Record  
*Michael D'Argenio   
mjdargen@gmail.com  
https://dargenio.dev  
https://github.com/mjdargen  
November 19, 2020*  
\
Records audio and video from webcam using OpenCV & PyAudio, mixes A/V together
with ffmpeg, uploads video to Google Drive using pyDrive, and sends email from
Gmail using ssl & smtplib. Video recording adapted from [JRodrigoF](https://github.com/JRodrigoF/AVrecordeR).  

## Project Overview
Goal: Create a fun contraption that serves as an incentive to donate. Whenever someone donates, the contraption will actuate rewarding the person for donating. A recording of the contraption will be sent to the donor.  

Background: There are many different examples of similar ideas in existence: coin donation spiral wishing wells, Kickstarter rewards, dunking booths, etc. All of these provide a fun reward for people's contributions. We want to create something in this spirit that brings joy to people for donating to a good cause. Donations will go to a local charity.  

Details: This project will incorporate web development, software development, circuits, and mechanical design to accomplish the goal. Throughout this project, the students are going to learn to be more resourceful and how to think like an engineer. They will learn how to use the materials and the educational resources at their disposal to create a unique project.  

## Installation Steps
* Install Python 3.8
* Install image-magick with ffmpeg, convert, and development headers  
* Install Microsoft Visual C++ 14.0, Build Tools for Visual Studio
* I ran Visual Studio Community Installer and installed the following:
  * Python development workload
  * Desktop development with C++
  * Linux development with C++
* pip install -r requirements.txt
* pip install pipwin
* pipwin install pyaudio

## Environment/Password Setup Steps
* Gmail Password:
  * Add 2FA to Gmail.
  * Generate a special app password in Gmail.
  * Store the special app password in .env under "GMAIL_PW"
* Drive Upload Client Secrets
  * I can't remember how I created this.
  * Do it and store in "client_secrets.json"

## Run Steps
* Import top level function
  * from avrecord import record_video
* Call function: record_video(duration, last_email)
  * 1st argument: duration (in seconds) for recording
  * 2nd argument: email you want to share the video link with
