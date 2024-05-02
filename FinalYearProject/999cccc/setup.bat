@echo off
echo Setting up the Python environment and dependencies...
if not exist "999.py" (
    echo Error: Please run this batch file from the root directory of the project where 999.py is located...
    pause
    exit
)

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing required libraries...
pip install flask
pip install tensorflow
pip install tensorflow-hub
pip install matplotlib
pip install Pillow
pip install numpy
pip install beautifulsoup4
echo All dependencies installed successfully!

echo Setting environment variables...
set FLASK_APP=999.py
set FLASK_ENV=development


echo Setup complete!
pause
