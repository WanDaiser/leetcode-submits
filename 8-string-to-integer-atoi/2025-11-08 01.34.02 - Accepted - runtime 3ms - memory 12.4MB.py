class Solution(object):
    def myAtoi(self, s):
        i, n, sign, num = 0, len(s), 1, 0

        # Başındaki boşlukları geç
        while i < n and s[i] == ' ':
            i += 1

        # İşaret kontrolü
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Rakamları oku
        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            # Overflow kontrolü (önceden)
            if num > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1
            num = num * 10 + digit
            i += 1

        return sign * num
