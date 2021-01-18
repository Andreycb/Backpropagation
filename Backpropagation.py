import math
import csv
import os
import numpy as np
import click

def Menu():
        print("***************************Trabalho de IA***************************")
        print("* Andrey Cunha Barreira de Araujo                                  *")
        print("* 1 -> Alterar valor da camada oculta                              *")
        print("* 2 -> Informar função de transferencia                            *")
        print("* 3 -> Informar condição de parada                                 *")
        print("* 4 -> Treinar                                                     *")
        print("* 5 -> Testar                                                      *")
        print("* 0 -> Sair                                                        *")
        print("********************************************************************\n")

        opc = int(input())
        
        return opc

def read_csv(filename):
        try:
                line = []
                with open(filename, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                                line.append(row)
        except FileNotFoundError:
                logger.error(f'Arquivo nao foi encontrado: {filename}')

        return line

def len_hidden_layer():
        print('Digite a quantidade de neuronios da camada oculta:')
        hidden = int(input())

        return hidden

def type_metod():
                print("********************************************************************")
                print("* 1 -> Logística                                                   *")
                print("* 2 -> Tangente Hiperbólica                                        *")
                print("********************************************************************\n")

                typemet = int(input())

                return typemet

def iterations():
                print("********************************************************************")
                print("* 1 -> Por iterações                                               *")
                print("* 2 -> Por erro limite                                             *")
                print("********************************************************************\n")

                typeit = int(input())

                return typeit

#quantidade de neuronio camada de saida
def get_number_class(filecsv):
        max_class = []
        for i in filecsv:
                max_class.append(i['classe'])

        return max(max_class)

#quantidade de neuronio camada de entrada
def get_number_atributes(filecsv):
        leng = len(filecsv[0].keys())

        return leng-1

#quantidade de neuronio camada oculta
def hidden_layer(value_in, value_ou):
        value = int(value_in) * int(value_ou)
        hidden = math.sqrt(value)

        return int(hidden)

@click.command()
def run():
        Menu()
        records = read_csv('C:\\Users\\Andrey\\Desktop\\UNESP\\IA\\dataset\\treinamento.csv')
        inp = get_number_atributes(records)
        out = get_number_class(records)
        hidden = (hidden_layer(inp,out)) #esse valor pode ser alterado

if __name__ == '__main__':
    run()