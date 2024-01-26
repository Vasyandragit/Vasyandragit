def month(num, lang):
    
    month_dict = {"ru": ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", 
                         "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"], 
                  "eng": ["January", "February", "March", "April", "May", "June", 
                          "July", "August", "September", "October", "November", "December"]}
    
    return month_dict[lang][num - 1]
