#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    
    tickets = [
      Ticket{ source: "PIT", destination: "ORD" },
      Ticket{ source: "XNA", destination: "CID" },
      Ticket{ source: "SFO", destination: "BHM" },
      Ticket{ source: "FLG", destination: "XNA" },
      Ticket{ source: "NONE", destination: "LAX" },
      Ticket{ source: "LAX", destination: "SFO" },
      Ticket{ source: "CID", destination: "SLC" },
      Ticket{ source: "ORD", destination: "NONE" },
      Ticket{ source: "SLC", destination: "PIT" },
      Ticket{ source: "BHM", destination: "FLG" }
    ]

    OutPut:
    ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
    
    """

    # insert the values into hashtable
    # loop thru each ticket inside [tickets]
    for ticket in tickets:
        # use insert function to fill the hashtable with tix start location (source)
        # and tix destination
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    """
    where the source string represents the starting airport and the destination 
    string represents the next airport along our trip. The ticket for your first flight 
    has a destination with a source of NONE, and the ticket for your final flight has a 
    source with a destination of NONE
    """
    # ticket with a source of NONE
    source = hash_table_retrieve(hashtable, "NONE")

    # value representing your current location
    current = source

    """
    when constructing the entire route, the ith location in the route can be found by checking 
    the hash table for the i-1th location.
    """
    # i is the location - 1
    for i in range(length - 1):
        # this will connect the flights together
        next_location = hash_table_retrieve(hashtable, current)
        # destination is the current index
        route[i] = current
        # setting up the next iteration of the function
        current = next_location

    return route
