import os
import sys
import errno
from fuse import FUSE, FuseOSError, Operations
# pip install fuse-python

## É NECESSÁRIO CORRER O PROGRAMA COM ROOT PRIVILEGES!!

"""
To use libfuse in Python, you can use the FUSE-Python package.
Here's an example of how to use FUSE-Python to create a simple file system:

In this example, MyFileSystem is a class that implements the file system operations using the FUSE-Python API.
The getattr, readdir, and read methods correspond to the getattr, readdir, and read operations in the file system, respectively.

---> Implementar um open() e um write()

__init__ : initilize the filesystem, set up any necessary state for the file system.

The FUSE call at the end sets up the file system and mounts it at the specified mount_point. The nothreads and foreground options specify that the file system should be run in the foreground and without multithreading.

You can run this script with python myfs.py /mnt/myfs to mount the file system at /mnt/myfs. Note that you'll need to run this script with root privileges to be able to mount the file system.

This is just a simple example to get you started. You can add other required methods for file system operations, such as open, write, and unlink, as needed for your file system. You can also add your own logic to implement access control and OTP verification, as required by the project description.

"""

class MyFileSystem(Operations):
    def __init__(self):
        # Initialize the file system
        pass

    def getattr(self, path, fh=None):
        # Get file attributes
        return os.lstat(path)

    def readdir(self, path, fh):
        # Read directory contents
        dirents = ['.', '..']
        dirents.extend(os.listdir(path))
        for r in dirents:
            yield r

    def read(self, path, size, offset, fh):
        # Read from a file
        with open(path, 'rb') as f:
            f.seek(offset)
            return f.read(size)

    # Add other required methods for file system operations

    # def open(...)

    # def write(...)

if __name__ == '__main__':
    mount_point = sys.argv[1]
    FUSE(MyFileSystem(), mount_point, nothreads=True, foreground=True)
