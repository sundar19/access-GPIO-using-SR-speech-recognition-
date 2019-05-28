# access-GPIO-using-SR-speech-recognition-
Can control General purpose input output pins of raspberry pi using speech recognition(Voice Control)
Requires a USB MICROPHONE connected with RPi USB port.
Packages Required:
pip3 install RPi.GPIO & 
pip3 install SpeechRecognition &
pip3 install Pyserial(if available for RPi and edit code accordingly)

NOTE: 
This project uses a recorded file(.wav) to activate the pins of GPIO. Check the GPIO by attaching LED or using a multimeter after compiling the python file. Planning to give real time accessing of GPIO pins by voice in near future. The program requires internet connection.

PROCDURE:
First record the voice by speaking to the microphone words such as "ON" or "OFF". save it using .wav file. Now save in the home directory so that it can be accessed by the .py file.
http://wiki.sunfounder.cc/index.php?title=To_use_USB_mini_microphone_on_Raspbian go through the following instructions to record your voice and purchase the microphone.Then use the program to control the GPIO pins.NOTE: use the GPIO pin specified in the code or change the code accordingly
