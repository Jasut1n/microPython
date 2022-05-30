<h1 align="center'>Install for Linux Shell</h1>
           
           <br />
           <strong>Create a new conda environment and install esptool
           To install MicroPython on the ESP8266-based microcontroller, we will start by creating a virtual environment.
           A virtual environment is an isolated Python interpreter and a set of packages that are separate from the base version of Python running on your computer.                We’ll create a new virtual environment with the Anaconda Prompt and the conda command line tool.
           Open the Anaconda Prompt and create a new virtual environment named micropython. Activate the environment with the command conda activate.
           After activating the virtual environment, you should see the virtual environment name (micropython) before the > Prompt.
           Once inside the virtual environment, use pip to install esptool. esptool will be used to upload the MicroPython .bin firmware file onto the ESP8266                      microcontroller.
           Confirm that esptool is installed in the (micropython) virtual environment by running the command conda list.
           The list of commands below also creates a new directory in the Documents folder called micropython to store all the project</strong>
           <br />
           
           <br />
           >> pip install esptool
           <br />
           
           <br />
           <strong>Download the latest MicroPython firmware .bin file
           Go to GitHub.com and download the latest .bin firmware file at <script img src=micropython.org/download#esp8266></script>. Move the .bin firmware file to a              new micropython directory. The .bin firmware file is the version of MicroPython that runs on the ESP8266 microcontroller. Straight from the manufacturer, the            ESP8266 microcontroller probably does not have MicroPyton installed, so we need to install MicroPython ourselves.
           After installing the Micropython .bin firmware file onto the board, we will be able to bring up the MicroPython REPL prompt, type commands into the                      Micropython REPL and run Micropython .py scripts on the board.</strong>
           <br />
