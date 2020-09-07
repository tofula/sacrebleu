import re

from .tokenizer_none import NoneTokenizer


class TokenizerRegexp(NoneTokenizer):

    def signature(self):
        return 're'

    def __init__(self):

        self.protected_re = [
            #list of patterns to be protected from tokenization
            # based on Moses tokenizer
            #https://github.com/moses-smt/mosesdecoder/blob/master/scripts/tokenizer/basic-protected-patterns
            re.compile(r'<\/?\S+\/?>'),
            re.compile(r'<\S+( [a-zA-Z0-9]+\=\"?[^\"]\")+ ?\/?>'),
            re.compile(r'<\S+( [a-zA-Z0-9]+\=\'?[^\']\')+ ?\/?>'),
            re.compile(r'[\w\-\_\.]+\@([\w\-\_]+\.)+[a-zA-Z]{2,}'),
            #re.compile(r''),
        ]

        self._re = [
            # language-dependent part (assuming Western languages)
            (re.compile(r'([\{-\~\[-\` -\&\(-\+\:-\@\/])'), r' \1 '),
            # tokenize period and comma unless preceded by a digit
            (re.compile(r'([^0-9])([\.,])'), r'\1 \2 '),
            # tokenize period and comma unless followed by a digit
            (re.compile(r'([\.,])([^0-9])'), r' \1 \2'),
            # tokenize dash when preceded by a digit
            (re.compile(r'([0-9])(-)'), r'\1 \2 '),
            # one space only between words
            (re.compile(r'\s+'), r' '),
        ]

    def _protect(self, line):
        """ replace term to be protected with placeholder
        """
        return line

    def _unprotect(self, line):
        """ recover back original string
        """
        return line

    def __call__(self, line):
        """Common post-processing tokenizer for `13a` and `zh` tokenizers.

        :param line: a segment to tokenize
        :return: the tokenized line
        """

        # mask the protected text first
        protected_tokens = [match.group()
                                for protected_re in self.protected_re
                                for match in re.finditer(protected_re, line)]
            # Apply the protected_patterns.
        for i, token in enumerate(protected_tokens):
            substitution = 'THISISPROTECTED' + str(i).zfill(3)
            line = line.replace(token, substitution)


        for (_re, repl) in self._re:
            line = _re.sub(repl, self._protect(line))

        # no leading or trailing spaces
        return self._unprotect(line).strip()
