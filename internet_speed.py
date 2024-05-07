from tkinter import *
import speedtest

root = Tk()
root.config(bg="white")
root.title("Internet Speed Text")
root.geometry("500x300")

label = Label(root, text="Internet Speed Check", font=("Lucida Sans Unicode", 20, "bold","italic"), fg="#5D6D7E", bg="white")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label = Label(root, text="Download Speed ↓", font=("Lucida Sans Unicode", 18, "bold"), fg="#1E8449", bg="white")
label.place(relx=0.25, rely=0.5, anchor=CENTER)

label = Label(root, text="Upload Speed ↑", font=("Lucida Sans Unicode", 18, "bold"), fg="#9B59B6", bg="white")
label.place(relx=0.75, rely=0.5, anchor=CENTER)

label_download_speed  = Label(root , font=("Yu Gothic Light", 14, "bold"), bg="white")
label_download_speed.place(relx=0.25, rely=0.6, anchor=CENTER)

label_upload_speed  = Label(root , font=("Yu Gothic Light", 14, "bold"), bg="white")
label_upload_speed.place(relx=0.75, rely=0.6, anchor=CENTER)

def speedCheck():
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    label_download_speed['text'] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000,2)
    label_upload_speed['text'] = str(upload_speed) + "mbps"
    
btn_doctor = Button(root, text="Check Speed",command=speedCheck, bg="#218796", fg="white", relief =  FLAT)
btn_doctor.place(relx= 0.5,rely=0.3, anchor=CENTER)

root.mainloop()