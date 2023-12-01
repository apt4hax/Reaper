import argparse
import time
from lottali_main import lottali_main
from mangler_main import mangler_main
from getmorekeywrds_main import getmorekeywrds_main
from gitgalaxy_main import gitgalaxy_main
from youdork_main import youdork_main

def main():
    parser = argparse.ArgumentParser(description="This tool is designed to help automate OSINT with associated company code repos")
    parser.add_argument('--company', required=True, help='Company name for LinkedIn search')
    parser.add_argument('--domain', required=True, help='Domain for amass search')

    args = parser.parse_args()


    try:
        linkedin_username = 'linkedin@gmail.com'
        linkedin_password = 'superSecurePass'
        company_url = f'https://www.linkedin.com/company/{args.company}/people/'
        lottali_main(linkedin_username, linkedin_password, company_url)
        print("Completed lottali_main successfully.")
    except Exception as e:
        print(f"Error in lottali_main: {e}")


    try:
        time.sleep(8)
        mangler_input_file = 'key/employeeNames.txt'  
        mangler_output_file = 'key/uvUsers.txt'  
        mangler_main(mangler_input_file, mangler_output_file, args.domain)
        print("Completed mangler_main successfully.")
    except Exception as e:
        print(f"Error in mangler_main: {e}")


    try:
        time.sleep(8)
        email_list_path = 'key/filtered.txt' 
        getmorekeywrds_main(email_list_path, args.domain)
        print("Completed getmorekeywrds_main successfully.")
    except Exception as e:
        print(f"Error in getmorekeywrds_main: {e}")


    try:
        time.sleep(8)
        gitgalaxy_main()
        print("Completed gitgalaxy_main successfully.")
    except Exception as e:
        print(f"Error in gitgalaxy_main: {e}")


    try:
        time.sleep(8)
        domains = ['github.com', 'gitlab.com']
        dorks = ['site:{0} AND "{1}"']
        youdork_main(domains, dorks)
        print("Completed youdork_main successfully.")
    except Exception as e:
        print(f"Error in youdork_main: {e}")

if __name__ == "__main__":
    main()
