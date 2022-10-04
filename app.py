import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
st.set_page_config(page_title="CAY NHA LA VUON")
st.header("Predict revenue based on advertising budget")
data_file=st.file_uploader("Input your file here ",type="xlsx")
flag=False
if data_file is not None :
    df=pd.read_excel(data_file)
    st.dataframe(df)
    label=st.text_input("Enter your label's name")
    if label!="" and label not in df.columns :
        st.warning('Not find label name in data frames', icon="⚠️")
    elif label in df.columns :
        flag=True
    else:
        st.warning("Not received input")
    if flag:
        col=df.shape[1]-1
        row=df.shape[0]
        X_train=np.ones([row,col])
        Y_train=np.ones([row,1])
        agree = st.checkbox("Are/Is there your features ?If not please check your data frames format and restart website")
        index=0
        for x in df.columns :
            if x !=label:
                st.write(x)
                X_train[:,index]=df[x]
                index+=1
        if agree==True:
            Y_train[:,0]=df[label]
            epoch=10
            if row<10: epoch=row
            X=tf.compat.v1.placeholder(tf.float32 ,[epoch,col] )
            Y=tf.compat.v1.placeholder(tf.float32,[epoch,1])
            W=tf.Variable(tf.ones([col,1]))
            b=tf.Variable(np.random.randn(),dtype=tf.float32)
            pred=tf.add(tf.matmul(X,W),b)
            loss=tf.compat.v1.reduce_mean (tf.square(pred-Y))
            optimizer=tf.compat.v1.train.GradientDescentOptimizer(learning_rate= 0.01).minimize(loss)
            init=tf.compat.v1.global_variables_initializer ()
            sess=tf.compat.v1.Session()
            sess.run(init)
            for i in range(0,row,epoch):
                if row-i<epoch:
                    epoch=row-i
                sess.run(optimizer,feed_dict={X:X_train[i:i+epoch,:],Y:Y_train[i:i+epoch,:]})
            my_array = np.array([])
            for x in df :
                if x !=label :
                    num=float(st.number_input("Enter value of "+x+" :"))
                    my_array=np.append(my_array,values=num)
            agree = st.checkbox("Click here to see your revenue predicted")
            if agree==True :
                my_array=my_array.reshape(1,-1)
                x=np.matmul(my_array,sess.run(W))
                st.write("Revenue forecast results is "+str(x[0]))



