# A Python virtual environment is required to run this app

# Install the virtual environment
pip install virtualenv

# Create the virtual environment
python3 -m venv env

# Run the virtual environment
env/Scripts/activate.bat (for CMD)
env/Scripts/Activate.ps1 (for powershell)

# Install reflex
pip3 install reflex

# Install Google GenAI
pip install google-generativeai (Python 3.9+ required)
pip3 install python-dotenv

# Run the application
reflex run