import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]

    mr.emit_intermediate(value, key)
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    asymmetric_friendships = []

    for v in list_of_values:
        if v not in total:
            total.append(v)
            asymmetric_friendships.append(v)
        else:
            asymmetric_friendships.remove(v)

    for a_friend in asymmetric_friendships:
        mr.emit((key, a_friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
