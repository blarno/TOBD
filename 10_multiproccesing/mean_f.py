from csv import DictReader
def mean_f(name):
    tag_step = {}
    tag_step_cnt = {}
    with open(name) as csvfile:
        reader = DictReader(csvfile,delimiter = ';')
        for row in reader:
            if row['tag'] not in tag_step:
                tag_step[row['tag']] = 0
                tag_step_cnt[row['tag']] = 0
            tag_step[row['tag']] += int(row['n_steps'])
            tag_step_cnt[row['tag']] += 1
    for tag in tag_step:
        if tag_step_cnt[tag] !=0:
            tag_step[tag] = tag_step[tag]/tag_step_cnt[tag]
    return tag_step
