import os
import filecmp

class CompareResults:

    def __init__(self, tests_file='tests.txt'):
        self.path_to_src = '*.java'
        self.tests_file = tests_file
        self.marks = 0
        self.tests = {}
        self.commands = {}
        self.compared_files = ["tracefile_clock", "tracefile_LRU"]

        # 1. read the configuration files
        with open(self.tests_file) as tf:
            for line in tf.readlines():
                commands_file, test_name, mark = line.split()
                self.tests[test_name] = int(mark)
                self.commands[test_name] = commands_file

        # 2. compile java files
        cmd = 'javac -nowarn ' + self.path_to_src
        ret = os.system(cmd)
        if ret:
            print('Compilation error')
            exit()
        marks = self.marks + 1

    def compare(self):
        i = 0
        for test_name in self.tests.keys():
            print('\n*****************Starting Test*******************')
            print(test_name, '.............')

            CMD = self.commands[test_name]
            cmd = 'java MemoryManagement ' + CMD + ' ' + test_name + '.conf'
            ret = os.system(cmd)

            if ret:
                print('Runtime Error in Test ' + test_name)
                continue

            compare_file = self.compared_files[i]
            passed = filecmp.cmp(compare_file, test_name+'.test', shallow=False)

            if passed:
                print(test_name, 'passed.', 'Marks:', self.tests[test_name])
                self.marks += self.tests[test_name]
            else:
                print(test_name, 'failed.')

            i += 1

        print('\n*******************Test Over*********************')

if __name__=="__main__":
    com = CompareResults()
    com.compare()



