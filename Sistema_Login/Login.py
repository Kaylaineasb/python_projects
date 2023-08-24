import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

janela = ctk.CTk()

class Application():
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.janela_login()
        janela.mainloop()

    @staticmethod
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    @staticmethod
    def tela():
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.iconbitmap("icon.ico")
        janela.resizable(False, False)

    @staticmethod
    def janela_login():
        # imagem da tela
        img = PhotoImage(file="imagem.png")
        label_img = ctk.CTkLabel(master=janela, image=img, text=None).place(x=65, y=65)

        # frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # frame widgets
        label = ctk.CTkLabel(master=login_frame, text="Login", font=("Comic-sans", 20)).place(x=150, y=50)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300,
                                      font=("Comic-sans", 14)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="*O campo nome de usuário é de carater obrigatório.",
                                      text_color="white", font=("Comic-sans", 10)).place(x=25, y=135)
        password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Senha", width=300, font=("Comic-sans", 14),
                                      show="*").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="*O campo senha é de carater obrigatório.",
                                      text_color="white", font=("Comic-sans", 10)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar-se de mim").place(x=25, y=235)

        def login():
            msg = messagebox.showinfo(title="Estado de login",message="Login efetuado")
        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300,command=login).place(x=25, y=285)

        register_span = ctk.CTkLabel(master=login_frame, text="Se não tem uma conta").place(x=25, y=325)

        def tela_register():
            #remover o frame de login
            login_frame.pack_forget()
            #criando a tela de cadastro de usuarios
            cadastro_frame = ctk.CTkFrame(master=janela, width=350, height=396)
            cadastro_frame.pack(side=RIGHT)

            label = ctk.CTkLabel(master=cadastro_frame, text="Cadastro", font=("Comic-sans", 20)).place(x=25, y=40)

            span = ctk.CTkLabel(master=cadastro_frame, text="Por favor preencha todos os campos com dados corretos.",text_color="gray", font=("Comic-sans", 10)).place(x=25, y=65)

            username_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Nome de usuário", width=300,
                                          font=("Comic-sans", 14)).place(x=25, y=105)
            email_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="E-mail de usuário", width=300,
                                          font=("Comic-sans", 14)).place(x=25, y=145)
            passwor_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Senha de usuário", width=300,
                                          font=("Comic-sans", 14),show="*").place(x=25, y=185)
            cpass_entry = ctk.CTkEntry(master=cadastro_frame, placeholder_text="Confirma senha", width=300,
                                          font=("Comic-sans", 14),show="*").place(x=25, y=225)
            checkbox = ctk.CTkCheckBox(master=cadastro_frame, text="Aceito dos termos e Políticas").place(x=25, y=265)
            def back():
                # removendo o frame de cadastro
                cadastro_frame.pack_forget()
                # devolvendo o frame de login
                login_frame.pack(side=RIGHT)
            back_button = ctk.CTkButton(master=cadastro_frame, text="Voltar", width=145, command=back).place(x=25, y=300)
            def save_user():
                msg = messagebox.showinfo(title="Estado do Cadastro", message="Parabéns!Usuário cadastrado com sucesso!")
            save_button = ctk.CTkButton(master=cadastro_frame, text="Cadastrar", width=145, command=save_user).place(x=180, y=300)


        register_button = ctk.CTkButton(master=login_frame, text="CADASTRE-SE", width=150, command=tela_register).place(
            x=175, y=325)
Application()
