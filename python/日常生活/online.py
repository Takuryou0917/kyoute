import streamlit as st
import pandas as pd

st.title("共通テスト合計点計算サイト")
st.header("文系理系どちらにも対応しています")
st.subheader("使い方↓")
st.text("点数を自動で合計してくれるプログラムです")
st.text("３点問題を２問 ４点問題を２個とった場合[3344]と打てば合計されて14点と表示されます *1")
st.text("初めにmをつけると間違えた点数の合計分を満点から引いてくれます *2")
st.text("合計を計算し終わっている場合は点数の前にgをつけると合計のままで計算します *3")
st.text("間違えた点数の合計がわかっている場合は前にnをつけるとその数字を引くいてくれます *4")
st.text("*1　3344=14点　*2　数1A　m5555=80点　　*3　g80=80点　　*4　n20=80点")
st.header(" ")

tensu = ["0","0","0","0","0","0","0","0","0"]
option = st.radio('文理選択',['理系', '文系'])
col1,col2,col3 = st.columns(3)

if option=="文系":
    listb1 = ['日本史', '世界史','地理','倫理','政治 経済']
    with col1:
        option1 = st.radio('社会科選択１科目',listb1)
    listb2 = [item for item in listb1 if item != option1]
    with col2:
        option2 = st.radio('社会科選択２科目',listb2)
    st.write(f"選択科目は{option1}と{option2}です")
    list = [["国語","英語R","英語L","数1A","数2BC","理科基礎",option1,option2,"情報"]]
    value = st.slider('目標点', 0, 1000, 750,step=10)
    st.subheader('点数入力')
    tensu[0] = str(st.text_input('国語') or "0")
    tensu[1] = str(st.text_input('英語R') or "0")
    tensu[2] = str(st.text_input('英語L') or "0")
    tensu[3] = str(st.text_input('数1A') or "0")
    tensu[4] = str(st.text_input('数2BC') or "0")
    tensu[5] = str(st.text_input('理科基礎') or "0")
    tensu[6] = str(st.text_input(option1) or "0")
    tensu[7] = str(st.text_input(option2) or "0")
    tensu[8] = str(st.text_input('情報') or "0")

elif option == "理系":
    listr1 = ['物理', '化学','生物']
    with col1:
        option1 = st.radio('理科選択１科目',listr1)
    listr2 = [item for item in listr1 if item != option1]
    with col2:
        option2 = st.radio('理会科選択２科目',listr2)
    with col3:
        option3 = st.radio('社会科選択',['地理','政治 経済'])
    st.write(f"選択科目は{option1}と{option2}と{option3}です")
    list = [["国語","英語R","英語L","数1A","数2BC",option1,option2,option,"情報"]]
    value = st.slider('目標点', 0, 1000, 750,step=10)
    st.subheader('点数入力')
    tensu[0] = str(st.text_input('国語') or "0")
    tensu[1] = str(st.text_input('英語R') or "0")
    tensu[2] = str(st.text_input('英語L') or "0")
    tensu[3] = str(st.text_input('数1A') or "0")
    tensu[4] = str(st.text_input('数2BC') or "0")
    tensu[5] = str(st.text_input(option1) or "0")
    tensu[6] = str(st.text_input(option2) or "0")
    tensu[7] = str(st.text_input(option3) or "0")
    tensu[8] = str(st.text_input('情報') or "0")

button = st.button('決定')
if button:
    for i in range(9):
        if tensu[i][0] != "g" and tensu[i][0] != "m" and tensu[i][0] != "n":
            u=0
            for j in range(0,len(tensu[i])):
                u = u + int(tensu[i][j])
            tensu[i] = u
        elif tensu[i][0] == "g":
            tensu[i] = int(tensu[i].replace("g",""))
        elif tensu[i][0] == "n":
            if i == 0:
                tensu[i] = 200 - int(tensu[i].replace("n",""))
            else:
                tensu[i] = 100 - int(tensu[i].replace("n",""))
        elif tensu[i][0] == "m":
            tensu[i] = tensu[i].replace("m","")
            if i==0:
                u = 200
            else:
                u = 100
            for j in range(0,len(tensu[i])):
                u = u - int(tensu[i][j])
            tensu[i] = u

    if option == '文系':
        df = pd.DataFrame({'教科':["国語","英語R","英語L","数1A","数2BC","理基礎",option1,option2,"情報"],
            '点数':[tensu[0],tensu[1],tensu[2],tensu[3],tensu[4],tensu[5],tensu[6],tensu[7],tensu[8]],
            '割合%':[int(tensu[0])/2,tensu[1],tensu[2],tensu[3],tensu[4],tensu[5],tensu[6],tensu[7],tensu[8]],
            })
        st.write(df)

    elif option == '理系':
        df = pd.DataFrame({'教科':["国語","英語R","英語L","数1A","数2BC",option1,option2,option3,"情報"],
            '点数':[tensu[0],tensu[1],tensu[2],tensu[3],tensu[4],tensu[5],tensu[6],tensu[7],tensu[8]],
            '割合%':[int(tensu[0])/2,tensu[1],tensu[2],tensu[3],tensu[4],tensu[5],tensu[6],tensu[7],tensu[8]],
            })
        st.write(df)

    k = 0
    for i in range(9):
        k = k+int(tensu[i])

    st.write('合計点 ',k,'点',sep='')
    st.write('割合 ',k/10,"%",sep='')
    st.write('目標点 ',value,'点',sep='')

    if k-value < 0:
        st.write('目標点まであと',value-k,'点',sep='')
    else:
        st.write('目標点達成！！！')