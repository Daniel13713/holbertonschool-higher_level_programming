#!/usr/bin/python3

################################################################################################
print("------------------------------------[0]----------------------------------------")
################################################################################################
add_integer = __import__("0-add_integer").add_integer
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)


################################################################################################
print("------------------------------------[1]----------------------------------------")
################################################################################################
matrix_divided = __import__("2-matrix_divided").matrix_divided

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix_divided(matrix, 3))
print(matrix)
################################################################################################
print("------------------------------------[2]----------------------------------------")
################################################################################################

################################################################################################
print("------------------------------------[3]----------------------------------------")
################################################################################################
print_square = __import__("4-print_square").print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

################################################################################################
print("------------------------------------[4]----------------------------------------")
################################################################################################
text_indentation = __import__("5-text_indentation").text_indentation

text_indentation(
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres"""
)
print("--------------------------------------")
text_indentation("hola?     que.     tal: si hacemos una ?                      \ncosa")

################################################################################################
print("------------------------------------[5]----------------------------------------")
################################################################################################
max_integer = __import__("6-max_integer").max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))

################################################################################################
print("------------------------------------[6]----------------------------------------")
################################################################################################

################################################################################################
print("------------------------------------[7]----------------------------------------")
################################################################################################
