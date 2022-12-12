class Solution:
    def solve(self, sentence, delimiters):
        if not sentence:
            return ""

        i = 0
        delimiters = set(delimiters)
        words = []
        delimiter_tokens = []

        while i < len(sentence):
            cur_token = []
            is_delimiter = sentence[i] in delimiters
            j = i

            while j < len(sentence) and (sentence[j] in delimiters) == is_delimiter:
                cur_token.append(sentence[j])
                j += 1

            if is_delimiter:
                delimiter_tokens.append("".join(cur_token))
            else:
                words.append("".join(cur_token))
            
            i = j

        words.reverse()

        if sentence[0] in delimiters:
            return "".join(delimiter_tokens[i//2] if i%2 == 0 else words[(i-1)//2] for i in range(len(words)+len(delimiter_tokens)))
        else:
            return "".join(words[i//2] if i%2 == 0 else delimiter_tokens[(i-1)//2] for i in range(len(words)+len(delimiter_tokens)))
