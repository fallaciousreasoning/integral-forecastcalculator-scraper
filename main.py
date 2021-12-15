from client import ApiClient
import simulate_command

client = ApiClient('jay.harris@outlook.co.nz', 'xsEn2xxwCLsty3')
client.ensure_loggedin()

response = client.simulate(38.221, 176.07, simulate_command.PSEM_1T_COMMANDS)
print(response.text)