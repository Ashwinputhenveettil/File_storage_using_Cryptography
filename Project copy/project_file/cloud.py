from ftplib import FTP

ftp = FTP('')
ftp.connect('ftp.drivehq.com')
ftp.login("username", "password")
ftp.cwd('/File_Storage/') #replace with your directory
ftp.retrlines('LIST')
print(ftp.pwd())


def uploadFile(filename, path):
 ftp.storbinary('STOR '+filename, open(path, 'rb'))
 
def downloadFile(filename):
 localfile = open("Project/downdes.txt", 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

def close():
 ftp.quit()
