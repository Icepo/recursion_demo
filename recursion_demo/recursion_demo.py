# coding:utf-8
import os
import os.path
import re
import tarfile
import time


class NumCounter(object):

    tar_regex = r'resource\\(\d{2}\\)*\d{2}\.tar\.gz'
    total_num = 0
    total_dir = 0
    total_file = 0

    def count(self, path):
        if re.match(self.tar_regex, path):
            self.unpack_path_file(path)
            packed_path = path[:-7]
            if os.path.isdir(packed_path):
                self.total_dir += 1
                for list_file in os.listdir(packed_path):
                    real_path = os.path.join(packed_path, list_file)
                    self.count(real_path)
            elif os.path.isfile(packed_path):
                self.total_file += 1
                num_file = os.open(packed_path, os.O_RDONLY)
                num = os.read(num_file, 1024)
                os.close(num_file)
                self.total_num += int(num)

    # 解压文件到当前目录
    @staticmethod
    def unpack_path_file(tar_path):
        target_path = os.path.split(tar_path)[0]
        archive = tarfile.open(tar_path, 'r:gz')
        archive.extractall(path=target_path)
        archive.close()
if __name__ == "__main__":
    root_path = 'resource'+os.path.sep+'00.tar.gz'
    start_stamp = time.time()
    numCounter = NumCounter()
    numCounter.count(root_path)
    print '用时：'+str(time.time()-start_stamp)
    print '目录：'+str(numCounter.total_dir)
    print '文件：'+str(numCounter.total_file)
    print '结果：'+str(numCounter.total_num)

