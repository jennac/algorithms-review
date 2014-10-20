# Programming Assignment 1: Implement Inversion Counter 
#  using merge sort as a base

def sort(A):

    if len(A) == 1:
        return A, 0
    else:
        left, linv = sort(A[:len(A)/2])
        right, rinv = sort(A[len(A)/2:])

        i = 0
        j = 0
        invs = 0 + linv + rinv
        output = []
        
        for x in range(len(A)):
            try:
                if left[i] < right[j]:
                    output.append(left[i])
                    i += 1
                else:
                    output.append(right[j])
                    j += 1
                    invs += len(left) - i
            except IndexError:
                break
        
        while not i == len(left):
            output.append(left[i])
            i += 1
        while not j == len(right):
            output.append(right[j])
            j += 1

        return output, invs


def get_data(filename):

    with open(filename, 'r') as f:
        A = f.readlines()
        A = [int(a.strip('\n')) for a in A]
    
    return A


def main():
    
    A = get_data('IntegerArray.txt')
    sorted_a, invs = sort(A)
    print 'FINAL: {}'.format(invs)

if __name__ == '__main__':
    main()
