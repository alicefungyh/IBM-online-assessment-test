def validate_data(file):
    '''file (string): name of file to be read'''
    with open(file) as f:
        lst = []
        for line in f.readlines():
            lst.append(line)
    
    error_lst = []
    for i in lst:
        if len(i) == 3:
            if i[2] not in error_lst:
                error_lst.append(i[2])
            else:
                pass
    
    if len(error_lst) == 0:
        result = 'Yes'
        
    if len(error_lst) > 0:
        result = f"No, {error_lst}"
        
    return result