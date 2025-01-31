import sys
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QApplication,QLayout

class finalizar(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 200, 550, 300)
        self.setWindowTitle("Finalizar Venda")

        
        self.layout_v = QVBoxLayout()
        


        self.label_fim = QLabel("Finalizar Venda")
        self.label_fim.setStyleSheet("QLabel{background-color:green}font-size:22pt,color:red")
        self.layout_v.addWidget(self.label_fim)
        
        #layout vertical
        self.label_hori = QLabel()
        self.label_hori.setStyleSheet("QLabel{background-color:blue}font-size:22pt,color:red")
        self.layout_v.addWidget(self.label_hori)
        
        #layout horizontal
        self.layout_h_total = QHBoxLayout()
        self.label_hori.setLayout(self.layout_h_total)

        
        #ceh coluna da esquerda horizontal 
        self.label_ceh = QLabel()
        #criar um layout vertical esquerda###########################################################################################
        self.layout_v_vertical = QVBoxLayout()

########################################################Total  Venda############################################################################
        #label para armazenar o texto total de venda e a caixa total de venda , ou seja , ira guardar uma nova label e uma lineedit
        self.label_total_venda =QLabel()


        #criar layout horizontal para a label total_venda e a lineedit
        self.layout_h_total_venda = QHBoxLayout()

        #criar a label que tera o texto total de vendas
        self.label_venda = QLabel("Total de venda")
        #criar a lineedit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 0,00")

        #adicionar a label_venda e a edit_venda ao layout horizontal venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)
        #adicionar o layout_h_venda a laabel_total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)


        #adicionar a label_total_venda ao layout_v_ esquerda
        self.layout_v_vertical.addWidget(self.label_total_venda)

###################################### DESCONTO #################################################################################
        self.label_desconto =QLabel()


        #criar layout horizontal para a label total_venda e a lineedit
        self.layout_h_desconto = QHBoxLayout()

        #criar a label que tera o texto total de vendas
        self.label_desc = QLabel("Total de desc")
        #criar a lineedit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")

        #adicionar a label_desc e a edit_desc ao layout horizontal desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)
        #adicionar o layout_h_venda a laabel_desconto
        self.label_desconto.setLayout(self.layout_h_desconto)


        #adicionar a label_desconto ao layout_v_ esquerda
        self.layout_v_vertical.addWidget(self.label_desconto)

        #############################################################ACRÉCIMO###########################################
        self.label_acrecimo =QLabel()


        #criar layout horizontal para a label total_venda e a lineedit
        self.layout_h_acrecimo = QHBoxLayout()

        #criar a label que tera o texto total de vendas
        self.label_acreci = QLabel("Acrécimo")
        #criar a lineedit que recebe o total de acreci
        self.edit_acreci = QLineEdit("R$ 0,00")

        #adicionar a label_acreci e a edit_acreci ao layout horizontal acreci
        self.layout_h_acrecimo.addWidget(self.label_acreci)
        self.layout_h_acrecimo.addWidget(self.edit_acreci)
        #adicionar o layout_h_venda a laabel_acrecimo
        self.label_acrecimo.setLayout(self.layout_h_acrecimo)


        #adicionar a label_acrecimo ao layout_v_ esquerda
        self.layout_v_vertical.addWidget(self.label_acrecimo)

        ############################################### TOTAL LIQUIDO ##################################################
        self.label_total_liquido =QLabel()


        #criar layout horizontal para a label total_venda e a lineedit
        self.layout_h_total_liquido = QHBoxLayout()

        #criar a label que tera o texto total de vendas
        self.label_totalliq = QLabel("Total de Liquido")
        #criar a lineedit que recebe o total de totalliq
        self.edit_totalliq = QLineEdit("R$ 0,00")

        #adicionar a label_totalliq e a edit_totalliq ao layout horizontal totalliq
        self.layout_h_total_liquido.addWidget(self.label_totalliq)
        self.layout_h_total_liquido.addWidget(self.edit_totalliq)
        #adicionar o layout_h_venda a laabel_total_liquido
        self.label_total_liquido.setLayout(self.layout_h_total_liquido)


        #adicionar a label_total_liquido ao layout_v_ esquerda
        self.layout_v_vertical.addWidget(self.label_total_liquido)

        ################################################# TROCO ####################################
        self.label_troco =QLabel()


        #criar layout horizontal para a label total_venda e a lineedit
        self.layout_h_troco = QHBoxLayout()

        #criar a label que tera o texto total de vendas
        self.label_troc = QLabel("Troco")
        #criar a lineedit que recebe o total de troc
        self.edit_troc = QLineEdit("R$ 0,00")

        #adicionar a label_troc e a edit_troc ao layout horizontal troc
        self.layout_h_troco.addWidget(self.label_troc)
        self.layout_h_troco.addWidget(self.edit_troc)
        #adicionar o layout_h_venda a laabel_troco
        self.label_troco.setLayout(self.layout_h_troco)


        #adicionar a label_troco ao layout_v_ esquerda
        self.layout_v_vertical.addWidget(self.label_troco)


        self.label_ceh.setLayout(self.layout_v_vertical)


        self.label_ceh.setStyleSheet("QLabel{background-color:grey}font-size:22pt,color:red")
        self.layout_h_total.addWidget(self.label_ceh)



       
        #coluna da direita horizontal ###################################################################################################################
        self.label_cdh = QLabel()
        self.label_cdh.setStyleSheet("QLabel{background-color:white}font-size:22pt,color:red")
        self.layout_h_total.addWidget(self.label_cdh)


        self.label_rodape = QLabel()
        self.label_rodape.setStyleSheet("QLabel{background-color:yellow}font-size:22pt,color:red")
        self.layout_v.addWidget(self.label_rodape)

       

      

        self.setLayout(self.layout_v)


app = QApplication(sys.argv)
tela = finalizar()
tela.show()
app.exec()
