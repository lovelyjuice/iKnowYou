import os


class Reader():
    dir_path = 'articles'

    @classmethod
    def getText(cls):
        textSet = []
        for root, dirs, files in os.walk(cls.dir_path):
            if files.__len__ != 0:
                for file in files:
                    with open(root +"\\"+ file, 'rb') as f:
                        textSet.append(f.read())
        # print(textSet.__len__())
        return textSet
