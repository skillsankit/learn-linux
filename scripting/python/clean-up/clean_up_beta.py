import os
from datetime import date, timedelta, datetime
from os.path import isfile, join, getmtime, getctime

lastfifthday = date.today() - timedelta(5)

print("Five days back date:", lastfifthday)

# mypath = "C:\\Users\\harikrishna\\Desktop\\Foxia\\foxia-original\\foxia\\blue-2"

mypath = "/home/maxx/Desktop/cleanup-beta"

# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

listoffiles = []

for file in os.listdir(mypath):
    if (isfile(join(mypath, file))):
        if (datetime.fromtimestamp(os.path.getmtime(join(mypath, file))).date() < lastfifthday):


            listoffiles.append(join(mypath, file))
            # listoffiles.append(datetime.fromtimestamp(os.path.getmtime(join(mypath, file))).date())

            # os.remove(join(mypath, file))
            
            # listoffiles.append(file)



print(listoffiles)

# name_list = os.listdir(mypath)

# full_list = [os.path.join(mypath,i) for i in name_list]

# print(full_list)
 

# path = "C:\\Users\\harikrishna\\Desktop\\Foxia\\foxia-original\\foxia\\blue-2"
# name_list = os.listdir(path)
# full_list = [os.path.join(path,i) for i in name_list]
# time_sorted_list = sorted(full_list, key=os.path.getctime)

# print (time_sorted_list)

# # if you want just the filenames sorted, simply remove the dir from each
# sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
# print (sorted_filename_list)



# path to the directory (relative or absolute)
# dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

# dirpath = "C:\\Users\harikrishna\Desktop\Foxia\\foxia-original\\foxia\\blue-2"

# # get all entries in the directory w/ stats
# entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
# entries = ((os.stat(path), path) for path in entries)

# # leave only regular files, insert creation date
# entries = ((stat[ST_CTIME], path)
#            for stat, path in entries if S_ISREG(stat[ST_MODE]))
# #NOTE: on Windows `ST_CTIME` is a creation date 
# #  but on Unix it could be something else
# #NOTE: use `ST_MTIME` to sort by a modification date

# for cdate, path in sorted(entries):
#     print (time.ctime(cdate), os.path.basename(path))