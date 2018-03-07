__author__ = 'Ruiqing YIN'

import unittest
from corpus2graph.applications import wordpair_generator, igraph_wrapper
from corpus2graph import FileParser, WordPreprocessor, Tokenizer, WordProcessing, \
    SentenceProcessing, WordPairsProcessing

import configparser
config = configparser.ConfigParser()
config.read('config.ini')


class TestIGraph(unittest.TestCase):
    """ ATTENTION
    Normally, data_folder and output_folder should be user defined paths (absolute paths).
    For unittest, as input and output folders locations are fixed, these two paths are exceptionally relative paths.
    """
    data_folder = '../test/unittest_data/'

    file_extension = '.txt'
    max_window_size = 6
    process_num = 3
    data_type = 'txt'
    min_count = 5
    max_vocab_size = 3

    def test_graph_tool_wrapper(self):
        wg = wordpair_generator.WordsGenerator(window_size=3, file_parser='txt',
                     xml_node_path=None, word_tokenizer='WordPunct',
                     remove_numbers=True, remove_punctuations=True,
                     stem_word=True, lowercase=True)

        igt = igraph_wrapper.IGraphWrapper('Test')
        for w1,w2 in wg(self.data_folder):
            igt.addPairs(w1, w2)

        graph = igt.getGraph()