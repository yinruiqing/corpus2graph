from corpus2graph import FileParser, WordPreprocessor, Tokenizer, WordProcessing, \
    SentenceProcessing, WordPairsProcessing, util
from corpus2graph.applications import wordpair_generator, igraph_wrapper
# from ..word_processor import FileParser, WordPreprocessor, Tokenizer
# from ..word_processing import WordProcessing
# from ..wordpair_processing import WordPairsProcessing
# from ..sentence_processing import SentenceProcessing
# from ..util import count_time

import time
import configparser

config = configparser.ConfigParser()
config.read('corpus2graph/test/config.ini')

"""run command below in Code/corpus2graph folder
python -m corpus2graph.server_test.py
"""

# data_folder = '/Users/zzcoolj/Code/GoW/data/training data/Wikipedia-Dumps_en_20170420_prep/'

# data_folder = '/dev/shm/zzheng-tmp/prep/'
# data_folder = '/dev/shm/zzheng-tmp/prep_partial/'
data_folder = '/dev/shm/zzheng-tmp/prep_3_files/'

output_folder = 'server_output/'
# TODO create edges, dicts, graph folder based on output_folder, no need to define them below.
dicts_folder = output_folder + 'dicts_and_encoded_texts/'
edges_folder = output_folder + 'edges/'
graph_folder = output_folder + 'graph/'

max_window_size = 5
process_num = 1
min_count = 0
max_vocab_size = 'None'

start_time = time.time()
wp = WordProcessing(output_folder=dicts_folder, word_tokenizer='', wtokenizer=Tokenizer.mytok,
                    remove_numbers=False, remove_punctuations=False, stem_word=False, lowercase=False)
merged_dict = wp.apply(data_folder=data_folder, process_num=process_num)
print('time in seconds:', util.count_time(start_time))

start_time = time.time()
sp = SentenceProcessing(dicts_folder=dicts_folder, output_folder=edges_folder,
                        max_window_size=max_window_size, local_dict_extension=config['graph']['local_dict_extension'])
word_count_all = sp.apply(data_folder=dicts_folder, process_num=process_num)
print('time in seconds:', util.count_time(start_time))

start_time = time.time()
wpp = WordPairsProcessing(max_vocab_size=max_vocab_size, min_count=min_count,
                          dicts_folder=dicts_folder, window_size=max_window_size,
                          edges_folder=edges_folder, graph_folder=graph_folder,
                          safe_files_number_per_processor=config['graph']['safe_files_number_per_processor'])
result = wpp.apply(process_num=process_num)
print('time in seconds:', util.count_time(start_time))


# # igraph naive
# start_time = time.time()
# data_folder = '/dev/shm/zzheng-tmp/prep_3_files/'
# wg = wordpair_generator.WordsGenerator(window_size=max_window_size,
#                                        xml_node_path=None, word_tokenizer='', wtokenizer=Tokenizer.mytok,
#                                        remove_numbers=False, remove_punctuations=False,
#                                        stem_word=False, lowercase=False)
# igt = igraph_wrapper.IGraphWrapper('Test')
# for w1, w2 in wg(data_folder):
#     igt.addPair(w1, w2)
# graph = igt.getGraph()
# print('time in seconds:', util.count_time(start_time))
