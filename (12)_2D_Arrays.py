from itertools import chain
if __name__ == '__main__':
    Array = [list(map(int,input().split())) for i in range(6)]
    sum_expand_array = []
    for i in range(0,4):
        for j in range(0,4):
            sum_expand_array.append(sum(list(chain.from_iterable([Array[i][j:j+3],[Array[i+1][j+1]],Array[i+2][j:j+3]]))))
    print(max(sum_expand_array))
