def look_for_size(shop_num, shop_size, request_num, request_size):
    if len(shop_num)<len(request_num):
        fulfil = 'No'
    
    else:
        lst1 = []
        for i in shop_size:
            if 'L' in i:
                lst1.append(len(i))
            elif 'S' in i:
                lst1.append(-len(i))
            else:
                lst1.append(0)

        lst2 = []
        for j in request_size:
            if 'L' in j:
                lst2.append(len(j))
            elif 'S' in j:
                lst2.append(-len(j))
            else:
                lst2.append(0)

        size1 = max(lst1)
        size2 = max(lst2)
        
        if size1 >= size2:
            fulfil = 'Yes'
        else:
            fulfil = 'No'
        
        
    return fulfil