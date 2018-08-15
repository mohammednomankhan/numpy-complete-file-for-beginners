
# coding: utf-8

# In[1]:


import numpy as np 
import numpy.matlib


# In[2]:


array = np.array([1,2,3]) #single dimension array
print(array)


# In[3]:


array = np.array([[12,33,44],[55,66,77]]) #multidimensional array

print("\n complete array with all values : \n\n",array)

print("\n value at first row first column : ",array[1][1],)

print("\n array dimension : ",array.shape)

print("\n total number of elements in array : ",array.size)


# In[4]:


array = np.array([[4,6,8],[55,66,99]] , dtype=float ) #data type of multidimensional array object

print("\n all values in array : \n\n",array)

print("\n dimension of array : ",array.ndim) #return the dimension of array

print("\n dimension of array in row*column form : ",array.shape) #also return the dimension of array


# In[5]:


# 3 dimensional array and rollaxis function and swapaxes function

array = np.arange(24).reshape(2,3,4) #this is a 3-dimensional array with 2 rows , 3 columns and 4 depth

print("\n values in 3-dimensional array : \n",array)

print("\n value at row 0 , column 2 and depth 1 : ",array[0,2,1])

print("\n values in array after rollaxis row wise : \n\n",np.rollaxis(array,0))

print("\n shape after rollaxis row wise : ",np.rollaxis(array,0).shape)

print("\n values in array after rollaxis column wise : \n\n",np.rollaxis(array,1))

print("\n shape after rollaxis column wise : ",np.rollaxis(array,1).shape)

print("\n values in array after rollaxis depth wise : \n\n",np.rollaxis(array,2))

print("\n shape after rollaxis depth wise : ",np.rollaxis(array,2).shape)

print("\n original shape of array is not changed : ",array.shape)

print("\n values after swapaxis 2 and 0 : \n\n",np.swapaxes(array,2,0))

print("\n values after swapaxis 1 and 2 : \n\n",np.swapaxes(array,1,2))

print("\n values after swapaxis 1 and 0 : \n\n",np.swapaxes(array,1,0))


# In[6]:


dt = np.dtype(np.int32)

newarray = np.array([1,8,44],dtype=dt)

print(newarray)

dt = np.dtype([('age',np.int32)])

newarray = np.array([1,8,44],dtype=dt)

print(newarray['age'])


# In[7]:


myarray = np.array([[5,6,7],[8,9,10]]) #this is a multidimensional array

print("array before resizing : \n\n",myarray)

print("\n dimensions of array in row*column form : ",myarray.shape) #returns the dimension of array in row*column form

print("\n dimension of array : ",myarray.ndim) # only returns the dimension of array

myarray.shape=3,2 #array is resized into 3 rows and two columns

print("\n array after resizing into 3 rows and 2 columns form : \n\n",myarray)

myarray.shape=6,1 #shape function can also be used again to resize array

print("\n array after resizing again into 6 rows and 1 columns form : \n\n",myarray)

myarray = np.array([2,3,4,5,6,7]) #this is a single dimension array

print("\n values in single dimensional array : ",myarray)

myarray = myarray.reshape(2,3)  #reshape function is used to change one dimensional array into 2 dimensional array

print("\n now single dimensional array has changed into 2 dimensional array (2 rows , 3 columns form) : \n\n",myarray)


# In[8]:


myarray = np.arange(11) # arange function can create array with evenly spaced numbers 
print("\n values from 1 to 10 in array : \n\n",myarray)

myarray = np.arange(1,11,2) # arange function takes starting range as 1 and ending range as 11 and space is 2
print("\n values from 1 to 10 with space of 2 : ",myarray)

myarray = np.arange(10,0,-2) # arange function can also be used to insert values in reverse order in array

print("\n values from 10 to 1 in array : ",myarray)

print("\n length of each element of array in bytes : ",myarray.itemsize)

print("\n",myarray.flags)


# In[9]:


myarray = np.empty([4,2],dtype=int) #new array is created with some random values 
print(myarray)


# In[10]:


myarray = np.zeros([6,3],dtype=int) #new array is created and 0 is assigned at each location
print(myarray)

myarray = np.zeros(4) #it can also create single dimension array
print("\n\n",myarray)

myarray = np.ones([5,2]) #also create array by assigning 1 in each element
print("\n\n",myarray)


# In[11]:


listx = [13,24,55,67]

array = np.asarray(listx , dtype=int) #array can be created by using list

