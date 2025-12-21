import data 

quest_index = 0 
quest_data = data.questions 
def generate_quest(QUEST, buttons) :
    if quest_index<len(quest_data ):
        quest = quest_data[quest_index] ["quest"]
        QUEST.config(text=quest) 

        for i in range (len(buttons)):
            buttons[i].config(text=quest_data[quest_index]["answers"][i])

    else:
        QUEST.config(text="Викторина закончена")
        for btn in buttons:
            btn.config(state="diablet")
    
def choice(button,QUEST,buttons,info):
    global quest_index  
    if button["text"]==quest_data[quest_index]["right"]:
        quest_index += 1
        info.config(text="") 
        generate_quest(QUEST,buttons)
    else:
        info.config(text="Ответ неверный") 


