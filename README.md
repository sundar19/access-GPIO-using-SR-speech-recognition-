# access-GPIO-using-SR-speech-recognition-
Can control General purpose input output pins of raspberry pi using speech recognition(Voice Control)
Requires a USB MICROPHONE connected with RPi USB port.
Packages Required:
pip3 install RPi.GPIO
pip3 install SpeechRecognition
pip3 install Pyserial(if available for RPi and edit code accordingly)

NOTE: 
THis project uses a recorded file(.wav) to activate the pins of GPIO. Check the GPIO by attaching LED or using a multimeter after compiling the python file. Planning to give real time accessing of GPIO pins by voice in near future. The program requires internet connection.
