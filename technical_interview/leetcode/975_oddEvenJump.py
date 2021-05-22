class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        """
        start from any index in array. move i to j.
        
        odd_number_jump. larger or equal to current value. smallest of all possible values.
        even_number_jump. smaller or equal to current values. largest of all possible values.
        
        inputs: current_index, array
        output: next_index or -1 (if there's no where to move)
        
        cnt = 0
        if cnt % 2 == 1 => odd_number_jump
        else => even_number_jump
        
        termination condition for the jump functions:
        1. reaches the end of array. return 1
        2. there is no where to move. return 0
        
        
        """
        def jump(current_i, array, jump_type):
            final_val = None
            out_idx = 0 
            current_val = array[current_i]

            if jump_type == 'odd':
                next_jump_type = 'even'
            else:
                next_jump_type = 'odd'
            
            for i, v in enumerate(array[current_i + 1:]):
                if jump_type == 'odd' and v >= current_val and (final_val is None or final_val > v):
                    final_val = v
                    out_idx = i + current_i + 1
                elif jump_type == 'even' and v <= current_val and (final_val is None or final_val < v):
                    final_val = v
                    out_idx = i + current_i + 1
            if out_idx == 0:
                return 0
            if out_idx in cache[next_jump_type].keys():
                return cache[next_jump_type][out_idx]
            else:
                cache[next_jump_type][out_idx] = jump(out_idx, array, next_jump_type)
            return cache[next_jump_type][out_idx]

        
        good_start_cnt = 0
        cache = {
            'even': {len(arr)-1: 1},
            'odd': {len(arr)-1: 1},
        }
        
        for i in range(len(arr)-1, -1, -1):
            if i in cache['odd'].keys():
                good_start_cnt += cache['odd'][i]
            else:
                good_start_cnt += jump(i, arr, 'odd')
        # good_start_cnt = jump(4, arr, 'odd')
        return good_start_cnt
    
    