print("\n values in single dimensional array : ",array)

print("\n values at 4th location (index number 3) in single dimensional array : ",array[3]) 

listy = [[45,46,78],[23,21,99]] #multidimensional array can be created by using list of lists

array = np.asarray(listy)

print("\n values in multidimensional array : \n\n",array)

print("\n value at second row first columns in multidimensional array : ",array[1][0]) 


tuplex = (89,45,55) #array can be created by using tuple

array = np.asarray(tuplex)

print("\n values in single dimensional array : ",array)

tupley = ((12,23),(44,46),(98,92)) #multidimensional array can be created by using tuple of tuples

array = np.asarray(tupley)

print("\n values in multi dimensional array :\n\n",array)

listz = ["noman","khan"] #creating array by using string as list elements

array = np.asarray(listz)

print("\n values in array : ",array)


# In[12]:


array = np.arange(11) 

print("values in array : ",array)

subarray = slice(2,9,2) #this function is used to slice array , 2 is starting range , 9 is ending range , and 2 is space

print("\nvalues in array after slicing : ",array[subarray])

array = np.arange(21)

arraytwo = array[5:16:3] #this will also used to slice array , 5 is starting range , 16 is ending range , and 3 is space

print("\nvalues in array with space of 3 numbers : ",arraytwo)


# In[13]:


arrayone = np.arange(20) #this is a single dimensional array

print("values in array from 1 to 5 : ",arrayone[1:6])

print("\nvalues in array from 11 : ",arrayone[11:])

print("\nvalues in array from start to 9 : ",arrayone[:10])


arraytwo = np.array([[12,43],[56,78],[98,42],[19,20]]) #this is a multidimensional array

print("\nvalues in multidimensional array : \n\n",arraytwo)

print("\nvalues in multidimensional array after first row : \n\n",arraytwo[1:])

print("\nvalues in multidimensional array from second row to third row : \n\n",arraytwo[1:3])

print("\nvalues in multidimensional array from first row to third row : \n\n",arraytwo[:3])


                                #USE OF ellipsis (…)
    
print("\nvalues in second column of multidimensional array : ",arraytwo[...,1])

print("\nvalues in first column of multidimensional array : ",arraytwo[...,0])

print("\nvalues in first row of multidimensional array : ",arraytwo[0,...])

print("\nvalues in third row of multidimensional array : ",arraytwo[2,...])

print("\nvalues in multidimensional array after first row : \n\n",arraytwo[1:,...])

print("\nvalues in multidimensional array from first row to third row : \n\n",arraytwo[:3,...])

print("\nvalues in multidimensional array in second column : \n\n",arraytwo[...,1:])

print("\nvalues in multidimensional array in first column : \n\n",arraytwo[...,:1])


# In[14]:


# ADVANCE INDEXING
    
    # two types of advance indexing 1) pure integer indexing 2) boolean indexing
    
newarray = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print("\n values in multidimensional array : \n\n",newarray) # pure integer indexing
 
print("\n values which are greater then 6 in array : ",newarray[newarray>6]) #boolean indexing

print("\n all even values in array : ",newarray[newarray%2==0]) #boolean indexing

print("\n all odd values in array : ",newarray[newarray%2 != 0]) #boolean indexing

print("\n square of each even number in array : ",newarray[newarray%2==0]**2) #boolean indexing

newarray = np.array([1,2,np.nan,76,89,np.nan,89])

print("\n values in array : ",newarray)

print("\n all nan (not a number) in array : ",np.isnan(newarray)) # it will return true where element is nan (not a number)

print("\n all values excluding nan (not a number) in array : ",~np.isnan(newarray)) #it wiil return false where element is nan (not a number)


# In[15]:


arrayone = np.array([3,4,3,2,5])

arrayatwo = np.array([8,8,5,6,9])

print("\n values in arrayone : ",arrayone)

print("\n values in arraytwo : ",arrayatwo)

print("\n multiplication of coresponding elements of arrayone and arraytwo : ",arrayone*arrayatwo) #pairs are (3*8)(4*8)(3*5)(2*6)(5*9)

print("\n sum of coresponding elements of arrayone and arrayatwo : ",arrayone+arrayatwo) #pairs are (3+8)(4+8)(3+5)(2+6)(5+9)


print("\n subtraction of coresponding elements of arrayone and arrayatwo : ",arrayone-arrayatwo) #pairs are (3-8)(4-8)(3-5)(2-6)(5-9)


