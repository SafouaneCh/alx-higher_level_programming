#!/usr/bin/python3
if __name__ == "__main__":
    def multiple_returns(sentence):
        if len(sentence) == 0:
            return None
        t = len(sentence), sentence[0]
        return t
