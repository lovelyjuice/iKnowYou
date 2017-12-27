import os
import shutil

import jieba.analyse
import numpy

import gnrtTemplate
from vector import vector


def setZero(vec):
    return vector(vec.word, 0.0)


def compare(userTpl, inputMdl):
    u_i = list(set(userTpl) - set(inputMdl))
    i_u = list(set(inputMdl) - set(userTpl))
    u_i = list(map(setZero, u_i))
    i_u = list(map(setZero, i_u))
    im = inputMdl + u_i
    ut = userTpl + i_u
    im.sort()
    ut.sort()
    im = list(map(lambda vec: vec.weight, im))
    ut = list(map(lambda vec: vec.weight, ut))
    x = numpy.array(im)
    y = numpy.array(ut)
    Lx = numpy.sqrt(x.dot(x))
    Ly = numpy.sqrt(y.dot(y))
    cos_angle = x.dot(y) / (Lx * Ly)
    # return ('%.4f' % numpy.dot(im, ut), '%.4f' % cos_angle)
    return cos_angle


if __name__ == '__main__':
    inputPath = 'input'
    edge = 0.1
    for root, dirs, files in os.walk(inputPath):
        if files.__len__ != 0:
            for file in files:
                inputFile = root + "\\" + file
                inputModel = []
                with open(inputFile, 'rb') as f:
                    text = f.read()
                words = jieba.analyse.extract_tags(text, topK=20, withWeight=True)
                for word in words:
                    word = vector(word[0], word[1])
                    inputModel.append(word)
                allUserTemplates = gnrtTemplate.fromText()
                for userTemplate in allUserTemplates:
                    cos = compare(userTemplate, inputModel)
                    if cos > edge:
                        print(inputFile, cos)
                        shutil.copy(inputFile, 'guessyoulike')
                        break