print("\n division of coresponding elements of arrayone and arrayatwo : ",arrayone/arrayatwo) #pairs are (3/8)(4/8)(3/5)(2/6)(5/9)


# In[16]:


#broadcasting
    
arrayone = np.array([[4,5,7],[5,2,5],[9,6,3]])

arraytwo = np.array([2,4,1])

print("\n sum of coresponding elements of array : \n",arrayone+arraytwo) # int this the pairs are (4+1)(5+4)(7+1)(5+2)(2+4)(5+1)(9+2)(6+4)(3+1)


# In[17]:


myarray = np.arange(1,51,5)
myarray = myarray.reshape(5,2)

print("\n values in array : \n\n",myarray)

print("\n")

for x in np.nditer(myarray) : # nditer is used to iterate over array
    print("values in array : ",x)

print("\n")

for x in np.nditer(myarray , order='C') : 
    print("values in C-order ",x)

print("\n")    

for x in np.nditer(myarray , order='F') :
    print("values in F-order ",x)
    
newarray = myarray.T # newarray will become transpose of myarray

print("\n values in newarray which is a transpose of myarray : \n\n",newarray)

print("\n")

for x in np.nditer(newarray): 
    print("values in newarray (by using nditer()): ",x)


# In[18]:


myarray = np.arange(1,11,2)

print("\n values in array : ",myarray)

for x in np.nditer(myarray, op_flags=['readwrite']) : # op_flags allows us to modify array elements
    x[...] = x**2 #square of each element of array

print("\n square of each value in array : ",myarray)


# In[19]:


myarray = np.arange(1,21,2)

print("\n values in array : ",myarray)

print("\n")

for x in np.nditer(myarray, flags = ['external_loop'], order = 'F') :
    print("values of array in F Order : ",x)
    
myarraytwo = np.arange(21,41,2)

print("\nvalues in myarraytwo : ",myarraytwo)

print("\n")

for x,y in np.nditer([myarray,myarraytwo]) : #it is possible to itrate multiple arrays in one loop
    print("\nelement of myarray : ",x)
    print("nelement of myarraytwo : ",y)


# In[20]:


array = np.arange(9)
array = array.reshape(3,3)

print("values in array : \n\n",array)

newarray = np.arange(11,20).reshape(3,3)

print("\n values in newarray : \n\n",newarray)

print("\n addition of array and newarray : \n\n",np.add(array,newarray))

print("\n multiplication of array and newarray : \n\n",np.multiply(array,newarray))

print("\n division of array and newarray : \n\n",np.divide(array,newarray))

print("\n subtraction of array and newarray : \n\n",np.subtract(array,newarray))


# In[21]:


array = np.array([[23,14,20,6],[5,12,2,11],[90,45,21,32]]) #multidimensional array

print("values in array : \n\n",array)

print("\n value at index number 6 (in the context of 1-dimensional array) : ",array.flat[6]) #1-D iterator over the array

print("\n dimension of array : ",array.shape)

print("\n copy of multidimensional array into 1-dimensional array : ",array.flatten()) #This function returns a copy of an array collapsed into one dimension

print("\n dimension of array is still same (it doesn't changed) : ",array.shape)

print("\n copy of multidimensional array into 1-dimensional array in F-Order : ",array.flatten(order='F'))

print("\n values in array by calling transpose function : \n\n",np.transpose(array)) #this will return transposed array in (4,3) shape
                                                                                 #but it will not change the actual dimension

print("\n dimension of array is still same (it doesn't changed) : ",array.shape)

print("\n values in array by calling transpose function : \n\n",array.T) #this willalso return transposed array in (4,3) shape
                                                                                 #but it will also not change the actual dimension

print("\n dimension of array is still same (it doesn't changed) : ",array.shape)



# In[22]:


#expand_dims function

array = np.array([[65,34,21],[76,89,49],[99,95,79],[12,19,16]])
                   
print("\n values in array : \n",array)
print("\n shape of array : ",array.shape)

newarray = np.expand_dims(array,axis=0)

print("\n newarray after expanding dimension at axis = 0 :\n",newarray)

print("\n shape of newarray : ",newarray.shape)

arraythree = np.expand_dims(array,axis=1)

print("\n arraythree after expanding dimension at axis = 1 : \n",arraythree)

print("\n shape of arraythree  : ",arraythree.shape)


arrayfour = np.expand_dims(array,axis=2)

