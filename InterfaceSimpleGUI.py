import PySimpleGUI as psg
import sympy
import numbers

input = psg.Input(key='input')
multiline = [psg.Multiline(size=(100, 20),  reroute_stdout=True, write_only=True, 
                           disabled=True, k='multiline', autoscroll=True)]
checkbox30 = [psg.Checkbox(text= "30%", key='checkbox30')]

layout = [[multiline],[input],[checkbox30]]

window = psg.Window('Calculo',layout,size=(250,400), finalize= True)
window['input'].bind('<Return>', 'ENTER')

while True:
    event,values = window.read()
     
    if event == "input" + "ENTER":
        
        check_letters = any(c.isalpha() for c in values['input'])
        if check_letters ==True :
            print("Digite Apenas Números")
        else:
            if values['input'] == '':
                print('Digite Algum Valor')
            else:
                if "," in values['input']:
                    b = values['input'].replace(",",".")
                    y = float(b)
                else:
                    y = float(values['input'])

                soma5 = y + (y* 5/100 )

                if values['checkbox30'] == True:
                    somavista = soma5 + (soma5* 30/100)
                else:
                    somavista = soma5 + (soma5* 35/100)
                    
                print(values['input'],'=')
                print("Á vista:",somavista)
            
                x = sympy.Symbol("x")
                equacao = sympy.Eq(x - 0.1 * x, somavista)
                resultado = sympy.solve([equacao], (x), set = True)
                stringconv = str(resultado[1])
                stringcut = stringconv[2:18]
                floatmak = float(stringcut)
                print("Cartão:",floatmak,"\n")


    if event == psg.WINDOW_CLOSED:
        break
window.close