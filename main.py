from client import ApiClient
import simulate_command

client = ApiClient('jay.harris@outlook.co.nz', 'xsEn2xxwCLsty3')

files = client.simulate(38.221, 176.07, simulate_command.PSEM_1T_COMMANDS)
for file in files:
    client.download_file('test', file)