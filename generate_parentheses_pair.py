# this iterative approach was investigated but fails 


class Solution(object):
    def generateParenthesis(self, n):

        
        base_case_string = n*"()"
        final_list = []
        clean_list = []

        final_list.append(base_case_string)
        base_case_string_list = list(base_case_string)

        # solve by a technique similar to induction
        for i in range(1, len(base_case_string)-1):
            base_case_string_list[i], base_case_string_list[i+1] = base_case_string_list[i+1], base_case_string_list[i]
            final_list.append((''.join(base_case_string_list)))

        # another iterative loop run
        for i in range(1, len(base_case_string)-2):
            base_case_string_list[i], base_case_string_list[i+1] = base_case_string_list[i+1], base_case_string_list[i]
            final_list.append((''.join(base_case_string_list)))


        # iterative loop to remove duplicates by picking up every other element
        for i in range(0, len(final_list), 2):
            clean_list.append(final_list[i])
        
        if n == 1:
            pass
        else:
            singular_case_string = n*"("+n*")"
            clean_list.append(singular_case_string)
        
        return clean_list



class Solution(object):
    def generateParenthesis(n):
        result_list = []
        def string_constructor(string, open_count, closed_count):
            # backtracks and move deeper in the branch
            if open_count > closed_count:
                return
            # the end of one branch i.e. a basecase
            if open_count == 0 and closed_count ==0:
                result_list.append(string)
                return
            # all those open parentheses should be closed in the isolated case of ((()))
            if open_count == 0:
                string_constructor(string+")", open_count, closed_count-1)
            else:
                string_constructor(string+"(", open_count-1, closed_count)
                string_constructor(string+")", open_count, closed_count-1)
        string_constructor("", n, n)
        return result_list