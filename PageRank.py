import sys, string, math
from math import log
from math import modf
import operator

outlink_dict = {}
inlink_dict = {}
PRank = {}
new_PRank = {}
Pages = []
SortedPR = []
topic_array = []

d = 0.85

def parse_file(inlink, topic):
    input = open(inlink, 'r')
    for line in input.readlines():
        words = []
        words = string.split(line)
        inlink_dict[words[0]] = words[1:]
        Pages.append(words[0])

    for word in string.split(open(topic, 'r').readline()):
        topic_array.append(word)
    print(topic_array)

    len_dic = float(len(Pages))
    for page in Pages:
        PRank[page] = float(1) / len_dic

    for page in inlink_dict.keys():
        for q in inlink_dict[page]:
            if outlink_dict.has_key(q):
                outlink_dict[q] += 1
            else:
                outlink_dict[q] = 1

def cal_pagerank():
    len_dic = float(len(inlink_dict.keys()))
    ite = 0

    while(ite < 100):
        print(ite)
        for page in PRank.keys():
            new_PRank[page] = float(1 - d) / len_dic
            for q in inlink_dict[page]:
                new_PRank[page] = new_PRank[page] + (d * float(PRank.get(q)) / float(outlink_dict.get(q)))
        for page in new_PRank.keys():
            PRank[page] = new_PRank.get(page)
        ite = ite + 1

def cal_topic_sensitive_pagerank():
    len_dic = float(len(inlink_dict.keys()))
    ite = 0

    while(ite < 100):
        print(ite)
        for page in PRank.keys():
            topic_related_page = 1 if page in topic_array else 0
            if topic_related_page == 1:
                print(page)
            new_PRank[page] = (float(1 - d)*topic_related_page) / float(len(topic_array))
            for q in inlink_dict[page]:
                new_PRank[page] = new_PRank[page] + (d * float(PRank.get(q)) / float(outlink_dict.get(q)))
        for page in new_PRank.keys():
            PRank[page] = new_PRank.get(page)
        ite = ite + 1

def top_rank():
    SortedPR = sorted(PRank.iteritems(), key=operator.itemgetter(1), reverse=True)
    for i in range(50):
        print (SortedPR[i])

if __name__ == "__main__":
    # if len(sys.argv) == 2:
        inlink = 'wt2g_inlinks.txt'
        topic = 'wt2g_example_topic.txt'
        parse_file(inlink, topic)
        cal_topic_sensitive_pagerank()
        top_rank()
    # else:
        print("Enter the inlink file for which page link should be calculated")
