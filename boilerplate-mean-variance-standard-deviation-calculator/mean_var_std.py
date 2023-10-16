import numpy as np


def calculate(list):

  if len(list) != 9:

    raise ValueError("List must contain nine numbers.")

  arr2d = np.array(list).reshape(3, -1)
  arr1d = arr2d.flatten()

  list_keys = ["mean", "variance", "standard deviation", "max", "min", "sum"]

  list_numpy_function_names = ["mean", "var", "std", "max", "min", "sum"]

  calculations = {}
  for idx, key in enumerate(list_keys):

    function_string = list_numpy_function_names[idx]

    result0 = getattr(np, function_string)(arr2d, axis=0).tolist()

    result1 = getattr(np, function_string)(arr2d, axis=1).tolist()

    resultf = getattr(np, function_string)(arr1d).tolist()

    calculations[key] = [result0, result1, resultf]

  return calculations
