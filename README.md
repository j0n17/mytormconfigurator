# myStorm configurator

## Install
```sh
git clone https://github.com/j0n17/mytormconfigurator
cd mytormconfigurator
virtualenv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python mystormconfigurator.py -h
```


## Usage
```sh
python mystormconfigurator.py show 10.0.15 # To show the configuration of your button
python mystormconfigurator.py set 10.0.0.15 single "post://home-assistant.example.com/api/webhook/scene.tv_lights_off" # To change the single click action trigger
```
