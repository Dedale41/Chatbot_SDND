from ast import Add
import streamlit as st
from streamlit_chat import message
from agenda import add_new_print 
import re


st.set_page_config(page_title="Entreprise Imprimenligne & co",layout="centered")


if 'message_history' not in st.session_state:
    st.session_state["message_history"]=["Salut ! Je suis l'ultra bot 3000, je peux imprimer tes documents."]

if 'user_history' not in st.session_state:
    st.session_state["user_history"]=[False]

if 'message_count' not in st.session_state:
    st.session_state["message_count"]=1

if 'agenda' not in st.session_state:
    st.session_state["agenda"]=agenda=[[],[],[],[],[],[]]

placeholder = st.empty()  # placeholder for the messages

input_ = st.text_input("you:") # user input
if input_!='':
    st.session_state["message_history"].append(input_)
    st.session_state["user_history"].append(True)

    st.session_state["message_history"].append("reponse")
    st.session_state["user_history"].append(False)


with placeholder.container(): #display all the messages
    for i in range(len(st.session_state["message_history"])):
        message(st.session_state["message_history"][i],is_user=st.session_state["user_history"][i],key=st.session_state["message_count"])
        st.session_state["message_count"]+=1

with st.sidebar:
    nb_pages=st.number_input('nb_pages:',value=0,step=1)
    docname=st.text_input('docname:')
    hour=st.number_input('hour:',value=0,step=1)
    day=st.number_input('day:',value=0,min_value=0,max_value=6,step=1)
    update_agenda=st.button("update agenda:")

if update_agenda:
    agenda=add_new_print(docname,nb_pages,hour,day,st.session_state["agenda"])
    if agenda!=-1:
        st.session_state["agenda"]=agenda



st.session_state["agenda"]






















# try:
#     st.session_state["question"]
#     st.write(type(st.session_state["question"]))
#     st.session_state["question"]==''

# except:
#     'question non definie'



# try:
#     j=st.session_state["flag"]
# except:
#     st.session_state["flag"]=True


# chat_box=st.empty()
# left_margin,client,bot,right_margin=chat_box.columns((1,2,2,1))


# if st.session_state["flag"]:
#     question=client.text_input(label="faites votre commande ici")
#     st.session_state["question"]=(question+ '.')[:-1]
#     st.session_state['flag']=False
# else:
#     # client.empty()
#     client.text_input(label="faites votre commande ici",placeholder=st.session_state["question"],disabled=True)

# st.write('''
   
# ''')
# bot.markdown("***")
# bot.text( st.session_state["question"])

