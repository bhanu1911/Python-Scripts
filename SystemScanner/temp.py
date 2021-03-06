from subprocess import Popen, PIPE
from re import split
from sys import stdout

class Proc(object):
    ''' Data structure for a processes . The class properties are
    process attributes '''
    def __init__(self, proc_info):
        self.user = proc_info[0]
        self.pid = proc_info[1]
        self.cpu = proc_info[2]
        self.mem = proc_info[3]
        self.vsz = proc_info[4]
        self.rss = proc_info[5]
        self.tty = proc_info[6]
        self.stat = proc_info[7]
        self.start = proc_info[8]
        self.time = proc_info[9]
        self.cmd = proc_info[10]

    def to_str(self):
        ''' Returns a string containing minimalistic info
        about the process : user, pid, and command '''
        return '%s %s %s' % (self.user, self.pid, self.cmd)

def get_proc_list():
    ''' Retrieves a list [] of Proc objects representing the active
    process list list '''
    proc_list = []
    sub_proc = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
    #Discard the first line (ps aux header)
    sub_proc.stdout.readline()
    for line in sub_proc.stdout:
        #The separator for splitting is 'variable number of spaces'
        proc_info = split(" *", line.strip())
        proc_list.append(Proc(proc_info))
    return proc_list

if __name__ == "__main__":
    proc_list = get_proc_list()
    #Show the minimal proc list (user, pid, cmd)
    stdout.write('Process list:n')
    for proc in proc_list:
        stdout.write('t' + proc.to_str() + 'n')
        # s['processes']['not root'] = proc
    #Build &amp; print a list of processes that are owned by root
    #(proc.user == 'root')
    root_proc_list = [ x for x in proc_list if x.user == 'root' ]
    stdout.write('Owned by root:n')
    for proc in root_proc_list:
        stdout.write('t' + proc.to_str() + 'n')
        #s['processes']['root'] = proc
