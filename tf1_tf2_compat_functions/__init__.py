"""
tf1_tf2_compat_functions package 
A simpler wrapper for Tensorflow functions that are compatible with both Tensorflow 1 and Tensorflow 2
@Author: Ty Nguyen
@Email: tynguyen@seas.upenn.edu
"""

import tensorflow as tf
# tf.app                                                                                                                                     
if int(tf.__version__[0]) == 2:                                                                                                              
    tf_app = tf.compat.v1.app                                                                                                           
    tf_io  = tf.io                                                                                                          
    
    # gfile
    tf_gfile = tf_io.gfile 
else:                                                                                                                     
    tf_app = tf.app                                                                                                                            
    tf_io  = tf.python_io
    
    # gfile
    tf_gfile = tf.gfile 


def print_docs(): 
    '''
    * Installation 
    cd tf1_tf2_compatibility_functions
    # Python3
    python3 -m pip install .
    
    # Python2 
    python2 -m pip install .

    * Usage
    from tf1_tf2_compat_functions import * 
    
    >> Instead of calling, tf.app.run() in TF1 or tf.compat.v1.app.run() in TF2, 
    call tf_app.run()

    >> Instead of calling, tf.io.TFRecordWriter() in TF2, or tf.python_io.TFRecordWriter() in TF2, 
    call tf_io.TFRecordWriter()
    '''

if __name__=="__main__":
    # Usage 
    print_docs.__doc__ 
