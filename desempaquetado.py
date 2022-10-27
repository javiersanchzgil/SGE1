def calc_4_sum(n1,n2,n3,n4):
    return n1 + n2 + n3 + n4

def cal_var_sum(*factors):
    return sum(factors)

def main():
    ln = [1, 2, 3, 4]
    res_4_sum = calc_4_sum(*ln)
    print(res_4_sum)
    #El asterisco desempaqueta el array, sin el * da error y puedes meter todos los números que quieras
    print(cal_var_sum(*ln,7))

if __name__ == "__main__":
    print("Comienzo tarea")
    main()
    print ("Fin tarea")