print("\n arrayfour after expanding dimension at axis = 2 : \n",arrayfour)

print("\n shape of arrayfour : ",arrayfour.shape)


# In[23]:


array = np.arange(12).reshape(1,4,3) #3D array

print("\n values in array : \n",array)
print("\n shape of array : ",array.shape)

print("\n",np.squeeze(array))  #This function removes one-dimensional entry from the shape of the given array.

print("\n shape of array : ",np.squeeze(array).shape)


# In[24]:


# array concatenate

first = np.array([[12,15],[34,26],[76,39]])

second = np.array([[2,4],[4,6],[8,5]])

print("\n values in first array : \n",first)

print("\n shape of first array : ",first.shape)

print("\n values in second array : \n",second)

print("\n shape of second array : \n",second.shape)

print("\n concatenate first and second array along axis = 0 :\n ",np.concatenate((first,second))) #axis is bydefault = 0

print("\n shape of array after concatenate along axis = 0 : ",np.concatenate((first,second)).shape)

print("\n concatenate first and second array along axis = 1 : \n",np.concatenate((first,second),axis=1))
  
print("\n shape of array after concatenate along axis = 1 : ",np.concatenate((first,second),axis=1).shape)    
                                           
#stack

print("\n joining array along axis = 1 : \n",np.stack((first,second),axis=1))

print("\n shape of array after joining along axis = 1 : ",np.stack((first,second),axis=1).shape)

print("\n joining array along axis = 0 : \n",np.stack((first,second),axis=0))

print("\n shape of array after joining along axis = 0 : ",np.stack((first,second),axis=0).shape)

#hstack and vstack

print("\n joining array horizontally : \n",np.hstack((first,second)))

print("\n shape of array after joining horizontally : ",np.hstack((first,second)).shape)

print("\n joining array vertically : \n",np.vstack((first,second)))

print("\n shape of array after joining vertically : ",np.vstack((first,second)).shape)


# In[25]:


# array split
    
array = np.arange(12) # 1D array

print("\n values in array : \n",array)

subarray = np.split((array),4)

print("\n array is splitted into 4 parts : ",subarray)

subarray = np.split((array),6)

print("\n array is splitted into 6 parts : ",subarray)


array = np.arange(12).reshape(4,3) #2D array

print("\n values in 2D array : \n",array)

subarray = np.split((array),2)

print("\n 2D array is splited in 2 parts : \n",subarray)

print("\n values in first part of array which has previously divided in two parts : \n",subarray[0])

print("\n values in second part of array which has previously divided in two parts : \n",subarray[1])

subarray = np.split((array),4)

print("\n 2D array is splited in 4 parts : \n",subarray)

#hsplit 

array = np.arange(16).reshape(4,4) 

print("\n values in new 2D array : \n",array)

subarray = np.hsplit(array,2)

print("\n 2D array is splited into 2 parts horizontally : \n",subarray)

print("\n first part of horizontally splitted array : \n",subarray[0])

print("\n second part of horizontally splitted array : \n",subarray[1])

#vsplit
    
subarray = np.vsplit(array,2)

print("\n 2D array is splitted into 2 parts verically : \n",subarray)

#splitting 3D array
array = np.arange(24).reshape(2,3,4)

print("\n values in 3D array : \n",array)

subarray = np.split(array,2)

print("\n 3D array is splited into 2 parts : \n\n this is the first part : \n\n"
      ,subarray[0],"\n\nthis is the second part : \n\n",subarray[1])


# In[26]:


# array resizing

array = np.arange(6).reshape(2,3)

print("\n values in array : \n",array)

print("\n shape of array : ",array.shape)

newarray = np.resize(array,(3,2))

print("\n values in array after resizing into (3,2) : \n",newarray)

print("\n shape of resized array : ",newarray.shape)

newarray = np.resize(array,(4,3)) #If the new size is greater than the original,
                                    #the repeated copies of entries in the original are contained

print("\n newarray is resized into (4,3) : \n",newarray)

print("\n shape of resized array : ",newarray.shape)


# In[27]:


# array append
array = np.arange(6).reshape(3,2)

print("\n values in array : \n",array)

newarray = np.append(array,[7,8])

print("\n values in array after appending it with new values : \n",newarray)

newarray = np.append(array,[[7,8]],axis=0)

print("\n values in array after appending it along axis = 0 : \n",newarray)

