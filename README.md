# DNA Storage_DBTRG
DNA Storage_DBTRG includes encoding, data recovery, and error-correcting algorithms. The encoding and data recovery algorithms and their results can be obtained through DBG_v1.py, while error correction and data recovery rate can be obtained through RS_correction.py in ReedSolomon-master.
  
## DBTRG
In DBTRG, huffcoder and huffdecoder respectively implement the encoding and decoding of the Rotation Tree algorithm. DBG_v1 implements the invocation of dynamic binary sequence in fake_random, the use of De Bruijn Trim graph, and integrates the Rotation Tree algorithm.

## RS codes
### Generalized Reed Solomon Code  
As RS has not been explained in detail in the paper, it will be explained in detail here.You can simply run RS_correction to perform error correction and obtain the data recovery rate.This special code can be sped up by a factor of p, since the code can be parallelized over p components. Additionally it allows to construct codes of arbitrary length as long as n%p == 0 is fulfilled and a primitive root of unity p can be found in the corresponding field over which the code is constructed. Whereas the standard Reed Solomon code imposes n= q^m -1. The code can be constructed over all Galois Fields.  
  
### Documentation  
n = k + r <br/>  
k = message symbols sent <br/>  
r = number of parity symbols <br/>  
p = speed up factor <br/>  
  
Currently the code can also handle codes where n %p != 0 however only if r is still divisble by p.  
#### Class Generalized_Reed_Solomon  
```  
class Generalized_Reed_Solomon(  
field_size:int, #q characterisitc of the field  
message_length:int, # n  
payload_length:int, # k  
symbol_size:int, #m exponent of field. Order of field is q^m  
p_factor:int, #p speedup factor  
irr_poly=None:array, # optional in case that the galois libary has not a precomputed irreducible polynominal  
multi_processing = False, #optional when True certain parts of the code will be parallelized this is however currently only efficent when operating with long messages  
debug=False # can be set to true in order to have the steps printed to the console  
)  
```  
#### Generalized_Reed_Solomon.encode()  
```  
Generalized_Reed_Solomon.encode(self,array)  
# Takes as an argument a list and appends parity symbols to it  
```  
#### Generalized_Reed_Solomon.decode()  
```  
Generalized_Reed_Solomon.decode(self, recieved_msg)  
# Takes as an argument a list of a encoded message. Detects and corrects errors and then returns the k info symbols  
```  
#### Generalized_Reed_Solomon.convert_to_symbol_array()  
```  
Generalized_Reed_Solomon.convert_to_symbol_array(self,array)  
# Takes as an argument a list values and converts them to galois elements. If the degree of field > 1, the list will be a list of list  
# where each list represents the coefficents of a Galois element of the corresponding Field  
```  
  
#### Generalized_Reed_Solomon.symbol_array_to_array()  
```  
Generalized_Reed_Solomon.symbol_array_to_array(self,array)  
# Takes a list of ints as an argument. Performs the reverse of convert_to_symbol_array(). Transforms each Galois field element in the list  
# into its coefficent representation.  
```  