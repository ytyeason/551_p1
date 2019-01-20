


import json # we need to use the JSON package to load the data, since the data is stored in JSON format

with open("proj1_data.json") as fp:
    data = json.load(fp)

# Now the data is loaded.
# It a list of data points, where each datapoint is a dictionary with the following attributes:
# popularity_score : a popularity score for this comment (based on the number of upvotes) (type: float)
# children : the number of replies to this comment (type: int)
# text : the text of this comment (type: string)
# controversiality : a score for how "controversial" this comment is (automatically computed by Reddit)
# is_root : if True, then this comment is a direct reply to a post; if False, this is a direct reply to another comment

# Example:
'''
data_point = data[0] # select the first data point in the dataset

# Now we print all the information about this datapoint

for info_name, info_value in data_point.items():
    print(info_name + " : " + str(info_value))
'''

training_set = data[0:10000]
validation_set = data[10000:11000]
testing_set = data[11000:12000]



def pre_process_text(text,frequency_map):
    precessed_list = text.lower().split()

    for word in precessed_list:
            if word in frequency_map:
                frequency_map[word] = frequency_map[word] + 1
            else:
                frequency_map[word] = 1
    return precessed_list

def pre_process(training_set):
    frequency_map = {}
    #preprocess is_root and text
    for item in training_set:
        if item['is_root'] == True:
            item['is_root'] = 1
        else:
            item['is_root'] = 0
        item['text'] = pre_process_text(item['text'],frequency_map)

    #sort the map by key in dscending order
    frequency_map = sorted(frequency_map.items(), key=lambda kv: kv[1], reverse = True)
    #first get the top 160 item of the map, then get the keys into a list
    most_frequent_word = [i[0] for i in frequency_map[0:160]]

    for item in training_set:
        x_counts = [0]*160
        for word in item['text']:
            if word in most_frequent_word:
                index = most_frequent_word.index(word)
                x_counts[index] = x_counts[index] + 1
        item['w_counts'] = x_counts

pre_process(training_set)
print(training_set[9])













#end