newarray = np.append(array,[[7,8],[9,10],[11,12]],axis=1) #because there are 3 rows and 2 columns in original array
                  #that's why you need to append 3 rows with 2 columns
                  #to append along axis = 1 ohterwise error will come

print("\n values in array after appending it along axis = 1 : \n",newarray)

# array insert 
print("\n values in array : ",array)

newarray = np.insert(array,4,[17])

print("\n values in array after inserting 17 at index number 4 in array : \n",newarray)

newarray = np.insert(array,2,[11,12],axis=0)

print("\n values in array after inserting 11 and 12 at index = 2 along axis = 0 : \n",newarray)

newarray = np.insert(array,1,[11,12,13],axis=1)

print("\n values in array after inserting 11 , 12 , 13 at index = 1 along axis = 1 : \n ",newarray)


# In[28]:


# delete from array
    
array = np.arange(12).reshape(4,3)

print("\n values in array : \n\n",array)

print("\n values in array after deleting value '4' : \n\n",np.delete(array,4))   #Array flattened before delete operation
                                      #as axis not used 

print("\n values in array after deleting column 1 ( where column begins with 0) : \n\n",np.delete(array,1,axis=1)) 

print("\n\n values in array after deleting row 1 ( where row begins with 0) : \n\n",np.delete(array,1,axis=0))


     # delete from 3D array
    
array = np.arange(36).reshape(3,4,3)

print("\n values in 3D array : \n\n",array)

print("\n values in array after deleting along axis = 0 : \n\n",np.delete(array,1,axis = 0)) # row number 0 is deleted

print("\n values in array after deleting along axis = 1 :\n\n",np.delete(array,2,axis= 1)) #column number 2 is deleted form each row

print("\n values in array after deleting along axis = 2 : \n\n",np.delete(array,1,axis = 2)) #values at depth = 2 is deleted from each row

 # unique in array
    
array = np.array([2,3,2,5,4,5,6,4])

print("\n values in array : \n\n",array)

print("\n unique values in array : \n\n",array)


# In[29]:


# String functions
strone = " hello"
strtwo = " how are you ?"
strthree = " world"
strfour = " I am fine" 
                                           #np.char.add()

print("\n string 1 = ",strone,"\n string 2 = ",strtwo,"\n string 3 = ",strthree,"\n string 4 = ",strfour)

print("\n concatenation of string 1 and string 2 : ",np.char.add(strone,strtwo))

print("\n concatenation of string 1 with string 3 and string 2 with string 4 : ",np.char.add([strone,strtwo],[strthree,strfour]))


#np.char.multiply()

print("\n concatenation of strone to 5 times : ",np.char.multiply(strone,5)) #this will print 'hello' 5 times


#np.char.center()

print("\n demonstartion of center() function : ",np.char.center("DataScience",25,fillchar="*"))
print("\n demonstartion of center() function : ",np.char.center("DataScience",25,fillchar="!"))
print("\n demonstartion of center() function : ",np.char.center("DataScience",25,fillchar="0"))
print("\n demonstartion of center() function : ",np.char.center("DataScience",25,fillchar="@"))
print("\n demonstartion of center() function : ",np.char.center("DataScience",25,fillchar="$"))

#np.char.capitalize()

print("\n first letter of string is capitalized : ",np.char.capitalize("numpy"))


#np.char.title()
        
print("\n strtwo in title case : ",np.char.title(strtwo))

#np.char.lower()

print("\n string in lower case : ",np.char.lower("MY NAME IS KHAN AND I AM A PROGRAMMER"))

print("\n string in upper case : ",np.char.upper("my name is khan and i am a programmer"))

#np.char.split()
    
print("\n demonstration of split function : ",np.char.split("my name is khan and i am a programmer")) 
                                    #By default,a whitespace is used as a separator

print("\n string is seprated by comma : ",np.char.split("my name is khan,and i am a programmer",sep=','))

#np.char.splitlines()

print("\n demonstration of splitlines() function  : ",np.char.splitlines("My name is khan and \n I am a programmer")) 
                                   
                                            #\n is used as line boundry
        
#np.char.strip()

print("\n strip 'p' from string : ",np.char.strip('python programming loop','p')) #it strip only first and last letter

print("\n strip 'p' from string : ",np.char.strip(["pythonp","programmingp","loop"],'p')) 

#np.char.join()
    
print ("\n string 'DMY' is joined with ':' as a separator ",np.char.join(':','DMY')) 

