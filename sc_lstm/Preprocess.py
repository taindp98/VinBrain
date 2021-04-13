#coding:utf-8
import numpy as np
# import tensorflow as tf
# import cPickle, os, collections
import os
import collections
import pickle
import Config

config = Config.Config()
config.vocab_size += 4

def Read_WordVec(config):
    # with open(config.vec_file, 'r') as fvec:
    with open('/home/taindp/VINBRAIN_INTERNSHIP/SC-LSTM/Data/vec5.txt','r') as fvec:
        wordLS = []
        vec_ls =[]
        fvec.readline()
        
        wordLS.append(u'PAD')
        vec_ls.append([0]*config.word_embedding_size)
        wordLS.append(u'START')
        vec_ls.append([0]*config.word_embedding_size)
        wordLS.append(u'END')
        vec_ls.append([0]*config.word_embedding_size)
        wordLS.append(u'UNK')
        vec_ls.append([0]*config.word_embedding_size)
        # print(len(fvec))
        for line in fvec:
            # print('line',line)
            line = line.split()
            try:
                word = line[0].encode('utf-8').decode('utf-8')
                vec = [float(i) for i in line[1:]]
                assert len(vec) == config.word_embedding_size
                wordLS.append(word)
                vec_ls.append(vec)
            except:
                print (line[0])
        # assert len(wordLS) == config.vocab_size
        word_vec = np.array(vec_ls, dtype=np.float32)
        
        # cPickle.dump(word_vec, open('word_vec.pkl','w'), protocol=cPickle.HIGHEST_PROTOCOL)
        # cPickle.dump(wordLS, open('word_voc.pkl','w'), protocol=cPickle.HIGHEST_PROTOCOL)
        with open('/home/taindp/VINBRAIN_INTERNSHIP/SC-LSTM/Data/word_vec.pkl','wb') as handle:
            pickle.dump(word_vec, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('/home/taindp/VINBRAIN_INTERNSHIP/SC-LSTM/Data/word_voc.pkl','wb') as handle:
            pickle.dump(wordLS, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # pickle.dump((word_vec, open('word_vec.pkl','w'), protocol=pickle.HIGHEST_PROTOCOL)
        # pickle.dump((wordLS, open('word_voc.pkl','w'), protocol=pickle.HIGHEST_PROTOCOL)
    return wordLS, word_vec

def Create_Keyword_Voc(config):
    kwd_ls = []
    with open(os.path.join(config.data_dir, 'TrainingData_Keywords.txt'), 'r') as fr:
        for line in fr:
            kwd = line.encode('utf-8').decode('utf-8').split()
            kwd_ls += kwd
        
        c = collections.Counter(kwd_ls)
        
        kwd_voc = []
        for word in c:
            if c[word] >= config.keyword_min_count:
                kwd_voc.append(word)
        
        # print ('size of keyword vocabulary:', len(kwd_voc))
        # cPickle.dump(kwd_voc, open('kwd_voc.pkl','w'), protocol=cPickle.HIGHEST_PROTOCOL)
        with open('/home/taindp/VINBRAIN_INTERNSHIP/SC-LSTM/Data/kwd_voc.pkl','wb') as handle:
            pickle.dump(kwd_voc, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    return kwd_voc

def Read_Data(config, kwd_voc):
    trainingdata = []
    with open(os.path.join(config.data_dir, 'TrainingData_Text.txt'),'r') as ftext, open(os.path.join(config.data_dir, 'TrainingData_Keywords.txt'),'r') as fkwd:
        for line1, line2 in zip(ftext, fkwd):
            line1 = line1.encode('utf-8').decode('utf-8')
            doc = line1.split()
            line2 = line2.encode('utf-8').decode('utf-8')
            keywords = [word for word in line2.split() if word in kwd_voc]
            
            trainingdata.append((doc, keywords))
    return trainingdata
    
# print ('loading the trainingdata...')
DATADIR = config.data_dir
vocab, _ = Read_WordVec(config)
key_word_voc = Create_Keyword_Voc(config)
data = Read_Data(config, key_word_voc)

word_to_idx = { ch:i for i,ch in enumerate(vocab) }
idx_to_word = { i:ch for i,ch in enumerate(vocab) }
data_size, _vocab_size = len(data), len(vocab)

# print ('data has %d document, size of word vocabular: %d.' % (data_size, _vocab_size))

keyword_voc_size = len(key_word_voc)
keyword_to_idx = { ch:i for i,ch in enumerate(key_word_voc) }
    
def data_iterator(trainingdata, batch_size, num_steps):
    epoch_size = len(trainingdata) // batch_size
    for i in range(epoch_size):
        batch_data = trainingdata[i*batch_size:(i+1)*batch_size]
        raw_data = []
        key_words = []
        for it in batch_data:
            raw_data.append(it[0])
            tmp = np.zeros(keyword_voc_size)
            for wd in it[1]:
                ## keyword --> slot 
                # print('>'*50)
                # print(wd)
                # print('>'*50)
                tmp[keyword_to_idx[wd]] = 1.0
            key_words.append(tmp)
        # print('>'*50)
        # print(key_words)
        # print('>'*50)
            
        data = np.zeros((len(raw_data), num_steps+1), dtype=np.int64)
        for i in range(len(raw_data)):
            doc = raw_data[i]
            tmp = [1]
            for wd in doc:
                if wd in vocab:
                    tmp.append(word_to_idx[wd])
                else:
                    tmp.append(3)
            tmp.append(2)        
            tmp = np.array(tmp, dtype=np.int64)
            _size = tmp.shape[0]
            data[i][:_size] = tmp
        
        key_words = np.array(key_words, dtype=np.float32)
        
        x = data[:, 0:num_steps]
        # print('>'*50)
        # print(x)
        # print('>'*50)
        y = data[:, 1:]

        # print('>'*50)
        # print(y)
        # print('>'*50)
        mask = np.float32(x != 0)
        yield (x, y, mask, key_words)


train_data = data

# print('='*50)

# writer = tf.python_io.TFRecordWriter("sclstm_data")

# dataLS = []

# for step, (x, y, mask, key_words) in enumerate(data_iterator(train_data, config.batch_size, config.num_steps)):
#     example = tf.train.Example(
#         # Example contains a Features proto object
#         features=tf.train.Features(
#           # Features contains a map of string to Feature proto objects
#           feature={
#             # A Feature contains one of either a int64_list,
#             # float_list, or bytes_list
#             'input_data': tf.train.Feature(
#                 int64_list=tf.train.Int64List(value=x.reshape(-1).astype("int64"))),
#             'target': tf.train.Feature(
#                 int64_list=tf.train.Int64List(value=y.reshape(-1).astype("int64"))),
#             'mask': tf.train.Feature(
#                 float_list=tf.train.FloatList(value=mask.reshape(-1).astype("float"))),
#             'key_words': tf.train.Feature(
#                 float_list=tf.train.FloatList(value=key_words.reshape(-1).astype("float"))),       
#     }))
#     # use the proto object to serialize the example to a string
#     serialized = example.SerializeToString()
#     #dataLS.append(kwd_pos)
#     # write the serialized object to disk
#     writer.write(serialized)
    
# print 'total step: ',step