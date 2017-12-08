import jieba
import jieba.analyse
from vector import vector
import numpy
import gnrtTemplate


def setZero(vec):
    return vector(vec.word, 0.0)


def filte(userTemplate, inputModel):
    u_i = list(set(userTemplate).difference(set(inputModel)))
    i_u = list(set(inputModel).difference(set(userTemplate)))
    u_i = list(map(setZero, u_i))
    i_u = list(map(setZero, i_u))
    im = inputModel + u_i
    ut = userTemplate + i_u
    im.sort()
    ut.sort()
    im = list(map(lambda vec: vec.weight, im))
    ut = list(map(lambda vec: vec.weight, ut))
    # print(im,ut)
    x = numpy.array(im)
    y = numpy.array(ut)
    Lx = numpy.sqrt(x.dot(x))
    Ly = numpy.sqrt(y.dot(y))
    cos_angle = x.dot(y) / (Lx * Ly)
    return ('%.4f' % numpy.dot(im, ut), '%.4f' % cos_angle)


if __name__ == '__main__':
    inputModel = []
    with open(r"C:\Users\wenqh\Desktop\config.txt", 'rb') as f:
        text = f.read()
    words = jieba.analyse.extract_tags(text, topK=20, withWeight=True)
    for word in words:
        word = vector(word[0], word[1])
        inputModel.append(word)
    allUserTemplate = gnrtTemplate.fromText()
    for userTemplate in allUserTemplate:
        print(filte(userTemplate, inputModel))
