from itertools import combinations

class System:
    def number_regular(self, number):
        return number - 10 if number >= 10 else number
        
    def rule_of_nine(self, number):
        return int('6' + str(number)[1]) if number > 90 else number
    
    def system_plan_1(self, poto, number):
        # Trouver nos deux chiffres
        number = str(number)
        digit_first = int(number[0])
        digit_second = int(number[1])

        if poto == 'P2':
            digit_first = str(self.number_regular(digit_first + 1))
            digit_second = str(self.number_regular(digit_second + 1))

            mouv = self.rule_of_nine(int(digit_first + digit_second))

            return mouv if mouv >= 10 else '0' + str(mouv) 

        if poto == 'P3':
            digit_first = str(self.number_regular(digit_first + 2))
            digit_second = str(self.number_regular(digit_second + 2))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P4':
            digit_first = str(self.number_regular(digit_first + 3))
            digit_second = str(self.number_regular(digit_second + 3))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P5':
            digit_first = str(self.number_regular(digit_first + 4))
            digit_second = str(self.number_regular(digit_second + 4))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P6':
            digit_first = str(self.number_regular(digit_first + 5))
            digit_second = str(self.number_regular(digit_second + 5))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P7':
            digit_first = str(self.number_regular(digit_first + 6))
            digit_second = str(self.number_regular(digit_second + 6))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P8':
            digit_first = str(self.number_regular(digit_first + 7))
            digit_second = str(self.number_regular(digit_second + 7))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P9':
            digit_first = str(self.number_regular(digit_first + 8))
            digit_second = str(self.number_regular(digit_second + 8))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P10':
            digit_first = str(self.number_regular(digit_first + 9))
            digit_second = str(self.number_regular(digit_second + 9))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
    def system_plan_2(self, poto, number):
        # Trouver nos deux chiffres
        number = str(number)
        digit_first = int(number[0])
        digit_second = int(number[1])

        if poto == 'P1':
            digit_first = str(self.number_regular(digit_first + 9))
            digit_second = str(self.number_regular(digit_second + 9))

            mouv = self.rule_of_nine(int(digit_first + digit_second))

            return mouv if mouv >= 10 else '0' + str(mouv) 

        if poto == 'P3':
            digit_first = str(self.number_regular(digit_first + 1))
            digit_second = str(self.number_regular(digit_second + 1))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P4':
            digit_first = str(self.number_regular(digit_first + 2))
            digit_second = str(self.number_regular(digit_second + 2))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P5':
            digit_first = str(self.number_regular(digit_first + 3))
            digit_second = str(self.number_regular(digit_second + 3))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P6':
            digit_first = str(self.number_regular(digit_first + 4))
            digit_second = str(self.number_regular(digit_second + 4))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P7':
            digit_first = str(self.number_regular(digit_first + 5))
            digit_second = str(self.number_regular(digit_second + 5))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P8':
            digit_first = str(self.number_regular(digit_first + 6))
            digit_second = str(self.number_regular(digit_second + 6))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P9':
            digit_first = str(self.number_regular(digit_first + 7))
            digit_second = str(self.number_regular(digit_second + 7))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P10':
            digit_first = str(self.number_regular(digit_first + 8))
            digit_second = str(self.number_regular(digit_second + 8))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 

    def system_plan_3(self, poto, number):
        # Trouver nos deux chiffres
        number = str(number)
        digit_first = int(number[0])
        digit_second = int(number[1])

        if poto == 'P1':
            digit_first = str(self.number_regular(digit_first + 8))
            digit_second = str(self.number_regular(digit_second + 8))

            mouv = self.rule_of_nine(int(digit_first + digit_second))

            return mouv if mouv >= 10 else '0' + str(mouv) 

        if poto == 'P2':
            digit_first = str(self.number_regular(digit_first + 9))
            digit_second = str(self.number_regular(digit_second + 9))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P4':
            digit_first = str(self.number_regular(digit_first + 1))
            digit_second = str(self.number_regular(digit_second + 1))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P5':
            digit_first = str(self.number_regular(digit_first + 2))
            digit_second = str(self.number_regular(digit_second + 2))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P6':
            digit_first = str(self.number_regular(digit_first + 3))
            digit_second = str(self.number_regular(digit_second + 3))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P7':
            digit_first = str(self.number_regular(digit_first + 4))
            digit_second = str(self.number_regular(digit_second + 4))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P8':
            digit_first = str(self.number_regular(digit_first + 5))
            digit_second = str(self.number_regular(digit_second + 5))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P9':
            digit_first = str(self.number_regular(digit_first + 6))
            digit_second = str(self.number_regular(digit_second + 6))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P10':
            digit_first = str(self.number_regular(digit_first + 7))
            digit_second = str(self.number_regular(digit_second + 7))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
    def system_plan_4(self, poto, number):
        # Trouver nos deux chiffres
        number = str(number)
        digit_first = int(number[0])
        digit_second = int(number[1])

        if poto == 'P1':
            digit_first = str(self.number_regular(digit_first + 7))
            digit_second = str(self.number_regular(digit_second + 7))

            mouv = self.rule_of_nine(int(digit_first + digit_second))

            return mouv if mouv >= 10 else '0' + str(mouv) 

        if poto == 'P2':
            digit_first = str(self.number_regular(digit_first + 8))
            digit_second = str(self.number_regular(digit_second + 8))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P3':
            digit_first = str(self.number_regular(digit_first + 9))
            digit_second = str(self.number_regular(digit_second + 9))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P5':
            digit_first = str(self.number_regular(digit_first + 1))
            digit_second = str(self.number_regular(digit_second + 1))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P6':
            digit_first = str(self.number_regular(digit_first + 2))
            digit_second = str(self.number_regular(digit_second + 2))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P7':
            digit_first = str(self.number_regular(digit_first + 3))
            digit_second = str(self.number_regular(digit_second + 3))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P8':
            digit_first = str(self.number_regular(digit_first + 4))
            digit_second = str(self.number_regular(digit_second + 4))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P9':
            digit_first = str(self.number_regular(digit_first + 5))
            digit_second = str(self.number_regular(digit_second + 5))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P10':
            digit_first = str(self.number_regular(digit_first + 6))
            digit_second = str(self.number_regular(digit_second + 6))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
    def system_plan_5(self, poto, number):
        # Trouver nos deux chiffres
        number = str(number)
        digit_first = int(number[0])
        digit_second = int(number[1])

        if poto == 'P1':
            digit_first = str(self.number_regular(digit_first + 6))
            digit_second = str(self.number_regular(digit_second + 6))

            mouv = self.rule_of_nine(int(digit_first + digit_second))

            return mouv if mouv >= 10 else '0' + str(mouv) 

        if poto == 'P2':
            digit_first = str(self.number_regular(digit_first + 7))
            digit_second = str(self.number_regular(digit_second + 7))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P3':
            digit_first = str(self.number_regular(digit_first + 8))
            digit_second = str(self.number_regular(digit_second + 8))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P4':
            digit_first = str(self.number_regular(digit_first + 9))
            digit_second = str(self.number_regular(digit_second + 9))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P6':
            digit_first = str(self.number_regular(digit_first + 1))
            digit_second = str(self.number_regular(digit_second + 1))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P7':
            digit_first = str(self.number_regular(digit_first + 2))
            digit_second = str(self.number_regular(digit_second + 2))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P8':
            digit_first = str(self.number_regular(digit_first + 3))
            digit_second = str(self.number_regular(digit_second + 3))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P9':
            digit_first = str(self.number_regular(digit_first + 4))
            digit_second = str(self.number_regular(digit_second + 4))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 
        
        if poto == 'P10':
            digit_first = str(self.number_regular(digit_first + 5))
            digit_second = str(self.number_regular(digit_second + 5))
            
            mouv = self.rule_of_nine(int(digit_first + digit_second))
            
            return mouv if mouv >= 10 else '0' + str(mouv) 

    def plan_1(self, poto, number):
        # Liste des éléments
        elements = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10']

        # Générer toutes les combinaisons de 3 éléments qui commencent par 'P2'
        combinations_starting_with_p1 = [
            comb for comb in combinations(elements, 3) if comb[0] == poto
        ]
        plans_dict = {}
        dict = {}

        for idx, comb in enumerate(combinations_starting_with_p1):
            deuxieme_element = comb[1]
            troisieme_element = comb[2]
            key = f"[{poto}: {number}, {deuxieme_element}: {self.system_plan_1(deuxieme_element, number)}, {troisieme_element}: {self.system_plan_1(troisieme_element, number)}]"
            plans_dict[idx] = key

        return plans_dict


    def plan_2(self, poto, number):
        # Liste des éléments
        elements = ['P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P1']

        # Générer toutes les combinaisons de 3 éléments qui commencent par 'P2'
        combinations_starting_with_p2 = [
            comb for comb in combinations(elements, 3) if comb[0] == poto
        ]
        plans_dict = {}
        dict = {}

        for idx, comb in enumerate(combinations_starting_with_p2):
            deuxieme_element = comb[1]
            troisieme_element = comb[2]
            key = f"[{poto}: {number}, {deuxieme_element}: {self.system_plan_2(deuxieme_element, number)}, {troisieme_element}: {self.system_plan_2(troisieme_element, number)}]"
            plans_dict[idx] = key

        return plans_dict

    def plan_3(self, poto, number):
        # Liste des éléments
        elements = ['P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P1', 'P2']

        # Générer toutes les combinaisons de 3 éléments qui commencent par 'P2'
        combinations_starting_with_p3 = [
            comb for comb in combinations(elements, 3) if comb[0] == poto
        ]
        plans_dict = {}
        dict = {}

        for idx, comb in enumerate(combinations_starting_with_p3):
            deuxieme_element = comb[1]
            troisieme_element = comb[2]
            key = f"[{poto}: {number}, {deuxieme_element}: {self.system_plan_3(deuxieme_element, number)}, {troisieme_element}: {self.system_plan_3(troisieme_element, number)}]"
            plans_dict[idx] = key

        return plans_dict
    
    def plan_4(self, poto, number):
        # Liste des éléments
        elements = ['P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P1', 'P2', 'P3']

        # Générer toutes les combinaisons de 3 éléments qui commencent par 'P2'
        combinations_starting_with_p4 = [
            comb for comb in combinations(elements, 3) if comb[0] == poto
        ]
        plans_dict = {}
        dict = {}

        for idx, comb in enumerate(combinations_starting_with_p4):
            deuxieme_element = comb[1]
            troisieme_element = comb[2]
            key = f"[{poto}: {number}, {deuxieme_element}: {self.system_plan_4(deuxieme_element, number)}, {troisieme_element}: {self.system_plan_4(troisieme_element, number)}]"
            plans_dict[idx] = key

        return plans_dict
    
    def plan_5(self, poto, number):
        # Liste des éléments
        elements = ['P5', 'P6', 'P7', 'P8', 'P9', 'P10', 'P1', 'P2', 'P3', 'P4']

        # Générer toutes les combinaisons de 3 éléments qui commencent par 'P2'
        combinations_starting_with_p5 = [
            comb for comb in combinations(elements, 3) if comb[0] == poto
        ]
        plans_dict = {}
        dict = {}

        for idx, comb in enumerate(combinations_starting_with_p5):
            deuxieme_element = comb[1]
            troisieme_element = comb[2]
            key = f"[{poto}: {number}, {deuxieme_element}: {self.system_plan_5(deuxieme_element, number)}, {troisieme_element}: {self.system_plan_5(troisieme_element, number)}]"
            plans_dict[idx] = key

        return plans_dict