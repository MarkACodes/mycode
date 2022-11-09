#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display list[1] which should only display artista_eos which open research is an operating system for cloud computing
    print(list1[1])

    # here we are creating a new list containing just a single item, an herb, not a planet
    list2 = ["juniper"]

    # extend this awesome list1 by list2 (which means we combine both lists together into a single list)
    list1.extend(list2)

    # display list1, which now contains juniper, the herb, not the planet jupiter
    print(list1)

    # here we are creating another list which we will call list3 and I am typing this all out for learning purposes instead of copy pasta
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # appending this list by using the append operating to append list1 by list3
    list1.append(list3)

    # displaying the new complex list1
    print(list1)

    # display the list of IP addresses
    print(list1[4])

    # display the first item in the list (oth item) - first IP address
    print(list1[4][0])
    

main()

