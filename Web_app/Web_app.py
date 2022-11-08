from ast import Add
import streamlit as st
from streamlit_chat import message
from agenda import add_new_print 
from answer_query import find_doc_name, find_pages_number
import classifier as cl
import re


st.set_page_config(page_title="Entreprise Imprimenligne & co",layout="centered")


if 'message_history' not in st.session_state:
    st.session_state["message_history"]=["Salut ! Je suis l'ultra bot 3000, je peux imprimer tes documents."]

if 'user_history' not in st.session_state:
    st.session_state["user_history"]=[False]

if 'message_count' not in st.session_state:
    st.session_state["message_count"]=1

if 'agenda' not in st.session_state:
    st.session_state["agenda"]=[[],[],[],[],[],[]]

if 'agenda_display' not in st.session_state:
    st.session_state["agenda_display"]=False

if 'model' not in st.session_state:
    # st.session_state["model"]=cl.import_model("../Model/model.pickle") #for offline version
    st.session_state["model"]=cl.import_model("/app/chatbot_printer/Model/model.pickle") #for online version

jour=["lundi","mardi","mercredi",'jeudi','vendredi','samedi',"dimanche"]
toggle=["afficher", "cacher"]
def vider_agenda():
    st.session_state["agenda"]=[[],[],[],[],[],[]]


def switch_agenda():
    st.session_state["agenda_display"]=not st.session_state["agenda_display"]

with st.sidebar:
    st.write("### Programmer une impression")
    date_str=str(st.date_input("choisir la date"))
    [y,mois,d]=re.split("-",date_str)

    F=int(d)+ ((13*int(mois)-1)/5) +int(y[2:])*3/4 +-7/4*int(y[:2])
    day_nb=int(((F-2)%7)//1)
    # Zeller's Rule:
    # d is  the day of the month.
    # mois is the month number.
    # y[2:] is the last two digits of the year.
    # y[:2] is the first two digits of the year
    # 0=monday,1=tuesday,...,6=sunday you get it

    time_str = str(st.time_input("choisir l'heure"))
    [h,m,s]=re.split(":",time_str)
    time_sec=int(h)*3600+int(m)*60+int(s)

    st.button("vider l'agenda", on_click=vider_agenda)
    st.button(toggle[st.session_state["agenda_display"]]+" l'agenda", on_click=switch_agenda)

    if st.session_state["agenda_display"]:
        st.session_state["agenda"]
   


placeholder = st.empty()  # placeholder for the messages

input_ = st.text_input("you:") # user input
if input_!='':
    st.session_state["message_history"].append(input_)
    st.session_state["user_history"].append(True)


    pred=st.session_state["model"].predict([input_])[0]
    if pred==1:
        nb_p=find_pages_number(input_)
        doc_n=find_doc_name(input_)
        if nb_p!=-1:
            if doc_n!=-1:
                try:
                    [h_print,d_print]=add_new_print(doc_n,int(nb_p),int(time_sec),int(day_nb),st.session_state["agenda"])
                    reponse="Nous lançons l'impression de "+str(nb_p)+" pages du document "+str(doc_n)+"."+" L'impression commence à "+str(h_print//3600)+"h "+str((h_print%3600)//60)+"min "+str((h_print%3600)%60)+"s "+jour[d_print]+" et durera "+str(int(nb_p)//3600)+"heures "+str((int(nb_p)%3600)//60)+"min "+str(int(nb_p)%60)+"secondes."

                except TypeError:
                    if int(nb_p)>36000:
                        reponse="Votre fichier est trop gros pour être imprimé en une seule journée, on ne peut s'en charger."
                    else:
                        reponse="Votre fichier ne peut pas être imprimé cette semaine, tentez la semaine suivante."
            else:
                try:
                    [h_print,d_print]=add_new_print(str(st.session_state["message_count"]),int(nb_p),int(time_sec),int(day_nb),st.session_state["agenda"])
                    reponse="Nous lançons l'impression de "+str(nb_p)+" pages. L'impression commence à "+str(h_print//3600)+"h "+str((h_print%3600)//60)+"min "+str((h_print%3600)%60)+"s "+jour[d_print]+" et durera "+str(int(nb_p)//3600)+"heures "+str((int(nb_p)%3600)//60)+"min "+str(int(nb_p)%60)+"secondes."
                except TypeError:
                    if int(nb_p)>36000:
                        reponse="Votre fichier est trop gros pour être imprimé en une seule journée, on ne peut s'en charger."
                    else:
                        reponse="Votre fichier ne peut pas être imprimé cette semaine, tentez la semaine suivante."
        else:
            reponse="Désolé je n'ai pas compris votre requête, pour lancer une impression veuillez me donner le nom de votre document ainsi que son nombre de pages"
    else:
        reponse="Désolé je n'ai pas compris votre requête, pour lancer une impression veuillez me donner le nom de votre document ainsi que son nombre de pages"


    st.session_state["message_history"].append(reponse)
    st.session_state["user_history"].append(False)


with placeholder.container(): #display all the messages
    for i in range(len(st.session_state["message_history"])):
        message(st.session_state["message_history"][i],is_user=st.session_state["user_history"][i],key=st.session_state["message_count"])
        st.session_state["message_count"]+=1



