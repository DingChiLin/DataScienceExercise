import MapReduce
import sys
import json

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix_name = record[0]
    i = record[1]
    j = record[2]

    for k in range(0,5):
        if matrix_name == 'a':
            mr.emit_intermediate(json.dumps([i,k]),record)
        else:
            mr.emit_intermediate(json.dumps([k,j]),record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    m_a = filter(lambda x: x[0] == 'a', list_of_values)
    m_b = filter(lambda x: x[0] == 'b', list_of_values)

    value = 0
    for record_a in m_a:
        for record_b in m_b:
            if record_a[2] == record_b[1]:
                value += record_a[3]*record_b[3]

    mr.emit((json.loads(key)[0],json.loads(key)[1], value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
