from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co4 = "#403d3d"  # letra
co6 = "#003452"  # azul

def conectar_banco():
    conn = sqlite3.connect('avaliacoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avaliacoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(255),
                    localizacao REAL,
                    tamanho_do_imovel REAL,
                    aluguel REAL,
                    segurança REAL,
                    estrutura REAL,
                    beleza REAL,
                    postos_de_saude REAL,
                    escola REAL,
                    mercado REAL,
                    hospital REAL,
                    area_verde REAL,
                    localizacao_two REAL,
                    tamanho_do_imovel_two REAL,
                    aluguel_two REAL,
                    segurança_two REAL,
                    estrutura_two REAL,
                    beleza_two REAL,
                    postos_de_saude_two REAL,
                    escola_two REAL,
                    mercado_two REAL,
                    hospital_two REAL,
                    area_verde_two REAL,
                    avaliacao_final REAL                   
        )
    ''')
    conn.commit()
    return conn, cursor

# Criação da aplicação
class AvaliadorImoveisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliador de Locação de Imóveis")
        self.root.geometry("620x620")
        self.root.configure(background=co1)
        self.root.resizable(width=FALSE, height=FALSE)

        self.conn, self.cursor = conectar_banco()

        self.criar_widgets()
    # Criação dos frames principais
    def criar_widgets(self):

        self.frame_logo = Frame(self.root, width=620, height=52, bg=co6)
        self.frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

        self.frame_dados = Frame(self.root, width=850, height=65, bg=co1)
        self.frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

        self.frame_main = Frame(self.root, width=850, height=200, bg=co1)
        self.frame_main.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

        self.frame_detalhes = Frame(self.frame_main, width=425, height=200, bg=co1)
        self.frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)
        
        self.frame_detalhes_two = Frame(self.frame_main, width=425, height=200, bg=co1)
        self.frame_detalhes_two.grid(row=4, column=0, pady=0, padx=280, sticky=NSEW)

        self.app_logo = Image.open('img/house.png')
        self.app_logo = self.app_logo.resize((50, 50))
        self.app_logo = ImageTk.PhotoImage(self.app_logo)
        self.app_lg = Label(self.frame_logo, image=self.app_logo, text="Cadastro de imóveis", width=850, compound=LEFT, relief=RAISED, anchor=NW, font='Ivy 15 bold', bg=co6, fg=co1)
        self.app_lg.place(x=0, y=0)


        self.app_bottun_cadastro = Image.open('img/adicionar.png')
        self.app_bottun_cadastro = self.app_bottun_cadastro.resize((18, 18))
        self.app_bottun_cadastro = ImageTk.PhotoImage(self.app_bottun_cadastro)
        self.app_cadastro = Button(self.frame_dados, command=self.cadastramento, image=self.app_bottun_cadastro, text="Cadastro", width=100, compound=LEFT, relief=RAISED, overrelief=RIDGE, font='Ivy 11', bg=co1, fg=co0)
        self.app_cadastro.place(x=10, y=30)

        self.app_bottun_media = Image.open('img/lista.png')
        self.app_bottun_media = self.app_bottun_media.resize((18,18))
        self.app_bottun_media = ImageTk.PhotoImage(self.app_bottun_media)
        self.app_media = Button(self.frame_dados, command=self.lista, image=self.app_bottun_media, text="Lista", width=100, compound=LEFT, relief=RAISED, overrelief=RIDGE , font='Ivy 11', bg= co1, fg=co0)
        self.app_media.place(x=123, y=30)
    
        self.criar_campos()
    
    # Criação dos frames de conteudo
    def criar_campos(self):

        self.frame_detalhes = Frame(self.frame_main, width=425, height=200, bg=co1)
        self.frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)  
        
        self.frame_detalhes_two = Frame(self.frame_main, width=425, height=200, bg=co1)
        self.frame_detalhes_two.grid(row=4, column=0, pady=0, padx=280, sticky=NSEW) 

        tk.Label(self.frame_detalhes, text=" Marido ", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4).grid(row=0, column=0)

        # notas 1
        tk.Label(self.frame_detalhes, text="link do imóvel: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=1, column=0)
        self.entry_nome = tk.Entry(self.frame_detalhes)
        self.entry_nome.grid(row=1, column=1)
        
        tk.Label(self.frame_detalhes, text="localização: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=2, column=0)
        self.entry_localizacao = tk.Entry(self.frame_detalhes)
        self.entry_localizacao.grid(row=2, column=1)
        
        tk.Label(self.frame_detalhes, text="tamanho do imóvel: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=3, column=0)
        self.entry_tamanho_do_imovel = tk.Entry(self.frame_detalhes)
        self.entry_tamanho_do_imovel.grid(row=3, column=1)

        tk.Label(self.frame_detalhes, text="aluguel: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=4, column=0)
        self.entry_aluguel = tk.Entry(self.frame_detalhes)
        self.entry_aluguel.grid(row=4, column=1)

        tk.Label(self.frame_detalhes, text="segurança: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=5, column=0)
        self.entry_seguranca = tk.Entry(self.frame_detalhes)
        self.entry_seguranca.grid(row=5, column=1)

        tk.Label(self.frame_detalhes, text="beleza: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=6, column=0)
        self.entry_beleza = tk.Entry(self.frame_detalhes)
        self.entry_beleza.grid(row=6, column=1)

        tk.Label(self.frame_detalhes, text="postos de saúde: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=7, column=0)
        self.entry_postos_de_saude = tk.Entry(self.frame_detalhes)
        self.entry_postos_de_saude.grid(row=7, column=1)
        
        tk.Label(self.frame_detalhes, text="escola: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=8, column=0)
        self.entry_escola = tk.Entry(self.frame_detalhes)
        self.entry_escola.grid(row=8, column=1)

        tk.Label(self.frame_detalhes, text="mercado: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=9, column=0)
        self.entry_mercado = tk.Entry(self.frame_detalhes)
        self.entry_mercado.grid(row=9, column=1)

        tk.Label(self.frame_detalhes, text="hospital: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=10, column=0)
        self.entry_hospital = tk.Entry(self.frame_detalhes)
        self.entry_hospital.grid(row=10, column=1)

        tk.Label(self.frame_detalhes, text="area verde: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=11, column=0)
        self.entry_area_verde = tk.Entry(self.frame_detalhes)
        self.entry_area_verde.grid(row=11, column=1)

        # notas 2
    
        tk.Label(self.frame_detalhes_two, text=" Esposa ", anchor=NW, font="Ivy 10 bold", bg=co1, fg=co4).grid(row=0, column=0)
        
        tk.Label(self.frame_detalhes_two, bg=co1, fg=co4).grid(row=1, column=0)

        tk.Label(self.frame_detalhes_two, text="localização: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=2, column=0)
        self.entry_localizacao_two = tk.Entry(self.frame_detalhes_two)
        self.entry_localizacao_two.grid(row=2, column=1)
        
        tk.Label(self.frame_detalhes_two, text="tamanho do imóvel: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=3, column=0)
        self.entry_tamanho_do_imovel_two = tk.Entry(self.frame_detalhes_two)
        self.entry_tamanho_do_imovel_two.grid(row=3, column=1)

        tk.Label(self.frame_detalhes_two, text="aluguel: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=4, column=0)
        self.entry_aluguel_two = tk.Entry(self.frame_detalhes_two)
        self.entry_aluguel_two.grid(row=4, column=1)

        tk.Label(self.frame_detalhes_two, text="segurança: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=5, column=0)
        self.entry_seguranca_two = tk.Entry(self.frame_detalhes_two)
        self.entry_seguranca_two.grid(row=5, column=1)

        tk.Label(self.frame_detalhes_two, text="beleza: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=6, column=0)
        self.entry_beleza_two = tk.Entry(self.frame_detalhes_two)
        self.entry_beleza_two.grid(row=6, column=1)

        tk.Label(self.frame_detalhes_two, text="postos de saúde: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=7, column=0)
        self.entry_postos_de_saude_two = tk.Entry(self.frame_detalhes_two)
        self.entry_postos_de_saude_two.grid(row=7, column=1)
        
        tk.Label(self.frame_detalhes_two, text="escola: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=8, column=0)
        self.entry_escola_two = tk.Entry(self.frame_detalhes_two)
        self.entry_escola_two.grid(row=8, column=1)

        tk.Label(self.frame_detalhes_two, text="mercado: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=9, column=0)
        self.entry_mercado_two = tk.Entry(self.frame_detalhes_two)
        self.entry_mercado_two.grid(row=9, column=1)

        tk.Label(self.frame_detalhes_two, text="hospital: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=10, column=0)
        self.entry_hospital_two = tk.Entry(self.frame_detalhes_two)
        self.entry_hospital_two.grid(row=10, column=1)

        tk.Label(self.frame_detalhes_two, text="area verde: ", anchor=NW, font="Ivy 10", bg=co1, fg=co4).grid(row=11, column=0)
        self.entry_area_verde_two = tk.Entry(self.frame_detalhes_two)
        self.entry_area_verde_two.grid(row=11, column=1)
        
        self.app_save = []
       
        self.save = Image.open('img/disk.png')
        self.save = self.save.resize((18,18))
        self.save = ImageTk.PhotoImage(self.save)
        self.app_save.append(self.save)
        self.app_save = tk.Button(self.frame_detalhes, image=self.app_save[-1], command=self.salvar, width=100, font='Ivy 11', bg= co1, fg=co0).grid(row=13, column=0)

    # Função de salvamento de dados       
    def salvar(self):
        
        try:
            
            self.campos_numericos = [
                (self.entry_localizacao, "localização"),
                (self.entry_tamanho_do_imovel, "tamanho do imóvel"),
                (self.entry_aluguel, "aluguel"),
                (self.entry_seguranca, "segurança"),
                (self.entry_beleza, "beleza"),
                (self.entry_postos_de_saude, "postos de saúde"),
                (self.entry_escola, "escola"),
                (self.entry_mercado, "mercado"),
                (self.entry_hospital, "hospital"),
                (self.entry_area_verde, "área verde"),
                (self.entry_localizacao_two, "localização (Esposa)"),
                (self.entry_tamanho_do_imovel_two, "tamanho do imóvel (Esposa)"),
                (self.entry_aluguel_two, "aluguel (Esposa)"),
                (self.entry_seguranca_two, "segurança (Esposa)"),
                (self.entry_beleza_two, "beleza (Esposa)"),
                (self.entry_postos_de_saude_two, "postos de saúde (Esposa)"),
                (self.entry_escola_two, "escola (Esposa)"),
                (self.entry_mercado_two, "mercado (Esposa)"),
                (self.entry_hospital_two, "hospital (Esposa)"),
                (self.entry_area_verde_two, "área verde (Esposa)")
            ]
            
            nome = self.entry_nome.get()
            if not nome:
                messagebox.showerror("Erro", "Por favor, preencha o campo 'Link do Imóvel'.")
                return
        
            dados = {}
            for campo, nome_campo in self.campos_numericos:
                    valor = campo.get()
                    if not valor:
                        messagebox.showerror("Erro", f"Por favor, preencha o campo '{nome_campo}'.")
                        return
                    try:
                        valor_float = float(valor)
                        if not (0 <= valor_float <= 10):
                            messagebox.showerror("Erro", f"O campo '{nome_campo}' deve ser um número entre 0 e 10.")
                            return
                        dados[nome_campo] = valor_float
                    except ValueError:
                        messagebox.showerror("Erro", f"O campo '{nome_campo}' deve ser um número válido.")
                        return
            
            localizacao = dados["localização"]
            tamanho = dados["tamanho do imóvel"]
            aluguel = dados["aluguel"]
            seguranca = dados["segurança"]
            beleza = dados["beleza"]
            saude = dados["postos de saúde"]
            escola = dados["escola"]
            mercado = dados["mercado"]
            hospital = dados["hospital"]
            verde = dados["área verde"]

            localizacao_two = dados["localização (Esposa)"]
            tamanho_two = dados["tamanho do imóvel (Esposa)"]
            aluguel_two = dados["aluguel (Esposa)"]
            seguranca_two = dados["segurança (Esposa)"]
            beleza_two = dados["beleza (Esposa)"]
            saude_two = dados["postos de saúde (Esposa)"]
            escola_two = dados["escola (Esposa)"]
            mercado_two = dados["mercado (Esposa)"]
            hospital_two = dados["hospital (Esposa)"]
            verde_two = dados["área verde (Esposa)"]

            self.cursor.execute('''
                    INSERT INTO avaliacoes (nome, localizacao, tamanho_do_imovel, aluguel, segurança, beleza, postos_de_saude, escola, mercado, hospital, area_verde, localizacao_two, tamanho_do_imovel_two, aluguel_two, segurança_two, beleza_two, postos_de_saude_two, escola_two, mercado_two, hospital_two, area_verde_two)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (nome, localizacao, tamanho, aluguel, seguranca, beleza, saude, escola, mercado, hospital, verde, localizacao_two, tamanho_two, aluguel_two, seguranca_two, beleza_two, saude_two, escola_two, mercado_two, hospital_two, verde_two))
            self.conn.commit()

            if self.entry_nome:
                self.entry_nome.delete(0, tk.END)

            for campo, nome_campo in self.campos_numericos:  
                campo.delete(0, tk.END)                
                
            messagebox.showinfo("Sucesso", "Avaliação salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    #Função de exibição de formulario (C)
    def cadastramento(self):
        for widget in self.frame_detalhes.winfo_children():
            widget.destroy()
            
        self.criar_campos()        
    
    #Função de deletar dados (D)
    def deletar_linha(self, id):
        try:
            if id is None:
                messagebox.showerror("Erro", "ID inválido para exclusão!")
                return
                
            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta linha?")
            if not resposta:
                return

            self.cursor.execute('DELETE FROM avaliacoes WHERE id = ?', (id,))
            self.conn.commit()

            self.lista()   

            messagebox.showinfo("Sucesso", "Linha apagada!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

    #Função de alteração de dados, apenas nome neste caso (U)
    def update_name(self, id):
        janela_secundaria = Toplevel(self.root)
        janela_secundaria.title("Atualizar link do imóvel")
        janela_secundaria.geometry("300x100")
        janela_secundaria.configure(bg=co1)
        janela_secundaria.transient(self.root)
        janela_secundaria.grab_set()
        janela_secundaria.focus_force()

        tk.Label(janela_secundaria, text="Novo link do imóvel:", font="Ivy 10", bg=co1, fg=co4).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        entry_novo_nome = tk.Entry(janela_secundaria)
        entry_novo_nome.grid(row=0, column=1, padx=10, pady=5)

        # Função para salvar o novo nome
        def salvar_nome():
            
            novo_nome = entry_novo_nome.get()

            if not novo_nome:
                messagebox.showerror("Erro", "Por favor, insira um novo nome para o imóvel.")
                return

            try:
                self.cursor.execute(''' UPDATE avaliacoes SET nome = ? WHERE id = ? ''', (novo_nome, id))
                self.conn.commit()

                messagebox.showinfo("Sucesso", "Nome do imóvel atualizado com sucesso!")

                janela_secundaria.destroy()
                
                self.lista()
            
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao atualizar o nome: {str(e)}")

        btn_salvar = Button(janela_secundaria, text="Salvar", command=salvar_nome, font='Ivy 11', bg=co1, fg=co0)
        btn_salvar.grid(row=1, column=0, pady=10)

        btn_fechar = Button(janela_secundaria, text="Cancelar", command=janela_secundaria.destroy, font='Ivy 11', bg=co1, fg=co0)
        btn_fechar.grid(row=1, column=1, pady=10)

    #Função de exibição de rankeamento (R)
    def lista(self):
                
                for widget in self.frame_detalhes.winfo_children():
                    widget.destroy()

                for widget in self.frame_detalhes_two.winfo_children():
                    widget.destroy()    

                self.frame_detalhes = tk.Frame(self.frame_main, bg=co1)
                self.frame_detalhes.place(x=50, y=20, width=500)

                self.canvas = tk.Canvas(self.frame_detalhes)
                self.canvas.grid(row=0, column=0, sticky=NSEW)

                self.scrollbar = tk.Scrollbar(self.frame_detalhes, orient="vertical", command=self.canvas.yview)
                self.scrollbar.grid(row=0, column=1, sticky="ns")
                
                self.canvas.configure(yscrollcommand=self.scrollbar.set)
                
                self.frame_interno = tk.Frame(self.canvas)
                
                self.canvas.create_window((0, 0), window=self.frame_interno, anchor="nw")      

                self.cursor.execute('''
                    SELECT id, nome, localizacao, tamanho_do_imovel, aluguel, segurança, beleza, postos_de_saude, escola, mercado, hospital, area_verde, localizacao_two, tamanho_do_imovel_two, aluguel_two, segurança_two, beleza_two, postos_de_saude_two, escola_two, mercado_two, hospital_two, area_verde_two
                    FROM avaliacoes
                ''')
                casas = self.cursor.fetchall()
                
                casas_com_media = []
                for casa in casas:
                    id = casa[0]
                    nome = casa[1]
                    notas = casa[2:]  
                    media = sum(notas) / len(notas) 
                    casas_com_media.append((id, nome, media))

                casas_com_media.sort(key=lambda x: x[2], reverse=True)
                

                # Exibição dos resultados
                tk.Label(self.frame_interno, text="Ranking de Casas", font="Ivy 15 bold", fg=co4).grid(row=0, column=0, columnspan=2, pady=10)

                tk.Label(self.frame_interno, text="Posição", font="Ivy 10 bold", fg=co4).grid(row=1, column=0, padx=10, pady=5)
                tk.Label(self.frame_interno, text="Nome da Casa", font="Ivy 10 bold", fg=co4).grid(row=1, column=1, padx=10, pady=5)
                tk.Label(self.frame_interno, text="Média", font="Ivy 10 bold", fg=co4).grid(row=1, column=2, padx=10, pady=5)                
                
                self.app_bin = []
                self.app_draw = []
                
                for i, (id, nome, media) in enumerate(casas_com_media, start=1):

                    nome_limitado = nome if len(nome) <= 5 else nome[:5] + "..."

                    tk.Label(self.frame_interno, text=str(i), font="Ivy 10", fg=co4).grid(row=i+1, column=0, padx=10, pady=5)
                    tk.Label(self.frame_interno, text=nome_limitado, font="Ivy 10", fg=co4).grid(row=i+1, column=1, padx=10, pady=5)
                    tk.Label(self.frame_interno, text=f"{media:.2f}", font="Ivy 10", fg=co4).grid(row=i+1, column=2, padx=10, pady=5)
                    
                    self.bin = Image.open('img/bin.png')
                    self.bin = self.bin.resize((15,15))
                    self.bin = ImageTk.PhotoImage(self.bin) 
                    self.app_bin.append(self.bin)
                    tk.Button(self.frame_interno, image=self.app_bin[-1], width=10, command=lambda id=id: self.deletar_linha(id),
                    compound=RIGHT, relief=RAISED, overrelief=RIDGE, bg=co1, fg=co0).grid(row=i+1, column=3, padx=0, pady=5)
                    
                    self.draw = Image.open('img/pencil.png')
                    self.draw = self.draw.resize((15,15))
                    self.draw = ImageTk.PhotoImage(self.draw) 
                    self.app_draw.append(self.draw)
                    tk.Button(self.frame_interno, image=self.app_draw[-1], width=10, command=lambda id=id: self.update_name(id),
                    compound=RIGHT, relief=RAISED, overrelief=RIDGE, bg=co1, fg=co0).grid(row=i+1, column=4, padx=10, pady=5)
                    
                    
                     # Atualizar a região da barra de rolagem e o redimensionamento correto
                self.frame_interno.update_idletasks()
                self.canvas.config(scrollregion=self.canvas.bbox("all"))
                self.frame_detalhes.grid_rowconfigure(0, weight=1)
                self.frame_detalhes.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AvaliadorImoveisApp(root)
    root.mainloop()