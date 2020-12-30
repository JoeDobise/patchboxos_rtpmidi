This is a very slight modifcation to the example systemd service from McLaren Labs

https://mclarenlabs.com/blog/2020/03/14/run-rtpmidi-as-a-service-on-raspberry-pi/

Modify the two variables {{ bonjour_name }} and {{ port }} to the name of the bonjour setting and port you are trying to connect to    

You will need McLaren Labs rtpmidi software for this to work which can be purchased here.

https://mclarenlabs.com/

This is configured to connect the pisounds midi port to rtpmidi directly, if you are looking to connect a different alsa midi device, run the following to find the alsa midi device number.

      $ sudo aconnect -l
If the device number is 666 you would replace the "-p 20:0" with "-p 666:0" section of the line in the service that starts with ExecStart  

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
