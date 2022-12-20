friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)
    
iteration 0 is john                                                                                                                                                                                                                              
iteration 1 is pat                                                                                                                                                                                                                               
iteration 2 is gary                                                                                                                                                                                                                              
iteration 3 is michael  
------------------------------------------
activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }
print activities
print activities[8]
for keys in activities.keys():
    print "%s: %s"  %(keys, activities[keys] )
------------------------------------------
size= 4
for i in range(size):
    print i
------------------------------------------
