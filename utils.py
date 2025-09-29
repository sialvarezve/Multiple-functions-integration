def suma(*nums):
    print('sumando')
    nums_for_real = [float(num) for num in nums]
    return sum(nums_for_real)

def resta(*nums):
    print('restando')
    nums_for_real = [float(num) for num in nums]
    result = nums_for_real[0]
    for num in nums_for_real[1:]:
        result -= num
    return result

def mayuscula_a_minuscula(*texts):
    print('convirtiendo a minúsculas')
    texts_for_real = [str(text) for text in texts]
    lower_texts = [text.lower() for text in texts_for_real]
    return lower_texts
