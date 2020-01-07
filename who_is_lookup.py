import whois
import time
f = open("check_me.txt", "r")
for x in f:
    x = x.strip()+'.com'
    domain = whois.query(x)
    if not domain:
        outF = open("results.txt", "a")
        outF.write(x)
        outF.write("\n")
        time.sleep(30)

outF.close()
f.close()
print('Process completed successfully, Check results.txt file for results')
