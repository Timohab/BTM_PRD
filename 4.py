import random
up_alph='QWERTYUIOPASDFGHJKLZXCVBNM'
low_alph='qwertyuiopasdfghjklzxcvbnm'
chisla='0123456789'
with open('scientist.txt',encoding='utf8') as file:
    a=file.readline()
    data=[x.split('#') for x in file.read().split('\n') if x!='']

for dt in data:
    spl_name=dt[0].split()
    login=f"{spl_name[0]}_{spl_name[1][0]}{spl_name[2][0]}"
    password=(random.choice(up_alph)+random.choice(low_alph)+random.choice(chisla))*3 +random.choice(up_alph)
    dt.append(login)
    dt.append(password)

with open('scientist_password.csv','w',encoding='utf8') as file:
    file.write('ScientistName#preparation#date#components#login#password\n')
    for i in data:
        file.write('#'.join(i)+'\n')