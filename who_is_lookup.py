import whois
f = open("words.txt", "r")
for x in f:
    x = x.strip()+'.com'
    domain = whois.query(x)
    if not domain:
        outF = open("results.txt", "a")
        outF.write(x)
        outF.write("\n")
print('completed')
