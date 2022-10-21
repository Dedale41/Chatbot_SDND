def add_new_print(doc_name,nb_pages,hour,day,agenda):
    h_debut=8*3600
    h_fin=18*3600

    if len(agenda[day])==0:                                     #si l'agenda de la journée est vide
        print("tortue")
        if hour+nb_pages<=h_fin:                                #si l'impression passe dans le reste de la journée
            agenda[day].append([hour,hour+nb_pages,doc_name])
        else:                                                   #si l'impression dépasse, on déplace au lendemain à la première heure, si c'est déjà samedi, on prépare pas pour la semaine suivante, erreur
            if day<5:
                return add_new_print(doc_name,nb_pages,h_debut,day+1,agenda)
            else:
                return -1
    else:
        if agenda[day][-1][1]<hour  :                                 #si l'agenda est libre au moment où on fait la demande d'impression
            print("lourte")
            if hour+nb_pages<=h_fin:                                #si l'impression passe dans le reste de la journée
                agenda[day].append([hour,hour+nb_pages,doc_name])
            else:                                                   #si l'impression dépasse, on déplace au lendemain à la première heure, si c'est déjà samedi, on prépare pas pour la semaine suivante, erreur
                if day<5:
                    return add_new_print(doc_name,nb_pages,h_debut,day+1,agenda)
                else:
                    return -1
        else:                                                       #si l'agenda n'est pas libre au moment de la demande d'impression
            print("truite")
            if agenda[day][-1][1]+nb_pages<=h_fin:                  #si l'impression passe dans la journée
                agenda[day].append([agenda[day][-1][1],agenda[day][-1][1]+nb_pages,doc_name])
            else:                                                   #si l'impression dépasse, on déplace au lendemain à la première heure, si c'est déjà samedi, on prépare pas pour la semaine suivante, erreur
                if day<5:
                    return add_new_print(doc_name,nb_pages,h_debut,day+1,agenda)
                else:
                    return -1
    return agenda