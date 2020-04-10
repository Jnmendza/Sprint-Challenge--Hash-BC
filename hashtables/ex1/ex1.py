# Initial Commit
#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # insert the values into your hashtable
    # loop thru each individual weight inside [weights]
    for i in range(len(weights)):
        # use insert function to fill the hashtable with our weights
        # i is the single value inside the [weights]
        hash_table_insert(ht, weights[i], i)

    # loop thru the length
    for i in range(length):
        """
        If we store each weight's list index as its value, we can then check 
        to see if the hash table contains an entry for limit - weight. If it 
        does, then we've found the two items whose weights sum up to the limit!
        """
        value = limit - weights[i]
        difference = hash_table_retrieve(ht, value)

        """
        The higher valued index should be placed in the zeroth index and the 
        smaller index should be placed in the first index.
        """
        if difference and difference > i:
            pair = [difference, i]
            return pair

    return None

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
