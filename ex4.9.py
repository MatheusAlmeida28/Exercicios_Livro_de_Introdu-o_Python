#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.


casa = float(input('Qual é o valor da casa a se comprar?: '))
salario = float(input('Qual é o seu salário?: '))
anos_pagar = int(input('Qual a quantidade de anos a pagar?: '))

porcentagem_salario_30 = (salario * 30)/100 

meses_a_pagar = anos_pagar * 12
prestacao = casa/meses_a_pagar


if prestacao > porcentagem_salario_30:
    print('Não foi possivel realizar o empréstimo')
else:
    print(f'Seu emprestimo foi realizado! Valor da prestação R${prestacao:.2f}')