print ("\n string 'DMY' is joined with separator ':' and string 'YMD' is joined with '-' ",np.char.join([':','-'],['DMY','YMD']))

#np.char.replace()
    
string = "java is a programming language"

print("\n string = ",string)

print("\n 'java' is replaced with 'python' in the string : ",np.char.replace(string,'java','python'))


# In[30]:


#statistical functions

                                    #amin() and amax()

array = np.array([[89,67,23],[75,99,89],[26,145,12],[160,65,39]])

print("\n values in 2D array : \n",array)

print("\n minimum value in 2D array : ",np.amin(array))

print("\n maximum value in 2D array : ",np.amax(array))

print("\n minimum value in 2D array along axis = 0 : ",np.amin(array,axis = 0)) 

print("\n minimum values in 2D array along axis = 1 : ",np.amin(array,axis = 1))

print("\n maximum values in 2D array along axis = 0 : ",np.amax(array,axis = 0))

print("\n maximum values in 2D array along axis = 1 : ",np.amax(array,axis = 1))

newarray = np.array([[[78,98,23,45],[156,111,789,456],[467,90,234,73]],[[990,680,340,560],[700,750,1000,922],[674,23,32,11]]])
                  
print("\n values in 3D array : \n\n",newarray)

print("\n minimum value in 3D array : ",np.amin(newarray))

print("\n maximum value in 3D array : ",np.amax(newarray))

print("\n minimum values in 3D array along axis = 1 : \n",np.amin(newarray,axis = 1))

print("\n maximum values in 3D array along axis = 1 : \n",np.amax(newarray,axis = 1))

print("\n minimum values in 3D array along axis = 2 : \n",np.amin(newarray,axis = 2))

print("\n maximum values in 3D array along axis = 2 : \n",np.amax(newarray,axis = 2))


    #ptp()

print("\n range (maximum-minimum) in 2D array : ",np.ptp(array))

print("\n range (maximum-minimum) in 3D array : ",np.ptp(newarray))

print("\n range (maximum-minimum) in 2D array along axis = 0 : ",np.ptp(array,axis=0))

print("\n range (maximum-minimum) in 2D array along axis = 1 : ",np.ptp(array,axis=1))

print("\n range (maximum-minimum) in 3D array along axis = 0 : \n",np.ptp(newarray,axis=0))

print("\n range (maximum-minimum) in 3D array along axis = 1 : \n",np.ptp(newarray,axis=1))

print("\n range (maximum-minimum) in 3D array along axis = 2 : \n",np.ptp(newarray,axis=2))

#median()

array = np.arange(5)

print("\n values in array : ",array)

print("\n median of array : ",np.median(array))

array = np.arange(6)

print("\n values in array : ",array)

print("\n median in array : ",np.median(array))
    
    
    #mean()


print("\n values in 1D array : ",array)        
print("\n mean in 1D array : ",np.mean(array))

array = np.arange(12).reshape(3,4)

print("\n values in 2D array : \n",array)

print("\n mean in 2D array : ",np.mean(array))

print("\n mean in 2D array along axis = 0 : ",np.mean(array,axis=0))

print("\n mean in 2D array along axis = 1 : ",np.mean(array,axis=1))

    
    #average()
        
print("\n average of 2D array : ",np.average(array)) # average = sum of all elements of array/ total number of elements
    
    #standard deviation()

print("\n standard deviation in 2D array : ",np.std(array))

    #variance()
    
print("\n variation in 2D array : ",np.var(array))
    


# In[31]:


#Sort()

array = np.array([65,76,333,56,76,47,43])   

print("\n values in 1D array : ",array)

print("\n values of 1D array in sorted order : ",np.sort(array))
    
arraytwo = np.array([[188,31,87],[999,62,16],[98,76,57]]) 

print("\n values in 2D array : \n",arraytwo)

print("\n values of 2D array in sorted order : \n",np.sort(arraytwo))

arraythree = np.array([[[65,76],[87,32]],[[53,76],[87,47]],[[98,700],[32,54]]])

print("\n values in 3D array : \n",arraythree)

print("\n values of 3D array in sorted order : \n",np.sort(arraythree))

print("\n values of 2D array in sorted order along axis = 0 : \n",np.sort(arraytwo,axis=0))

print("\n values of 2D array in sorted order along axis = 1 : \n",np.sort(arraytwo,axis=1))

print("\n values of 3D array in sorted order along axis = 0 : \n",np.sort(arraythree,axis=0))

