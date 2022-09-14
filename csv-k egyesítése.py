def Program(hanyszor):
  kifile=open('kimenet.csv', 'w', encoding='utf-16', newline="")
  befile=open('statisztika0.csv', 'rt', encoding="utf-16")
  kifile.write(befile.readline())
  befile.close()
  for i in range(hanyszor):
    try:
      befile=open('statisztika'+str(i)+'.csv', 'rt')
      befile.readline()
      sor=befile.readline()
      while sor!= "":
        kifile.write(sor+"\n")
        sor=befile.readline()
      befile.close()
      print(i, 'db fájl feldolgozva a', str(hanyszor-1)+'-ból')
    except:
      print('A statisztika'+str(i)+'.csv nevű file nem létezik.')
  kifile.close()

#sok az üres sor, át kéne még írni

Program(1084)
