#!/usr/bin/python3

import os
import sys
import math

import array

import statistics



class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = map(int,f.readline().split())  # TODO: прочитать из файла
            self._titles = []
            self._sizes = array.array('L', [0] * n)
            self._links = array.array('L', [0] * _nlinks)
            self._redirect = array.array('B', [0] * n)
            self._offset = array.array('L', [0] * (n + 1))
            l = 0
            for i in range(n):
                title = f.readline()
                self._titles.append(title)
                size, redirect, amount_links = map(int, f.readline().split())
                self._sizes[i] = size
                self._redirect[i] = redirect

                self._offset[i] = l
                for j in range(amount_links):
                    self._links[j] = int(f.readline)
                    l += 1
            self._offset[n] = l


        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[_offset[_id]:_offset[_id + 1]]

    def get_id(self, title):
        return len(self._titles)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл



if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)


    def bfs(g, start, finish):
        dist=[-1 for i in range(len(g))]
        pass