"""
docstring


"""

var = 100500

print('hello')

def factorial(number):
  """
    Факториал, принимает целое (HW) / натуральное число


    Homework
    - Посмотрите какие виде рекурсивных функций бывают
  """
  if type(number) is int:
    if number >= 1:
        return number * factorial(number-1)
    elif number == 0:
        return 1


if __name__ == '__main__':
    
    print(__name__)
    print('Только с помощью интерпретатора!')

    def test_bigger_one():
        assert factorial(1) is 1, "факториал от {}".format(-1) 

    def test_negative_val():
        assert factorial(-1) is None,  "факториал от {}".format(-1)

    def test_float_val(n):
        assert factorial(n) is None,  f"факториал от {n} = {factorial(n)}"
  
    test_bigger_one()
    test_negative_val()
    test_float_val(1.0)


  # print(factorial(3.))