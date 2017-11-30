
import os
import subprocess


dd = 'type D:\\github\\iwall_test\\testcases\\general\\11105_SQL_injection_3.case | D:\\github\\iwall_test\\tools\\ncat.exe 192.168.120.227 80';
print (dd)
httptest=subprocess.Popen( dd, shell=True, stdout=subprocess.PIPE)
returnCode = httptest.wait()
print "returnCode:",returnCode
stdout = httptest.communicate()
print stdout
#file=httptest.stdout.readline()
#httptest1=subprocess.Popen(['F:\\iwall_test\\tools\\ncat.exe 192.168.120.227 80',file],stdout=test)
