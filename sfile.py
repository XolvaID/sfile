# Original Source Code By Kgyya



# Recode By XolvaID :v
# Channel : t.me/XolvaCode
import os,sys,time,re
import requests
from bs4 import BeautifulSoup as bs
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37m'
flag = '\x1b[47;30m'
off = '\x1b[m'
bold = '\033[1m'
plus = f" [ + ]{off}"
bintang = f" [ * ]{off}"
seru = f" [ ! ]{off}"
tanya = f" [ ? ]{off}"
satu = f" [ 1 ]{off}"
dua = f" [ 2 ]{off}"
class KONTOL:
 def REALSHT():
  ses = requests.Session()
  link = input(f"{off}{bold}Input Link {red}>>>{green} ")
  print(off)
  Requests1 = ses.get(link)
  Requests2 = ses.get("https://z.realsht.mobi/get-link.php")
  ReLink = re.search('"(.*?)"',Requests2.text).group(1)
  print(f"{bold}Url {red}>>>{green} "+str(ReLink))
  print(off)


 def SEARCH():
  count = 0
  jud = []
  q = input(f"{bold}Search File {red}>>>{green} ").replace(" ","+")
  print(f"{off}")
  url = f"https://sfile.mobi/search.php?q={q}"
  raw = requests.get(url,headers={"User-Agent":"Chrome"}).text
  for list in re.findall('(.*?)</div><div class="list">', raw):
   count += 1
   data = list.strip()
   for href in re.findall('a\shref="(.*?)"',data):
    link = href.strip()
    judul = re.findall('">(.*?)</a>\s', data)
    jud.append(href.strip())
    print(f"{bold}({cyan}{str(count)}{off}{bold}) {green}{str(judul)}{off}{bold}".replace("'",""))
  pil = input(f"\n{bold}Choose File {red}>>>{green} ")
  print(off)
  link = jud[int(pil) - 1]
  raww = requests.get(link,headers={"User-Agent":"Chrome"}).text
  try:
   down = re.search('href="https://sfile.mobi/download(.*?)"', raww).group(1)
  except AttributeError:
   pw = input(f"{off}{bold}Input Password File {red}>>>{green} ")
   data = {"pa":pw,"pas":"unlock"}
   reqp = requests.get(raww,data=data,headers={"User-Agent":"Chrome"})
   if "Having trouble downloading? Please clear your browser cache." in reqp.text:
    down = re.search('href="https://sfile.mobi/download(.*?)"', reqp.text).group(1)
    pass
   else:
    exit(f"{off}{bold}[{red}!{off}{bold}] Invalid Password")
  load = "https://sfile.mobi/download"+down
  judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
  oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
  pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
  tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
  tag = re.search("i> - (.*?)<", raww).group(1)
  penis = re.search('.html">(.*?)<',raww).group(1)
  ukuran = re.search("Download File (.*?)<",raww).group(1)
  print(f"{bold}================================")
  print(f"{bold}[{cyan}*{off}{bold}] Title         {green}: "+judul_link)
  print(f"{off}{bold}[{cyan}#{off}{bold}] Tags          {green}: "+tag)
  print(f"{off}{bold}[{cyan}{off}{bold}] File Type     {green}: "+penis)
  print(f"{off}{bold}[{cyan}-{off}{bold}] Bio File      {green}: ")
  print(f"{off}{bold}[{cyan}-{off}{bold}] File Size     {green}: "+ukuran)
  print(f"{off}{bold}[{cyan}©{off}{bold}] Uploaded By   {green}: "+oleh)
  print(f"{off}{bold}[{cyan}*{off}{bold}] Upload Date   {green}: "+pada)
  print(f"{off}{bold}[{cyan}*{off}{bold}] Total Download{green}: "+tot_down)
  print(f"{off}{bold}================================\n")
  p = input(f"{off}{bold}[{cyan}?{off}{bold}] Download File? ({green}y{off}{bold}/{red}n{off}{bold}) {red}>>>{green} ")
  while p == "":
   p = input(f"{off}{bold}[{cyan}?{off}{bold}] Download File? ({green}y{off}{bold}/{red}n{off}{bold}) {red}>>>{green} ")
   print(off)
  if p in ("y","Y"):
   out = input(f"{off}{bold}[{cyan}?{off}{bold}] Output {red}>>>{green} ").replace(" ","_")
   print(off)
   extensi = re.search("(.*?)/",tag).group(1)
   print(f"{bold}Processing...")
   r = requests.get(load,headers={"User-Agent":"Chrome"}, stream=True,allow_redirects=True)
   with open(f"{out}.{extensi}", "wb") as s:
    dl = 0
    total_panjang = int(r.headers.get("content-length"))
    for KNTL in r.iter_content(chunk_size=4096):
     dl += len(KNTL)
     s.write(KNTL)
     done = int(43 * dl / total_panjang)
     sys.stdout.write("\r[%s%s]" % ('#' * done, ' ' * (43-done)) )
     sys.stdout.flush()
   print(f"\n{bold}[{green}✓{off}{bold}] Download Success")
   print(f"{bold}[{cyan}?{off}{bold}] Move Files To?")
   print(f" {bold}[{cyan}01{off}{bold}] /sdcard/")
   print(f" {bold}[{cyan}02{off}{bold}] /storage/emulated/0/")
   print(f" {bold}[{cyan}03{off}{bold}] /data/data/com.termux/files/\n")
   pindah = input("{bold}[{cyan}?{off}{bold}]Input Number {red}>>>{green} ")
   if pindah in ("01","1"):
    os.system(f"mv {out}.{extensi} /sdcard")
    print(f"{bold}[{green}✓{off}{bold}] Success > {green}/sdcard/{out}.{extensi}")
   elif pindah in ("02","2"):
    os.system(f"mv {out}.{extensi} /storage/emulated/0")
    print(f"{bold}[{green}✓{off}{bold}] Sucess > {green}/storage/emulated/0/{out}.{extensi}")
   elif pindah in ("03","3"):
    os.system(f"mv {out}.{extensi} /data/data/com.termux/files/home")
    print(f"{bold}[{green}✓{off}{bold}] Success > /data/data/com.termux/files/home/{out}.{extensi}")
   else:
    exit()
 def LOGIN():
  ses = requests.Session()
  email = input("Email >>> ")
  pw = input("Password >>> ")
  dat = {
   "mail":email,
   "pass":pw,
   "LogIn":"Login"
}
  pos = ses.post("https://sfile.mobi/login.php", data=dat,headers={"User-Agent":"Chrome"})
  if "User Panel" in pos.text:
   os.system("clear")
   time.sleep(1)
   print("Panel User\n")
   raw = ses.get("https://sfile.mobi/user/",headers={"User-Agent":"Chrome"})
   revenue = re.search("Your Revenue: <b>(.*?)</b><br>\s", str(raw.text)).group(1)
   earning = re.search("Total Earning: <b>(.*?)</b>\s", str(raw.text)).group(1)
   downloaded = re.search("Total Downloaded: <b>(.*?)</b><br>\s", str(raw.text)).group(1)
   disk = re.search("Disk space: (.*?)<br/>\s", str(raw.text)).group(1)
   free = re.search("Free space: (.*?) <br/>\s", str(raw.text)).group(1)
   user = re.search("(\w+)\sPanel</h3>", str(raw.text)).group(1)
   print(f"\n[@] User       : {user}")
   print(f"[E] Email      : {email}")
   print(f"[$] Revenue    : {revenue}")
   print(f"[+] Downloaded : {downloaded}")
   print(f"[$] Earning    : {earning}")
   print(f"[📁] Total Space: {disk}")
   print(f"[📂] Free Space : {free}\n")
   print("[00] Exit.")
   print("[01] Re-load\n")
   p = input("Input Menu : ")
   if p in ("00","0"):
    os.system("clear")
    exit()
   elif p in ("1","01"):
    KONTOL.LOGIN()

  elif "Invalid Password or Username!" in pos.text:
   print("Username/Email Atau Password Tidak Valid.")
 def BESAR():
  ses = requests.Session()
  try:
   link = input(f"{off}{bold}Input Link {red}>>>{green} ")
   print(off)
   raww = ses.get(link,headers={"User-Agent":"Chrome"}).text
  except ses.exceptions.ConnectionError:
   exit(f"{bold}[{red}!{off}{bold}] No Internet Connection")
  soup = bs(raww, "html.parser")
  try:
   down = re.search('href="https://sfile.mobi/download(.*?)"',raww).group(1)
   load = "https://sfile.mobi/download"+down
   judul_link = re.search('class="img" alt="(.*?)"', raww).group(1)
   oleh = re.search('rel="nofollow">(.*?)<', raww).group(1)
   pada = re.search('i> - Uploaded: (.*?)<', raww).group(1)
   tot_down = re.search('i> - Downloads: (.*?)<', raww).group(1)
   tag = re.search("i> - (.*?)<", raww).group(1)
   penis = re.search('.html">(.*?)<',raww).group(1)
   ukuran = re.search("Download File (.*?)<",raww).group(1)
   print(f"{bold}================================")
   print(f"{bold}[{cyan}*{off}{bold}] Title         {green}: "+judul_link)
   print(f"{off}{bold}[{cyan}#{off}{bold}] Tags          {green}: "+tag)
   print(f"{off}{bold}[{cyan}{off}{bold}] File Type     {green}: "+penis)
   print(f"{off}{bold}[{cyan}-{off}{bold}] Bio File      {green}: ")
   print(f"{off}{bold}[{cyan}-{off}{bold}] File Size     {green}: "+ukuran)
   print(f"{off}{bold}[{cyan}©{off}{bold}] Uploaded By   {green}: "+oleh)
   print(f"{off}{bold}[{cyan}*{off}{bold}] Upload Date   {green}: "+pada)
   print(f"{off}{bold}[{cyan}*{off}{bold}] Total Download{green}: "+tot_down)
   print(f"{off}{bold}================================\n")
  except IndexError:
   exit(f"{off}{bold}[{red}!{off}{bold}] Invalid Url OR Files Had Password")
  ragu = input(f"{off}{bold}Download File? ({green}y{off}{bold}/{red}n{off}{bold}) {red}>>>{green}  ")
  print(off)
  if ragu in ("y","Y"):
   out = input(f"{off}{bold}Output {red}>>>{green} ").replace(" ","_")
   print(off)
   extensi = re.search("(.*?)/",tag).group(1)
   print(f"\n   Mendownload...")
   r = requests.get(load,headers={"User-Agent":"Chrome"}, stream=True, allow_redirects=True)
   with open(f"{out}.{extensi}", "wb") as MEMEK:
    dl = 0
    total_panjang = int(r.headers.get("content-length"))
    for KNTL in r.iter_content(chunk_size=4096):
     dl += len(KNTL)
     MEMEK.write(KNTL)
     done = int(43 * dl / total_panjang)
     sys.stdout.write("\r[%s%s]" % ('#' * done, ' ' * (43-done)) )
     sys.stdout.flush()
   print(f"\n{bold}[{green}✓{off}{bold}] Download Success")
   print(f"{bold}[{cyan}?{off}{bold}] Move Files To?")
   print(f" {bold}[{cyan}01{off}{bold}] /sdcard/")
   print(f" {bold}[{cyan}02{off}{bold}] /storage/emulated/0/")
   print(f" {bold}[{cyan}03{off}{bold}] /data/data/com.termux/files/\n")
   pindah = input(f"{bold}[{cyan}?{off}{bold}]Input Number {red}>>>{green} ")
   if pindah in ("01","1"):
    os.system(f"mv {out}.{extensi} /sdcard")
    print(f"{bold}[{green}✓{off}{bold}] Success > {green}/sdcard/{out}.{extensi}")
   elif pindah in ("02","2"):
    os.system(f"mv {out}.{extensi} /storage/emulated/0")
    print(f"{bold}[{green}✓{off}{bold}] Sucess > {green}/storage/emulated/0/{out}.{extensi}")
   elif pindah in ("03","3"):
    os.system(f"mv {out}.{extensi} /data/data/com.termux/files/home")
    print(f"{bold}[{green}✓{off}{bold}] Success > /data/data/com.termux/files/home/{out}.{extensi}")
   else:
    exit()
  elif ragu in ("n","N"):
   exit(f"{off}{bold}[{red}!{off}{bold}] Exitting Script")
  else:
   exit(f"{off}{bold}[{red}!{off}{bold}] Exitting Script")

 def KECIL():
  os.system("clear")
  ses = requests.Session()
  print(f"{seru} NOTE!")
  print(" [*] Hanya Support Link Yang Langsung Download")
  print(" [*] Misalnya Mediafire, ZippyShare, GDrive")
  time.sleep(5)
  os.system("clear")
  print("[+] File Downloader")
  print("[+] Python 3.x.x\n")
  try:
   link = input("[?] Input Link > ")
   raw = ses.get(link).text
  except requests.exceptions.ConnectionError:
   exit("[!] Gada Sinyal Bang")
  print("Ukuran File: Tidak Diketahui\n")
  yakin = input("Yakin Mau Download? (y/n) > ")
  while yakin == "":
   print("Jgn Kosong Bgsd")
   yakin = input("Yang Bener (y/n) > ")
  if yakin in ("y","Y"):
   output = input("[?] Output > ").replace(" ","_")
   exten = input("[?] Extensi File (apk, mp4, Etc) > ")
   print("\nMendownload...")
   r = requests.get(link, stream=True, allow_redirects=True)
   with open(f"{output}.{exten}", "wb") as MEMEK:
    dl = 0
    total_panjang = int(r.headers.get("content-length"))
    for KNTL in r.iter_content(chunk_size=4096):
     dl += len(KNTL)
     MEMEK.write(KNTL)
     done = int(43 * dl / total_panjang)
     sys.stdout.write("\r[%s%s]" % ('#' * done, ' ' * (43-done)) )
     sys.stdout.flush()
  elif ragu in ("n","N"):
   exit("Ga Niat Njink")
  else:
   exit("Ga Niat Njink")
