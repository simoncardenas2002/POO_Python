from bokeh.plotting import figure,output_file,show


if __name__ == '__main__':
    output_file("Graficado_simple.html")
    fig= figure()

    total_val=int(input("Cuantos valores quieres graficar"))
    x_vals=list(range(total_val))
    y_vals=[]

    for x in x_vals:
        val=int(input("Valor Y para {x}"))
        y_vals.append(val)

    fig.line(x_vals,y_vals, line_width=2)
    show(fig)
