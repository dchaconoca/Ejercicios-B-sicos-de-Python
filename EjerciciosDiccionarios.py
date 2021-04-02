#################################
##### MANEJO DE DICCIONARIOS ####
#################################

torta = {
    "mantequilla":200,
    "azucar":150,
    "huevos":3,
    "harina":3
}

def mostrarIngredientes(plato):
    i = 0
    print(len(plato))
    
    while i <= len(plato):
        ingrediente = plato.item(i)
        print(ingrediente)
        i += 1






###############
##### MAIN ####
###############

mostrarIngredientes(torta)
