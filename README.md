# DNA Storage_DBTRG
DNA Storage_DBTRG includes encoding, data recovery, and error-correcting algorithms. The encoding and data recovery algorithms and their results can be obtained through DBG_v1.py, while error correction and data recovery rate can be obtained through RS_correction.py in ReedSolomon-master.
  
## DBTRG
In DBTRG, huffcoder and huffdecoder respectively implement the encoding and decoding of the Rotation Tree algorithm. DBG_v1 implements the invocation of dynamic binary sequence in fake_random, the use of De Bruijn Trim graph, and integrates the Rotation Tree algorithm.

## RS codes
### Generalized Reed Solomon Code  
As RS has not been explained in detail in the paper, it will be explained in detail here.You can simply run RS_correction to perform error correction and obtain the data recovery rate.
