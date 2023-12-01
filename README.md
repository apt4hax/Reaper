# Reaper 
Reaper is a comprehensive OSINT Bot desinged to use Selenium WebDriver to open a browser and scrape linkedin, then perform additional user and domain enumeration, then perform google and github dorking for related code repositories. This tool is run in an open browser so there are some longish sleep timers to help defeate anti-botting protections, combined with the Github api key rate limit of 60 requests an hour this tool is truley a slow burn. 
## Whats Inside
- LinkedIn data scraping (`lottali_main`)
- Name processing and potential email generation (`mangler_main`)
- Running `nuclei` and `amass` for employee social media accounts & amass for subdomain enumeration (`getmorekeywrds_main`)
- GitHub code search automation (`gitgalaxy_main`)
- Automated Google searches with specific parameters (`youdork_main`)
## Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with the installed Chrome version)
- You must have both amass and nuclei installed with system paths set
## Install
- Use a python virtual enviroment for this script 
- ```git clone https://github.com/apt4hax/Reaper.git```
- ```cd Reaper```
- ```virtualenv -p $(which python3) .venv && source .venv/bin/activate```
- ```python3 -m pip install -r requirments.txt```
## Configuration
- Update `linkedin_username` and `linkedin_password` in `reaper.py` with your LinkedIn credentials.
- Ensure the paths in the scripts are correctly set according to your environment.
- create a .auth folder and store your github apikey as github.keys
## Usage
-```python reaper.py --company [COMPANY_NAME] --domain [DOMAIN_NAME]```
- Add additional keyworks in a line by line text file in the key directory any item in the key directory will be used in the search/dorking functionality. 
## Development plans
- Port lottali.py and youdork.py to use puppeteer/nodejs for improved browser scraping
- Make github api search optional (skip api search of Github due low rate limits)
- Improve file processing/output logging/directory structure
- Add additional google dorks and code repository sites
- Create a keys file for this repo and store file with common keywords (password, username, etc)




