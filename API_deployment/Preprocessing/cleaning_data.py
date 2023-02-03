import json


def check_area(data: dict):
  """ 
  This function takes a dictionnary as input representing the data of the users
  It stop the programm if there is an error with the field Living_Area, else do nothing
  In data, Living_Area has to be a int in squared meter
  """
  try:
    if not isinstance(data['Living_Area'], int):
      raise ValueError('Error: Living_Area has the wrong type, int required')
    if data['Living_Area'] < 0:
      raise ValueError('Error: Living_Area must be a positive integer')
  except KeyError:
    raise KeyError('Error: Living_Area field is missing')

def check_property_type(data: dict) -> dict:
  """ 
  This function takes a dictionnary as input representing the data of the users
  It stop the programm if there is an error in the field Type_of_property, else do nothing
  In data, Type_of_property has to be a str: HOUSE or APARTMENT
  """
  try:
    if not isinstance(data['Type_of_property'], str):
      raise ValueError('Error: Type_of_property has the wrong type, str required')
    if data['Type_of_property'] != 'HOUSE' and data['Type_of_property'] != 'APARTMENT':
      raise ValueError('Error: Type_of_property must be HOUSE or APARTMENT')
  except KeyError:
    raise KeyError('Error: Type_of_property field is missing')

  if data['Type_of_property'] == "HOUSE":
    data['Type_of_property'] = 2
  else:
    data['Type_of_property'] = 1
  
  return data


def check_rooms_number(data: dict):
  """ 
  This function takes a dictionnary as input representing the data of the users
  It stop the programm if there is an error with the field Number_of_rooms, else do nothing
  In data, Number_of_rooms has to be a int > 0
  """
  try:
    if not isinstance(data['Number_of_rooms'], int):
      raise ValueError('Error: Number_of_rooms has the wrong type, int required')
    if data['Number_of_rooms'] < 0:
      raise ValueError('Error: Number_of_rooms must be a positive integer')
  except KeyError:
    raise KeyError('Error: Number_of_rooms field is missing')

def check_zip_code(data: dict):
  """ 
  This function takes a dictionnary as input representing the data of the users
  It stop the programm if there is an error with the field Locality, else do nothing
  In data, Locality has to be a int > 0
  """
  try:
    if not isinstance(data['Locality'], int):
      raise ValueError('Error: Locality has the wrong type, int required')
    if data['Locality'] < 0:
      raise ValueError('Error: Locality must be a positive integer')
  except KeyError:
    raise KeyError('Error: Locality field is missing')

def check_swimming_pool(data) -> dict:
  """ 
  This function takes a dictionnary as input representing the data of the users
  Swimming_pool has to be a boolean incoded in integer (0/1), if it is not or Swimming_pool field is missing set the field to 0
  return the (modified) data dictionnary
  """
  data["Swimming_pool_was_missing"] = 0
  try:
    if not isinstance(data['Swimming_pool'], int) :
      print('Swimming_pool field must be 0 or 1, field set to False')
      data['Swimming_pool'] = 0
      data["Swimming_pool_was_missing"] = 1
  except KeyError:
    print('Swimming_pool field is missing, field set to False')
    data['Swimming_pool'] = 0
    data["Swimming_pool_was_missing"] = 1

  return data


def preprocess(data: dict) -> dict:
    """ 
    This function takes a json file as input representing the dta of the users
    It returns a json file with the preprocessed data
    """
    #the following fields are compulsory, if they are missing stop the programm
    check_area(data)
    check_rooms_number(data)
    check_zip_code(data)
    data = check_property_type(data)

    #the following fields are optional, if they are missing, add a field 'field'_was_missing ==1 (0 else)
    #for this project I will only use the field swiming pool 
    proprecessed_data  = check_swimming_pool(data)
    
    return proprecessed_data 