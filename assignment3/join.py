import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orders = []
    line_items = []

    for v in list_of_values:
      if v[0] == "order":
        orders.append(v)
      elif v[0] == "line_item":
        line_items.append(v)

    for order in orders:
      for line_item in line_items:
        mr.emit(order + line_item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
