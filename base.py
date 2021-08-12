
def diagnose(symptom_list):


    result = rule1(symptom_list)
    if result != 0:
        return result
    else:
        result = rule2(symptom_list)
        if result != 0:
            return result
        else:
            result = rule3(symptom_list)
            if result != 0:
                return result
            else:
                result = rule4(symptom_list)
                if result != 0:
                    return result
                else:
                    result = rule5(symptom_list)
                    if result != 0:
                        return result
                    else:
                        result = rule6(symptom_list)
                        return result



def rule1(symptom_type):
    if symptom_type[0] == 'Dry':
        return 'Covid-19'
    else:
        return 0

def rule2(symptom_type):
    if symptom_type[0] == 'NoCough':
        if len(symptom_type) == 1:
            return 0
        if symptom_type[1] == 'Mild':
            return 'Covid-19'
        else :
            return 0
    else:
        return 0

def rule3(symptom_type):
    if symptom_type[0] == 'NoCough':
        if len(symptom_type) == 1:
            return 0
        if symptom_type[1] == 'None':
            return 'Flu'
        else :
            return 0
    else:
        return 0

def rule4(symptom_type):
    if symptom_type[0] == 'Wet':
        if len(symptom_type) == 1:
            return 0
        if symptom_type[1] == 'None':
            return 'Cold'
        else :
            return 0
    else:
        return 0

def rule5(symptom_type):
    if symptom_type[0] == 'Wet':
        if len(symptom_type) == 1:
            return 0
        if symptom_type[1] == 'High':
            return 'Flu'
        else :
            return 0
    else:
        return 0

def rule6(symptom_type):
    if symptom_type[0] == 'Wet':
        if len(symptom_type) == 1:
            return 0
        if symptom_type[1] == 'Mild':
            return 'Cold'
        else :
            return 0
    else:
        return 0

