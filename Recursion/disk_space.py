# Calculating the size of directories- O(n).
import os
def disk_usage(path):
    # return num of bytes used by folder or file and any sub in them.
    total = os.path.getsize(path)     # account for direct usage.
    if os.path.isdir(path):         # if this is a directory.
        for filename in os.listdir(path):  # then for each child
            child_path = os.path.join(path,filename) # add child's usage to total.
            total += disk_usage(child_path)   # {recursive call}

    print('{0:<15}'.format(total),path)  # discribtive output(optional).
    return total                        # return grand total.
disk_usage('/home/ahmed/Desktop')
