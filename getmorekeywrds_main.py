import subprocess
import os
import re
import sys
import multiprocessing

def run_nuclei(email_file, output_dir):
    with open(email_file, 'r') as file:
        emails = [line.strip() for line in file]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for email in emails:
        output_file = os.path.join(output_dir, f"{email}_nuclei.txt")
        command = f"nuclei -tags osint -var user={email} -o {output_file}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        print(result.stderr, file=sys.stderr)

def run_amass(domain):
    amass_command = f"amass enum -d {domain}"
    result = subprocess.check_output(amass_command, shell=True, text=True)
    print(result)

    with open('key/fqdn.txt', 'w') as fqdn_file, open('key/ips.txt', 'w') as ips_file:
        for line in result.splitlines():
            if re.match(r'^\d+\.\d+\.\d+\.\d+$', line):
                ips_file.write(line + '\n')
            else:
                fqdn_file.write(line + '\n')

def getmorekeywrds_main(email_list, domain):
    nuclei_process = multiprocessing.Process(target=run_nuclei, args=(email_list, 'key/users_social_media'))
    nuclei_process.start()
    nuclei_process.join()

    amass_process = multiprocessing.Process(target=run_amass, args=(domain,))
    amass_process.start()
    amass_process.join()
