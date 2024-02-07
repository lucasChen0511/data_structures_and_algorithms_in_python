#-----------------P2-34-----------------
class DocumentReader:
    def __init__(self, filepath):
        self._filepath = filepath
        self._total_chars = 0
        self._char_count = [0] * 26
        self._read_document()
    
    def _read_document(self):
        fp = open(self._filepath)
        all_text = fp.read().lower()
        for c in all_text:
            if self._check_if_chars(c):
                self._char_count[ord(c)-ord('a')] += 1
        self._total_chars = sum(self._char_count)
    
    def _check_if_chars(self, c):
        num = ord(c)
        if (ord('a') <= num <= ord('z')):
            return True
        else:
            return False
    
    def output_graph(self):
        max_val = max(self._char_count)
        for i in range(len(self._char_count)):
            print (chr(i+ord('a')), 'X' * int(self._char_count[i]/max_val*100))
        
        print('Each x represents: ', max_val * 100, 'instances of that character  (rounded down)')

if __name__ == '__main__':
    d = DocumentReader(r'F:\py_script\py_algorithm\Chapter2\test.txt')
    d.output_graph()