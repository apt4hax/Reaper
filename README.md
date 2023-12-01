# Reaper
Reaper is a comprehensive OSINT tool desinged to scrape linkedin, perform additional user and domain enumeration, then perform google and github dorking for related code repositories. 
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
## Install
- Use a python virtual enviroment for this script 
`git clone https://github.com/apt4hax/Reaper.git`
`cd Reaper`
`virtualenv -p $(which python3) .venv && source .venv/bin/activate`
`python3 -m pip install -r requirments.txt`
## Configuration
- Update `linkedin_username` and `linkedin_password` in `reaper.py` with your LinkedIn credentials.
- Ensure the paths in the scripts are correctly set according to your environment.
- create a .auth folder and store your github apikey as github.keys
## Usage
```python reaper.py --company [COMPANY_NAME] --domain [DOMAIN_NAME]```
