from __future__ import print_function
import numpy as np
import tensorflow as tf
import pprint
import string
import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

pp = pprint.PrettyPrinter(indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save',
                        help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=10000,
                        help='number of characters to sample')
    parser.add_argument('--prime', type=str, default=' ',
                        help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                        help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')

    args = parser.parse_args()
    s = sample(args)
    print(s)
    return s

def sample(args):
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            p = model.sample(sess, chars, vocab, args.n, args.prime, args.sample)
            return(p)
            p = p.replace('\n', ", ")
            p = p.strip("'")
            p = p.strip('"')
            p = "".join([c for c in p if c in string.letters or c in string.whitespace or c == ","])

            # try:
            #     os.system("say " + str(p))
            # except:
            #     pass

if __name__ == '__main__':
    main()
