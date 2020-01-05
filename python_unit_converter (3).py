# -*- coding: utf-8 -*-
"""python_unit_converter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hy7iIWcBhu8M7-vmI97Tu2f62f-H92Yh

this is for my google code in python uni
"""

# type two of python code 
print('welcome to my unit converter program')
print('quick note ')
print("please type your units in short ")


#recieving input from the user
inp=input("please enter your value ")
splitval=inp.split(",")

value=int(splitval[0])
value_unit=splitval[1]
converted=splitval[2]


#unit recognization
distance=['m','cm','km','mm']
time=['hrs','min','s']
volume=['kl','ml','l']




# the distance converting function

def distance_converter():
  distance_base=value
  if value_unit=='km':
    distance_base=value*1000
    

  elif value_unit=='cm':
    distance_base=value/100

  elif value_unit=='mm':
    disttance_base=value/1000

  else:
    distance_base=value

  # the conversion part

  converted_value=0
  if converted=='cm':
    converted_value=distance_base*100

  elif converted=='km':
    converted_value=distance_base/1000

  elif converted=='mm':
    converted_value=distance_base*1000

  else:
    converted_value=disttance_base

  return converted_value



# the time converting function 
def time_converter():
  time_base=value
  if value_unit=='hrs':
    time_base=value*60

  elif value_unit=='min':
    time_base=value

  else:
    time_base=value/60

  time_converted=time_base

  if converted=='hrs':
    time_converted=time_base/60

  elif converted=='min':
    time_converted=time_base

  else:
    time_converted=time_base*60

  return time_converted


#the volume converting function

def volume_converter():
  volume_base=value
  if value_unit=='kl':
    volume_base=value*1000

  elif volume_unit=='l':
    volume_base=value

  else:
    volume_base=value/1000

  volume_converted=volume_base

  if converted=='ml':
    volume_converted=volume_base*1000

  elif converted=='l':
    volume_converted=volume_base

  else:
    volume_converted=volume_base/1000

  return volume_converted



#checking if unites are of the same type
if value_unit in distance and converted in distance:
  print("processing")
  print(distance_converter())
  

elif value_unit in time and converted in time:
  print("the problem is time type")
  print(time_converter())

elif value_unit in volume and converted in volume:
  print("the problem is volime type")
  print(volume_converter())

else:
  print("type not found... please try again")

