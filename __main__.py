from ruamel import yaml


## Path to adguard home
adguard_home_path = ''
dns_domain_cert_name = 'abpvn.com-0001'
env_mode = 'dev'

if env_mode == 'server':
    adguard_home_path = '/var/www/html/dns/AdGuardHome/'
    cert_file = '/etc/letsencrypt/live/' + dns_domain_cert_name + '/fullchain.pem'
    privkey_file = '/etc/letsencrypt/live/' + dns_domain_cert_name + '/privkey.pem'
else:
    cert_file = 'fullchain4.pem'
    privkey_file = 'privkey4.pem'

def get_file_content(file_path):
    with open(file_path, 'r') as read_file:
        return read_file.read()
def get_cert():
    return get_file_content(cert_file)

def get_privkey():
    return get_file_content(privkey_file)

def write_file_content(file_path, content):
    with open(file_path, 'w') as write_file:
        write_file.writelines(content)

config_content = get_file_content(adguard_home_path + "AdGuardHome.yaml")
config = yaml.load(config_content, Loader=yaml.RoundTripLoader)
config['tls']['certificate_chain'] = get_cert()
config['tls']['private_key'] = get_privkey()

out_config_str = yaml.dump(config, Dumper=yaml.RoundTripDumper, default_flow_style=False)
if env_mode == 'dev':
    write_file_content(adguard_home_path + "AdGuardHome_dev.yaml", out_config_str)
else:
    write_file_content(adguard_home_path + "AdGuardHome.yaml", out_config_str)