def main():
 os.system("clear")
 print(f"{bold}================================")
 print(f"""{bold}███████╗███████╗██╗██╗     ███████╗
██╔════╝██╔════╝██║██║     ██╔════╝
███████╗█████╗  ██║██║     █████╗By {white}Xolva{red}ID{off}
╚════██║██╔══╝  ██║██║     ██╔══╝
███████║██║     ██║███████╗███████╗
╚══════╝╚═╝[V.1]╚═╝╚══════╝╚══════╝""")
 print(f"{bold}================================")
 print(f"[{cyan}00{off}{bold}] Exit Script")
 print(f"[{cyan}01{off}{bold}] Download From Link")
 print(f"[{cyan}02{off}{bold}] Check SFile Account")
 print(f"[{cyan}03{off}{bold}] Search File")
 print(f"[{cyan}04{off}{bold}] Realsht Bypass")
 print(f"[{cyan}05{off}{bold}] Other Tools")
 print(f"[{cyan}69{off}{bold}] About")
 print(f"{bold}================================\n")
 p = input(f"Input {red}>>>{green}  ")
 print(f"{off}\n")
 while p == "":
  print("Jgn Kosong Bgst")
  p = input(f"[?] Input >  ")
 if p in ("1","01"):
  KONTOL.BESAR()
 elif p in ("",""):
  KONTOL.KECIL()
 elif p in ("02","2"):
  KONTOL.LOGIN()
 elif p in ("03","3"):
  KONTOL.SEARCH()
 elif p in ("04","4"):
  KONTOL.REALSHT()
 elif p in ("05","5"):
  os.system("xdg-open https://github.com/XolvaID")
  exit()
 elif p in ("69"):
  os.system("clear")
  print("=========================")
  print("Telegram : @XolvaID")
  print("CH Tele  : @XolvaCode")
  print("=========================")
  time.sleep(4)
  main()
 else:
  exit("Dahlah")

if __name__ == "__main__":
 main()
