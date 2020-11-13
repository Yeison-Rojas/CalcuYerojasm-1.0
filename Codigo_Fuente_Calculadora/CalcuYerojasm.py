import tkinter as tk
from  tkinter import ttk
from tkinter import messagebox

def init_window():
    """
        Esta función configura todo lo relacionado con la interfaz grafica
        """
    window=tk.Tk()
    window.title('CalcuYerojasm 1.0')
    window.geometry('450x280')

    calcu = tk.PhotoImage(file='img_calcu.png')
    bien = tk.Label(window, image=calcu)
    bien.grid(column=0, row=0)
    label= tk.Label(window, text='Calculadora', font=('Adobe Fan Heiti Std B', 15))
    label.grid(column=1, row=0)
    entrada1= tk.Entry(window, width=10)
    entrada2= tk.Entry(window, width=10)

    calculin = tk.PhotoImage(file='img_calcu.png')
    bienvenido = tk.Label(window, image=calculin)
    bienvenido.grid(column=2, row=0)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero:', font=('Adobe Fan Heiti Std B', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Adobe Fan Heiti Std B', 10))
    label_entrada2.grid(column = 0, row = 2)

    label_operador= tk.Label(window, text='Escoja un operador', font=('Adobe Fan Heiti Std B', 10))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado= tk.Label( window, text='Resultado: ', font=('Adobe Fan Heiti Std B',15))
    label_resultado.grid(column=0, row=5)
    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          label_resultado,
                          entrada1.get(), entrada2.get(),
                          combo_operadores.get()),
                      text='Calcular',
                      bg="purple",
                      fg="white"
                      )

    etiqueta= tk.Label(window)
    etiqueta.grid(column=1, row=10)

    boton.grid(column=1, row=4)
    radio1= tk.Radiobutton(window, text='Te gusto?', value=1,  command=lambda:presionar(etiqueta),
                           bg='sky blue', fg='black')
    radio1.grid(column = 0, row =8)
    radio2 = tk.Radiobutton(window, text='No te gusto?', value=2, command=lambda:(presionar_no(etiqueta), mensaje()),
                            bg='sky blue', fg='black')
    radio2.grid(column=2, row=8)
    window.mainloop()
def presionar(e):
    """
        Es la función que responde al marcar un RadioButton

        :param tk.Label e : es la etiqueta en donde se configurara el texto
        """
    e.configure(text = "¡GRACIAS! ", font=('Imprint MT Shadow', 20))
def presionar_no(e):
    """
        Es la función que responde al marcar un RadioButton

        :param tk.Label e : es la etiqueta en donde se configurara el texto
        """
    e.configure(text = "El virus es broma, \nEstamos mejorando", font=('Imprint MT Shadow', 12) )
def mensaje():
    """Muestra una caja de mensaje"""

    messagebox.showerror("JaJAJaJA", "Esto es un virus ahora su computador esta dañado")

def calculadora(num1, num2, operador):
    """
        Hace la operación indicada
        :param float num1 : primer número para operar
        :param float num2 : segundo número para operar
        :param ttk.combobox operador: define cual es la operación a realizar
            """

    if operador ==  '+':
        resultado = num1 + num2
    elif operador ==  '-':
        resultado = num1 - num2
    elif operador ==  '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round ((num1 / num2), 2)
    else:
        resultado= num1**num2
    return resultado

def click_calcular(label, num1, num2, operador):
    """
        configura el resultado en pantalla
        :param tk.Label label : Es la etiqueta donde se pondrá el resultado
        :param int num1 : primer número para operar
        :param int num2 : segundo número para operar
        :param ttk.combobox operador: define cual es la operación a realizar
         """

    valor1= float(num1)
    valor2= float(num2)
    res= calculadora(valor1, valor2, operador)
    label.configure(text = 'Resultado: '+ str(res))

def main():
    """
        Inicia el programa
        """
    init_window()

main()