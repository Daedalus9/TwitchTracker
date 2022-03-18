#TwitchTracker

Track watch time of 300 most popular italian Twitch streamers

## :notebook: Requirements

- python3
- requests
- glob

## :zap: Usage
```bash
git clone https://github.com/Daedalus9/TwitchTracker
cd TwitchTracker
pip3 install requests
python3 main.py [option]

--search        Search without store informations
--store         Search and store informations
--delete        Delete all streamer files
--plots         Create all plots from streamer files
--delete_plots  Delete all plots from streamer files
--dump          Dump streamer list
--help          Show help
```
