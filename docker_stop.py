#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type: text/html")
form= cgi.FieldStorage()
cname= form.getvalue("s")
cmd= "sudo docker stop {}".format(cname)
x= sp.getoutput(cmd)
print("location: http://192.168.56.101/cgi-bin/docker_run.py")
print()

