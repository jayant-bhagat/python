import argparse
import os
import sys

ssh_template = '''
      HOST {name}
          HostName {hostname}
          User {user}
          Port {port}
          '''

def args_to_obj(args):
        obj = ssh_template.format(**args)
        return obj

def add_to_conf(conf, obj):
       conf = os.path.expanduser(conf)
       with open (conf, 'a') as f:
           f.write(obj)

def main():
   parser = argparse.ArgumentParser(prog = "adding ssh")
   parser.add_argument('name', help = "This s name of hosts to be difine")
   parser.add_argument('hostname', help = "Please define hostname for proper host")
   parser.add_argument('--user', default = 'root',   help = "Put username for host" )
   parser.add_argument('--port', default = 22, type = int, help = "Give port got ssh for remote host" )
   parser.add_argument('--conf',  default = '~/.ssh/config', help = "default location")
   args = parser.parse_args()

   obj = args_to_obj(args.__dict__)
   print(obj)
   add_to_conf(args.conf,obj)
main()

