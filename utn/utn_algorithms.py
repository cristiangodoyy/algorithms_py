"""
Ingresar 3 valores en 3 variables X,Y y Z. Se desea obtener una rotación de sus
valores, es decir que el contenido de Z pase a X, el contenido de X pase a Y, y el
contenido de Y pase a Z. Se debe mostrar las variables X, Y y Z con sus valores
originales y mostrar X, Y y Z con los valores luego de la rotación. 
"""

import random


def rotation_values():
    x = 4
    y = 87
    z = 1

    print(f'Valores originales: x: {x} y: {y} z: {z}')

    aux = x

    x = z   # contenido de Z pase a X
    z = y   # el contenido de Y pase a Z
    y = aux # el contenido de X pase a Y

    print(f'Valores cambiados: x: {x} y: {y} z: {z}')


def determine_lower():
    """
    Determinar si el primero de un conjunto de tres numeros dados, es menor que los otros dos.
    """ 
    first = 1
    second = 50
    third = 46

    if first < second and first < third:
        print(f'First number {first} is less than second {second} and third {third}')
    else:
        print(f'First number {first} is not less than second {second} and third {third}')


def numbers_in_crecent_input():
    """
	Ingresar 3 números enteros distintos. Determinar si ingresaron en forma creciente.
    """
    n1 = 1
    n2 = 4
    n3 = 3
    
    if n1 < n2 and n2 < n3:
        print('Ingresaron en forma creciente')
    else:
        print('No ingresaron en forma creciente')


def three_letters_alphabeticall_order():
    """
    Ingresar 3 letras mayúsculas y mostrarlas alfabéticamente
    """
    let1 = 'b'
    let2 = 'c'
    let3 = 'a'
    
    if let1 < let2 and let2 < let3:
        print(let1, let2, let3)
    elif let1 < let3 and let3 < let2:
        print(let1, let3, let2)
    elif let2 < let1 and let1 < let3:
        print(let2, let1, let3)
    elif let2 < let3 and let3 < let1:
        print(let2, let3, let1) 
    elif let3 < let2 and let2 < let1:
        print(let3, let2, let1)
    elif let3 < let1 and let1 < let2:
        print(let3, let1, let2)


def read_25_numeric_values():
    """
    Leer 25 valores numericos y exhibir el cuadrado de cada uno de ellos 
    """
    for i in range(1, 26):
        print(f'Number: {i}. Square: {i*i}')


def sum_first_natural_numbers():
    """
    Sumar los primeros 100 números enteros. Mostrar su suma. 
    """
    sum = 0
    for i in range(1, 101):
        sum += i

    print(sum)


def natural_numbers_including_extremes():
    """
    Dado dos numeros. Generar y exhibir todos los numeros que hay entre ellos en secuencia 
    ascendente incluyendo los extremos.
    """
    n1 = 30
    n2 = 40
    
    if n1 < n2:
        for number in range(n1, n2+1):
            print(number)
    else:
        print(f'n1: {n1} is not a less than n2: {n2}')


def determine_maximun_minimun():
    """
    Dada una lista de 93 numeros, determinar e informar el valor máximo y el valor 
    mínimo y la posición en el que fueron ingresado.
    """
    
    pos_max = 0
    pos_min = 0
    val_max = 0
    val_min = 0
    
    for position in range(1, 94):
        number = random.randint(1, 100)
        
        if position == 1:
            val_max = number
            pos_max = position
            val_min = number
            pos_min = position
            continue
        
        if number > val_max:
            val_max = number
            pos_max = position
            
        if number < val_min:
            val_min = number
            pos_min = position  

    print(f'Max value: {val_max} Max position: {pos_max}. Min value: {val_min} Min position: {pos_min}')


def detrmine_silaba_pa():
    """
    Se cuenta con un texto de 190 caracteres. Determinar cuantas veces aparece la sílaba “pa”.
    """
    text = "fadsfdsfsaapfasdfdsafpaadfdfapsvvcxzpa"
    count = 0
    
    for i in range(len(text)):
        char = text[i]
        if char == 'p':
            if text[i+1] == 'a':
                count += 1
    print(f'Count veces that pa silabe find: {count}')            


