import urllib
from urllib.request import urlopen
import re
# open file to write
fout = open('wikipedia_links_answer.csv', 'w')
fout.write('wikipedia_page,"website"')
flag = True
file_name = input()
# open file to read links
while(flag):
    try:
        fhand = open(file_name)
        flag = False
    except:
        print ('File cannot be opened')
        print ('try again')
        print ('if you want to exit enter "exit" ')
        file_name = input()
        if(file_name=='exit'):
            exit()
        else:
            continue
# for each link find on page after word "Website" link to website
for line in fhand:
    line = line[1:len(line)-2]
    fout.write('\n'+line+', ')
    page = urlopen(line).read()
    links1 = re.findall('Website</th>\n<(.+)', str(page,'utf-8'))
    links = re.findall('href="(http.*?)"', ''.join(links1))
    if(not links):
        links = re.findall('href="(//www.*?)"', ''.join(links1))
# write to website to wikipedia_links_answer.csv
    for link in links:
        fout.write(link)
fout.close()
fhand = open('wikipedia_links_answer.csv')
print('All have done')
 
