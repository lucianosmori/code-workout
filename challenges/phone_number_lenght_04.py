class Solution:
    def main(self, numbers=list[int]):
        for number in numbers:
            print(self.validate_numbers(number))
        

    def validate_numbers(self, number) -> str:
        if self.validate_number_lenght(number) and self.starts_with(number):
            return "YES"
        else:
            return "NO"

    def validate_number_lenght(self, number=int) -> bool:
        return True if len(str(number)) == 10 else False
    
    def starts_with(self, number=int) -> bool:
        legit_numbers = [7,8,9]
        try:
            number = [int(x) for x in str(number)] # map(int, str(num))
            # convert int into str, then a list of ints
            for legit in legit_numbers:
                if number[0] == legit:
                    return True
        except Exception:
            return False            
        else: 
            return False


if __name__ == "__main__":    
    x = list(map(int, input("Enter multiple values: ").split()))
    #x = ["8F54698745", 8991231235, 9991231235, 1991231235]
    s = Solution()
    s.main(x)
