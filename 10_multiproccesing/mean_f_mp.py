from csv import DictReader
from collections import Counter

def mean_f_mp(queue_files,queue_sum,queue_count):
    tag_step = {}
    tag_step_cnt = {}
    while not queue_files.empty():
        name = queue_files.get()
        with open(name) as csvfile:
            print(name)
            reader = DictReader(csvfile,delimiter = ';')
            for row in reader:
                if row['tag'] not in tag_step:
                    tag_step[row['tag']] = 0
                    tag_step_cnt[row['tag']] = 0
                tag_step[row['tag']] += int(row['n_steps'])
                tag_step_cnt[row['tag']] += 1
    queue_sum.put(tag_step)
    queue_count.put(tag_step_cnt)
    return True

def merging_dicts(big_dict):
    counter = Counter()
    [counter.update(i) for i in big_dict]
    return(dict(big_dict[0]))
