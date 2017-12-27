import jieba
import jieba.analyse

from vector import vector


def fromText():
    template = []
    from trianIn import Reader
    articleSet = Reader.getText()
    for article in articleSet:
        template_line = []
        words = jieba.analyse.extract_tags(article, topK=20, withWeight=True)
        for word in words:
            word = vector(word[0], word[1])
            template_line.append(word)
        template.append(template_line)
    # print(template)

    return template


if __name__ == '__main__':
    fromText()
