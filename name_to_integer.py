global name_encode
def names_to_no(names):
    int_label=[]
    for name in names:
        if name not in int_label: 
           int_label.append(name)
    indices=[]
    for i in int_label:
        indices.append(int_label.index(i))
        
    name_encode={}
    for name in int_label:
        name_encode[name]=int_label.index(name)
    
    str_to_int=[]
    for name in names:
       for i in name_encode:
        if name==i:
            str_to_int.append(int(name_encode[i]))
    
    return str_to_int,name_encode
        
#names=['s','s','z','a','z','a']       
#names_to_no(names)         
        

        
