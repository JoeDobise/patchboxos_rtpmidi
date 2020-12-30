This started out as an attempt to integrate a better clock source output from any DAW integrating into a hardware setup. 
What I have found is that by installing the patchboxos from blokas onto a raspberry pi anyone has a perfect starting point to produce better midi data with less jitter.
This midi data I was initially using the pisound midi outputs to generate however recent experiments have proved extremely promissing even with usb midi devices.
With some minimal reconfiguration to the generic patchboxos it is possible to install rtpmidi and connect any class compliant usb midi devices with minimal OS introduced jitter latency. 
Spamming 2-5M midi packets to multiple cc usb midi devices outputted a very consistent latency with extremely low jitter measured with the alsa-midi-latency-test. 

The rtpmidi-call.service file is a very slight modifcation to the example systemd service from McLaren Labs

https://mclarenlabs.com/blog/2020/03/14/run-rtpmidi-as-a-service-on-raspberry-pi/

Modify the two variables {{ bonjour_name }} and {{ port }} to the name of the bonjour setting and port you are trying to connect to    

You will need McLaren Labs rtpmidi software for this to work which can be purchased here.

https://mclarenlabs.com/

This is configured to connect the pisounds midi port to rtpmidi directly, if you are looking to connect a different alsa midi device, run the following to find the alsa midi device number. `$ sudo aconnect -l` If the device number is 666 you would replace the "-p 20:0" with "-p 666:0" section of the line in the service that starts with ExecStart  

Additional considerations to be made that are configured specifically for the pisound and patchbox os are the user named 'patch'. Every occurance of the word 'patch' in the rtpmidi-call.service file would need to be changed to whatever the name of the user on your system is.
It is highly recommended to use Pisound and the Patchbox OS, both are located here.

https://blokas.io/

Steps to install service:
  1. replace {{ bonjour_name }} and {{ port }} with the bonjour name and port you are attempting to connect to
  2. on the raspberry pi place the modified file in /etc/systemd/system/rtpmidi-call.service
  3. on the raspberry pi run the following commands at the shell:
  
      `$ sudo systemctl daemon-reload`
      
      `$ sudo systemctl enable rtpmidi-call.service`
      
      `$ sudo systemctl start rtpmidi-call.service`
 
 Following those steps will connect your pisound (or alternate alsa midi device) directly to the desired rtpmidi server. 
