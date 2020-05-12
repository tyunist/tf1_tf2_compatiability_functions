"""
tf1_tf2_functions.py 
A simpler wrapper for Tensorflow functions that are compatible with both Tensorflow 1 and Tensorflow 2
@Author: Ty Nguyen
@Email: tynguyen@seas.upenn.edu
"""

import tensorflow as tf
# tf.app                                                                                                                                     
if int(tf.__version__[0]) == 2:                                                                                                              
    tf_app = tf.compat.v1.app                                                                                                           
    tf_io  = tf.io                                                                                                          
else:                                                                                                                     
    tf_app = tf.app                                                                                                                            
    tf_io  = tf.python_io


def print_docs(): 
    '''
    * Installation 
    cd tf1_tf2_compatibility_functions
    python setup.py install

    * Usage
    from tf1_tf2_functions import * 
    
    >> Instead of calling, tf.app.run() in TF1 or tf.compat.v1.app.run() in TF2, 
    call tf_app.run()

    >> Instead of calling, tf.io.TFRecordWriter() in TF2, or tf.python_io.TFRecordWriter() in TF2, 
    call tf_io.TFRecordWriter()
    '''

if __name__=="__main__":
    # Usage 
    print_docs.__doc__ 