print("\n values of 3D array in sorted order along axis = 1 : \n",np.sort(arraythree,axis=1))

print("\n values of 3D array in sorted order along axis = 2 : \n",np.sort(arraythree,axis=2))

                                        # argsort()

indexsorted = np.argsort(array) #this will return the index numbers of sorted elements

print("\n index number of sorted elements in 1D array after sorting using argsort : \n",indexsorted)

array_new = array[indexsorted] # this will create a new array with sorted values by using the sorted index number

print("\n values in new array : \n",array_new)


                                        #argmin()
    
print("\n index numbers of minumum value of 2D array : ",np.argmin(arraytwo))

print("\n index numbers of minimum values along axis = 0 in 2D array : ",np.argmin(arraytwo,axis=0))

print("\n index numbers of minimum values along axis = 1 in 2D array : ",np.argmin(arraytwo,axis=1))


                                        #argmax()
    
print("\n index numbers of maximum value of 2D array : ",np.argmax(arraytwo))

print("\n index numbers of maximum values along axis = 0 in 2D array : ",np.argmax(arraytwo,axis=0))

print("\n index numbers of maximum values along axis = 1 in 2D array : ",np.argmax(arraytwo,axis=1))
 
    
                                        #extract

print("\n all the values which are greater then 75 in 2D array : ",np.extract(arraytwo>75,arraytwo))

print("\n all the even values in 2D array : ",np.extract((arraytwo%2==0),arraytwo))

print("\n all the even values in 2D array : ",np.extract((arraytwo%2 !=0),arraytwo))


# In[32]:


#No Copy (change in one array reflacts to another also if their id's are same)

array_one = np.arange(6).reshape(2,3)

print("\n values in array_one : \n",array_one)

print("\n id of array_one : ",id(array_one))

array_two = array_one

print("\n values in array two : \n",array_two)

print("\n id of array 2 : ",id(array_two))

if(id(array_one)==id(array_two)):
    print("\n id of array_one and id of array_two is simmilar..")
else :
    print("\n id of array_one and array_two is diffrent..")
    
array_two.shape = 6,1

print("\n shape of array_two has changed : \n",array_two)

print("\n shape of array_one has also changed automatically : \n",array_one) #that's because the id of both arrays are same
                          #and when we changed the shpae of array_two 
                          #shape of array_two also changed automatically
array_one[0][0] = 1990

print("\n value at 0 location has changed to 1990 in array_one : \n",array_one)

print("\n value at 0 location has also changed automatically to 1990 in array_two : \n",array_two)

                            #view (change in one array will not reflacts to another becaues their id's are not same)

first_array = np.arange(8).reshape(2,4)

print("\n values in first_array : \n",first_array)

print("\n id of first_array : ",id(first_array))

second_array = first_array.view() #view of first_array is assigned into second_array

print("\n value in second_array : \n",second_array)

print("\n id of second_array : ",id(second_array))

if(id(first_array)==id(second_array)) :
    print("\n id's of first_array and second_array are same..")
else :
    print("\n id's of first_array and second_array are not same..")  #because view of first_array has assigned into second_array
    
second_array.shape= 4,2

print("\n shape of second_array has changed : \n",second_array)

print("\n but shape of first_array has not changed : \n",first_array)


                             #copy(change in one array will not reflacts to another becaues their id's are not same)

third_array = np.arange(15).reshape(5,3)

print("\n values in third_array : \n",third_array)

print("\n id of third_array : ",id(third_array))

fourth_array = third_array.copy() #view of first_array is assigned into second_array

print("\n value in fourth_array : \n",fourth_array)

print("\n id of fourth_array : ",id(fourth_array))

if(id(third_array)==id(fourth_array)) :
    print("\n id's of third_array and fourth_array are same..")
else :
    print("\n id's of third_array and fourth_array are not same..")  #because view of first_array has assigned into second_array
    
third_array = third_array.reshape(3,5)

print("\n shape of third_array has changed : \n",third_array)

print("\n but shape of fourth_array has not changed : \n",fourth_array)
  
                            


# In[33]:


#matrix library

matrix = np.matrix([[45,47],[23,43],[78,90]])
    
print("\n matrix : \n",matrix)   

array = np.asarray(matrix)

print("\n now matrix has changed into array : \n",array)

matrix = np.asmatrix(array)

print("\n array has changed back into matrix : \n",matrix)


    
                                #matlib.zeros()
                        
