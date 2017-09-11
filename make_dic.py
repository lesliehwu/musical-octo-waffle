name = ["Anna", "Eli", "Pariece", "Brendan", "Amy"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dic(santas,craigs):
    my_dic = {}

    if len(santas) >= len(craigs):
        giga = zip(santas,craigs)
    else:
        giga = zip(craigs,santas)

    for present,creeper in giga:
        my_dic[present] = creeper

    print my_dic
        
make_dic(name,favorite_animal)
