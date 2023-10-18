import random
def generate_android_user_agent():
    user_agents = []
    for _ in range(10):
        user_agent = f"[FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(0,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["en_US"]))+";FBRV/"+str(random.randint(111111111,999999999))+";FBCR/"+str(random.choice(["TNT", "GLOBE","DITO","SMART","SUN","TM","GOMO","WIFI"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["xiaomi","Xiaomi","Redmi",]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2012K11C","Redmi 6A","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4","Redmi Note 5", "Redmi 4X","Redmi Note 8","Redmi Note 8 Pro"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
        user_agents.append(user_agent)
    return user_agents

android_user_agents = generate_android_user_agent()
for user_agent in android_user_agents:
    colour = random.choice(['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m'])
    print(colour+'\n'+user_agent)
