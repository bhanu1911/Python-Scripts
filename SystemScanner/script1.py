import platform
import psutil
import json
import datetime
from subprocess import Popen, PIPE
from re import split

s = {}
s['system variables'] = {}
s['windows'] = {}
# s['processes'] = {}
if (platform.system() == 'Windows'):
    s['windows']['Windows version'] = platform.platform()

# class Proc(object):
#$    ''' Data structure for a processes . The class properties are
#$    process attributes '''
#$    def __init__(self, proc_info):
#$        self.user = proc_info[0]
#$        self.pid = proc_info[1]
#$        self.cpu = proc_info[2]
#$        self.mem = proc_info[3]
#$        self.vsz = proc_info[4]
#$        self.rss = proc_info[5]
#$        self.tty = proc_info[6]
#$        self.stat = proc_info[7]
#$        self.start = proc_info[8]
#$        self.time = proc_info[9]
#$        self.cmd = proc_info[10]
#$
#$    def to_str(self):
#$        ''' Returns a string containing minimalistic info
#$        about the process : user, pid, and command '''
#$        return '%s %s %s' % (self.user, self.pid, self.cmd)
#$
#$def get_proc_list():
#$    process list list '''
#$    proc_list = []
#$    sub_proc = Popen(['ps', 'aux'], stdout = PIPE, shell = False)
#$    #Discard the first line (ps aux header)
#$    sub_proc.stdout.readline()
#$        #The separator for splitting is 'variable number of spaces'
#$        proc_info = split(" *", line.strip())
#$        proc_list.append(Proc(proc_info))
#$    return proc_list
#$
#$f __name__ == "__main__":
#$    proc_list = get_proc_list()
#$    #Show the minimal proc list (user, pid, cmd)
#$    #stdout.write('Process list:n')
#    k = 0
#$for proc in proc_list:
#$#        stdout.write('t' + proc.to_str() + 'n')
#$        k = k + 1
#$    #Build &amp; print a list of processes that are owned by root
#$#(proc.user == 'root')
#$    j = 0
#$    root_proc_list = [ x for x in proc_list if x.user == 'root' ]
#$    # stdout.write('Owned by root:n')
#$    for proc in root_proc_list:
#$    #    stdout.write('t' + proc.to_str() + 'n')
#$        s['processes'][j] = proc
#$        j = j + 1

def secs2hours(secs):
	mm, ss = divmod(secs, 60)
	hh, mm = divmod(mm, 60)
	return "%d:%02d:%02d" % (hh, mm, ss)

def bytes2gb(bytes, bsize=1024):
        r = float(bytes)
        r = r / (bsize*bsize*bsize)
        return(r)

battery = psutil.sensors_battery()

s['system variables']['OS'] = platform.system()
s['system variables']['release'] = platform.release()
s['system variables']['Version'] = platform.version()
s['system variables']['cpu times '] = psutil.cpu_times()
s['system variables']['cpu percent '] = psutil.cpu_percent()
s['system variables']['cpu count logical '] = psutil.cpu_count(logical=True)
s['system variables']['cpu count physical '] = psutil.cpu_count()
s['system variables']['cpu statistics '] = psutil.cpu_stats()
s['system variables']['cpu frequency per cpu'] = psutil.cpu_freq(percpu = True)

mem = psutil.virtual_memory()

s['RAM']={}
s['RAM']["Total"]=str(bytes2gb(mem.total))+'GB'
s['RAM']["Available"]=str(bytes2gb(mem.available))+'GB'
s['RAM']["Used"]=str(bytes2gb(mem.used))+'GB'

s['system variables']['swap space'] =  psutil.swap_memory()
s['system variables']['disk partitions'] = psutil.disk_partitions()
s['system variables']['disk usage by root'] = psutil.disk_usage('/')
s['system variables']['disk i/o counters'] = psutil.disk_io_counters()
s['system variables']['network i/o counters (per NIC)'] = psutil.net_io_counters(pernic = True)
s['system variables']['network connections'] = psutil.net_connections()
s['system variables']['network addresses'] = psutil.net_if_addrs()
s['system variables']['network statistics'] = psutil.net_if_stats()
#s['system variables']['sensor temperature'] = psutil.sensors_temperatures()
s['system variables']['fans'] = psutil.sensors_fans()
s['system variables']['Battery Left']=secs2hours(battery.secsleft)
s['system variables']['Battery Percentage'] = battery.percent
s['system variables']['boot time'] = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
s['system variables']['users'] = psutil.users()

with open('systeminfo.json', 'w') as outfile:
        outfile.write(json.dumps(s,sort_keys=True, ensure_ascii=False,indent = 4,))