def enter_sequence_character():
    """
    Ingresar una secuencia ordenada alfabéticamente de letras con repeticiones. 
    Informar cada carácter y la cantidad de veces que aparece en la lista. 
    La secuencia finaliza con un *
    """
    #sequence = 'fvcxoijgremeeenlekrtaaaaalvlfskmlckmdllklaffnqieqfiueilnlcdc'
    sequence = 'aaabbbBBBBCCCCzzzzz'
    
    counter = {}
    for letter in sequence:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
        
    print(f'Sequence counter: {counter}')


def number_to_sum():
    """
    Se dispone de un conjunto de números enteros positivos. 
    Determinar cuántos números al menos se deben sumar, desde el primero que ingresa 
	en adelante, para alcanzar un resultado que sea mayor que un número N 
    ingresado previamente.
    """
    pass
    
    N = 80
    nums = [80, 1, 1, 5, 15, 20, 8, 9, 24, 25, 10, 15]
    
    counter = 1
    suma = 0
    added_nums = []
    
    for number in nums:
        suma += number
        added_nums.append(number)
        
        if suma > N:
            break
        counter += 1

    print(f'Previou number: {N}. Count nums tu sum: {counter}. Added nums: {added_nums}. Sum array: {sum(added_nums)}')



def frase_contiene_cadena_ignore_case():
    """
    Encontrar cuantas veces esta la cadena "Vivo en Rosario" en la frase dada en 
    la variable txt. 
    Ignorando si la frase está en mayusculas o minusculas en el texto dado.
    
    System.out.println(txt);
		System.out.println( txt.toLowerCase().indexOf(frase.toLowerCase()) );
		System.out.println( txt.toLowerCase().indexOf(frase.toLowerCase())+frase.length() );
		System.out.println(frase.length());
		//txt.indexOf(frase): devuelve el numero de indice cuando comienza la cadena frase si ocurre en la cadena txt
		while ( txt.toLowerCase().indexOf(frase.toLowerCase() ) > -1 ) { //En el caso de que no encuentre la cadena, indexOf devolverá el valor -1.
			txt = txt.substring( txt.toLowerCase().indexOf(frase.toLowerCase())+frase.length(), txt.length() );
			System.out.println(txt+"\n");
			System.out.println( txt.toLowerCase().indexOf(frase.toLowerCase()) );
			System.out.println( txt.toLowerCase().indexOf(frase.toLowerCase())+frase.length() );
			System.out.println(frase.length());
			count++;
		}
		System.out.println("Cantidad de veces que aparece la frase vivo en rosario omitiendo may y min: "+count);
    
    """
    txt = "Me llamo pepe parada. Vivo en Rosario. Ayer me mude a villa constitucion. Vivo en Rosario. vivo en Rosario. vivo en rosario. Vivo en rosario"
    frase = "Vivo en Rosario"
    count = 0
    
    txt_lower = txt.lower()
    txt_len = len(txt) # indice del final del texto mas uno
    frase_len = len(frase)  # 15
    frase_lower = frase.lower()  # 
    
    while txt_lower.find(frase_lower) > -1:
        print(txt_lower.find(frase_lower))
        print(frase_len + txt_lower.find(frase_lower))
        txt_lower = txt_lower[ txt_lower.find(frase_lower) + frase_len : txt_len]
        print(txt_lower)
        count += 1
    
    print(count)


if __name__ == '__main__':
    # rotation_values()
    # determine_lower()
    # numbers_in_crecent_input()
    # three_letters_alphabeticall_order()
    # read_25_numeric_values()
    # sum_first_natural_numbers()
    # natural_numbers_including_extremes()
    # determine_maximun_minimun()
    # detrmine_silaba_pa()
    # enter_sequence_character()
    # number_to_sum()
    frase_contiene_cadena_ignore_case()
