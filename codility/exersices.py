
class BinaryGap:
    """
    https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
    Binary gap(brecha)
    Find longest sequence of zeros in binary representation of an integer.
    Encuentra la secuencia mas larga de ceros en la representacion binaria de un entero.
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded(rodeado) by 
    ones(unos:1's) at both ends(extremos) in the binary representation of N. 
    For example, number 9 has binary representation 1001 and 
    contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: 
    one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of 
    length 1. The number 15 has binary representation 1111 and has no binary gaps.
    
    Write a function:
    
    int solution(int N);
    
    that, given a positive integer N, returns the length of its longest(mas larga) binary gap. The function should return 0 if N 
    doesn't contain a binary gap. For example, given N = 1041 the function should return 5, because N has binary 
    representation 10000010001 and so its longest binary gap is of length 5.
    
    Assume that:

    N is an integer within the range [1..2,147,483,647].
    Complexity:
        expected worst-case time complexity is O(log(N));
        expected worst-case space complexity is O(1).
    """
    
    @staticmethod
    def solution_1(N):
        """
        {} places a variable into a string
        0 takes the variable at argument position 0
        : adds formatting options for this variable (otherwise it would represent decimal 6)
        08 formats the number to eight digits zero-padded on the left
        b converts the number to its binary representation
        :param N: 529=1000010001, 9=1001, 20=10100, 15=1111, 1041= , 15=
        """
        
        if N > 0:
            n_bin_str = '{0:b}'.format(N)
            


if __name__ == '__main__':
    BinaryGap.solution_1(529)


