import re


class JavaCodeCleaner:

    @staticmethod
    def clean(code):
        # SINGLE-LINE COMMENTS //
        code = re.sub(r'//.*', '', code)

        # JAVADoc AND MULTI-LINE COMMENTS /** */ AND /* */
        code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

        # EXTRA SPACE TO ONE SPACE
        code = re.sub(r'\s+', ' ', code).strip()

        # IMPORT STATEMENT
        code = re.sub(
            r'\s*import\s+(static\s+)?[^\s;]+(\.[^\s;]+)*;\s*', '', code, flags=re.MULTILINE)

        code = re.sub(
            r'\s*package\s+[^\s;]+;\s*', '', code, flags=re.MULTILINE)

        return code
