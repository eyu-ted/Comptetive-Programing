class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_val = {
            "I"     :        1,
            "V"     :        5,
            "X"      :       10,
            "L"      :      50,
            "C"     :        100,
            "D"      :       500,
            "M"      :       1000,
        }
        unique_vals = { "IV":4, "IX":9, "XL": 40, "XC":90, "CD":400, "CM":900 }
        total_value = 0
        index = 1
        end = False
        while index < len(s)+1:
            current_val = s[index-1:index+1]
            if current_val in unique_vals:
                total_value += unique_vals[current_val]
                # if index == len(s)-1:
                #     end = True
                index += 2
            else:
                total_value += symbol_val[s[index-1]]
                index += 1

        # if not end:
        #     total_value += symbol_val[s[-1]]
        
        return total_value

