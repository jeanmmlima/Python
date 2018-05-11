#!/usr/bin/python
# -*- coding: utf8 -*-


from Tkinter import *

import os

class Application:
      def __init__(self, master=None):
          self.fonte = ("Verdana", "8")
   
          self.container1 = Frame(master)
          self.container1["pady"] = 10
          self.container1.pack()
          self.container2 = Frame(master)
          self.container2["padx"] = 20
          self.container2["pady"] = 5
          self.container2.pack()
          self.container3 = Frame(master)
          self.container3["padx"] = 20
          self.container3["pady"] = 5
          self.container3.pack()
          self.container4 = Frame(master)
          self.container4["padx"] = 20
          self.container4["pady"] = 5
          self.container4.pack()
          self.container5 = Frame(master)
          self.container5["padx"] = 20
          self.container5["pady"] = 5
          self.container5.pack()
          self.container6 = Frame(master)
          self.container6["padx"] = 20
          self.container6["pady"] = 5
          self.container6.pack()
          self.container7 = Frame(master)
          self.container7["padx"] = 20
          self.container7["pady"] = 5
          self.container7.pack()
          self.container8 = Frame(master)
          self.container8["padx"] = 15
          self.container8["pady"] = 10
          self.container8.pack()
          self.container9 = Frame(master)
          self.container9["pady"] = 15
          self.container9.pack()
   
          self.titulo = Label(self.container1, text="Cadastro de Usuários - LABGRAD:")
          self.titulo["font"] = ("Calibri", "9", "bold")
          self.titulo.pack ()
   
          self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=15)
          self.lblnome.pack(side=LEFT)
   
          self.txtnome = Entry(self.container3)
          self.txtnome["width"] = 25
          self.txtnome["font"] = self.fonte
          self.txtnome.pack(side=LEFT)
  
   
          self.lblusuario= Label(self.container5, text="Usuário:", font=self.fonte, width=15)
          self.lblusuario.pack(side=LEFT)
   
          self.txtusuario = Entry(self.container5)
          self.txtusuario["width"] = 25
          self.txtusuario["font"] = self.fonte
          self.txtusuario.pack(side=LEFT)

   
          self.lblsenha= Label(self.container6, text="Senha:", font=self.fonte, width=15)
          self.lblsenha.pack(side=LEFT)
   
          self.txtsenha = Entry(self.container6)
          self.txtsenha["width"] = 25
          self.txtsenha["show"] = "*"
          self.txtsenha["font"] = self.fonte
          self.txtsenha.pack(side=LEFT)

	  self.lblsenha= Label(self.container7, text="Confirma Senha:", font=self.fonte, width=15)
          self.lblsenha.pack(side=LEFT)
   
          self.txtconfirmaSenha = Entry(self.container7)
          self.txtconfirmaSenha["width"] = 25
          self.txtconfirmaSenha["show"] = "*"
          self.txtconfirmaSenha["font"] = self.fonte
          self.txtconfirmaSenha.pack(side=LEFT)

   
          self.bntCadastrar = Button(self.container8, text="Cadastrar", font=self.fonte, width=12)
          self.bntCadastrar["command"] = self.cadastrarUser
          self.bntCadastrar.pack (side=LEFT)
   
          self.bntCancelar = Button(self.container8, text="Cancelar", font=self.fonte, width=12)
          self.bntCancelar["command"] = self.cancelarCadastro
          self.bntCancelar.pack (side=LEFT)
   
          self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
         # self.bntExcluir["command"] = self.excluirUsuario
          self.bntExcluir.pack(side=LEFT)
   
          self.lblmsg = Label(self.container9, text="")
          self.lblmsg["font"] = ("Verdana", "9", "italic")
          self.lblmsg.pack()

      def cadastrarUser(self):
	  os.system("echo Nome: "+self.txtnome.get())
	  os.system("echo Usuário: "+self.txtusuario.get())
	  os.system("echo Senha: "+self.txtsenha.get())
	  os.system("echo Confirma a Senha: "+self.txtconfirmaSenha.get())
	  

          if(self.txtsenha.get() == self.txtconfirmaSenha.get()):
     	 os.system("echo Senha correta. Criando usuário...")
     	 self.lblmsg["fg"] = "green"
           self.lblmsg["text"] = "Senha correta. Criando usuário..."
           os.system("sudo useradd -m -d /home/"+self.txtusuario.get()+" -p $(openssl passwd -1 "+self.txtsenha.get()+") -s /bin/bash "+self.txtusuario.get())
           os.system("sudo chown -R "+self.txtusuario.get()+" /home/"+self.txtusuario.get()) 
           os.system("sudo chmod -R o-r /home/"+self.txtusuario.get()) 
           self.lblmsg["text"] = "Usuário Criado!"


	    else:
		os.system("echo Erro ao confirmar a senha!")
		self.lblmsg["fg"] = "red"
	     self.lblmsg["text"] = "Senha Incorreta. Redigite a senha!"


      def cancelarCadastro(self):
	  self.lblmsg["text"] = " ";
          self.txtnome.delete(0, END)
          self.txtusuario.delete(0, END)
          self.txtsenha.delete(0, END)
	  self.txtconfirmaSenha.delete(0, END)


		



root = Tk()
Application(root)
root.mainloop()