matix = np.matlib.zeros((4,3)) 

print("\n matrix has created with 0 as values : \n",matix)

                                #matlib.ones()
                        
matrix = np.matlib.ones((2,5))

print("\n matrix has formed with 1 as values : \n",matrix)

                                #matlib.empty

matrix = np.matlib.empty((3,5), dtype=int)

print("\n an empty matrix has created : \n",matrix)


                                #matlib.eye() returns a matrix with 1 along the diagonal elements and the zeros elsewhere.

matrix = np.matlib.eye(n=3 , M = 4 , k = 0 , dtype = int) # n = number of row , M = number of columns , k = Index of diagonal

print("\n diagonal matrix with 1 as diagonal has created : \n",matrix)


                    #matlib.identity() returns the Identity matrix which is a square matrix with all diagonal elements as 1.  
    
matrix = np.matlib.identity(6,dtype=int) #in square matrix number of columns and number of rows remains same

print("\n identity matrix with 1 as diagonal elment has created : \n",matrix)

                    
                   #matlib.rand() #create a matrix of specified size with random values
        
matrix = np.matlib.rand(3,2)

print("\n matrix with some random values has created : \n",matrix)


# In[36]:


#saving and loading numpy array in binary file 

array = np.arange(6).reshape(2,3)

print("\n values in array which will be saved in binary file and text file both: \n",array)

np.save('savedarray',array) #this will save array in binary file

new_array = np.load('savedarray.npy') # array's data, shape, dtype  is stored in savedarray.npy file which is a binary file

print("\n array which is retrieved from binary file and stored in new_array : \n",new_array)

#saving and loading numpy array in text file


np.savetxt('saveintextfile.txt',array)  #this will save array in text file

array_three = np.loadtxt('saveintextfile.txt')

print("\n array which is retrieved from text file and stored in array_three : \n",array_three)


# In[35]:


#Linear Algebra
                                    
                                    #dot product [dot()]
                                    
array_one = np.arange(4).reshape(2,2)
array_two = np.arange(5,11).reshape(2,3)

print("\n values in array_one : \n",array_one)

print("\n values in array_two : \n",array_two)
    
print("\n dot product of array_one and array_two : \n",np.dot(array_one,array_two)) #pairs in dot product are (0*5 + 1*8 = 8)
                
#pairs in dot product are (0*5 + 1*8 = 8) (0*6 + 1*9 = 9) (0*7 + 1*10 = 10)
                        # (2*5 + 3*8 = 34) (2*6 + 3*9 = 39) (2*7 + 3*10 = 44)
                                    
                                    #dot product of two vectors [vdot()]
                                    
array_one = np.arange(6).reshape(2,3)
array_two = np.arange(7,13).reshape(2,3)

print("\n values in array_one : \n",array_one)

print("\n values in array_two : \n",array_two)

print("\n dot product of two vectors : ",np.vdot(array_one,array_two))  # (0*7 + 1*8 + 2*9 + 3*10 + 4*11 + 5*12 = 160)
                                    
                                    #inner product [inner()]
                                
print("\n inner product : \n",np.inner(array_one,array_two)) #(0*7 + 1*8 + 2*9 = 26) (0*10 + 1*11 + 2*12 = 35)
                 #(3*7 * 4*8 + 5*9 = 98) (3*10 + 4*11 + 5*12 = 134)

    
                                    #matrix multiplication of two arrays [(matmul())] 
        
array_two = np.arange(10,19).reshape(3,3)

print("\n values in array_one : \n",array_one)

print("\n values in array_two : \n",array_two)

print("\n matrix multiplication of two arrays array_one and array_two : \n",np.matmul(array_one,array_two))

               #(0*10 + 1*13 + 2*16 = 45   0*11 + 1*14 + 2*17 = 48   0*12 + 1*15 + 2*18 = 51)
               #(3*10 + 4*13 + 5*16 = 162  3*11 + 4*14 + 5*17 = 178  3*12 + 4*15 + 5*18 = 186)
               #(6*10 + 7*13 + 8*16 = 279  6*11 + 7*14 + 8*17 = 300  6*12 + 7*15 + 8*18 = 321)
            

                                    #Determinant

array_one = np.arange(4).reshape(2,2)                
                
print("\n values in array_one : \n",array_one)
    
print("\n determinant of array_one : ",np.linalg.det(array_one)) #determinant = (0*3 - 1*2 = -2)
 

