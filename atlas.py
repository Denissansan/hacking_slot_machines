# character mappings for polyalphabetic substitution cipher

maps = {
' ': 	'6543210?>=<;:98\'&%$\xA3"! /.-,+*,(7',
'!': 	'+(,./,-"\xA3 !&\'$%:;89>?<=23016745*',
'"': 	'PSRUTWVYX[Z]\_^A@CBEDGFIHKJMLONQ',
'$': 	'<?>98;:54761032-,/.,(+*%$\'&! \xA3"=',
'%': 	'.-,+*,(\'&%$\xA3"! ?>=<;:9876543210/',
'&': 	'YZ[\]^_PQRSTUVWHIJKLMNO@ABCDEFGX',
'\'': 	'FEDCBA@ONMLKJIHWVUTSRQP_^]\[ZYXG',
'(': 	'|?~yx{zutwvqpsrmlonihkjedgfa`cb}',
')': 	'~}|{zyxwvutsrqponmlkjihgfedcba`#',
'*': 	'WTURSPQ^_\]Z[XYFGDEBC@ANOLMJKHIV',
'+': 	'UVWPQRS\]^_XY|[DEFG@ABCLMNOHIJKT',
',': 	'TWVQPSR]\_^YX[ZEDGFA@CBMLONIHKJU',
'-': 	'rqpwvut{zyx#~}|cba`gfedkjihonmls',
'.': 	'}~#xyq{tuvwpqrslmnohijkdefg\'abc|',
'/': 	'X[Z]\_^QPSRUTWVIHKJMLONA@CBEDGFY',
'0': 	'^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@_',
'1': 	'2107654;:98?>=<\xA3"! \'&%$+*,(/.-,3',
'2': 	' \xA3"%$\'&,(+*-,/.1032547698;:=<?>! ',
'3': 	'&%$\xA3"! /.-,+*,(76543210?>=<;:98\'',
'4': 	'_\]Z[XYVWTURSPQNOLMJKHIFGDEBC@A^',
'5': 	'/,-*+(,&\'$%"\xA3 !>?<=:;8967452301.',
'6': 	'5670123<=>?89:;$%&\' !"\xA3,-./(,*+4',
'7': 	'\_^YX[ZUTWVQPSRMLONIHKJEDGFA@CB]',
'8': 	'QRSTUVWXYZ[\]^_@ABCDEFGHIJKLMNOP',
'9': 	'twvqpsr}|#~yx{zedgfa`cbmlonihkju',
':': 	'MNOHIJKDEFG@ABC\]^_XYZ[TUVWPQRSL',
';': 	'7452301>?<=:;89&\'$%"\xA3 !./,-*+(,6',
'<': 	'3016745:;89>?<="\xA3 !&\'$%*+(,./,-2',
'=': 	'4761032=<?>98;:%$\'&! \xA3"-,/.,(+*5',
'>': 	'efg`abclmnohijktuvwpqrs|}~#xyz{d',
'?': 	'DGFA@CBMLONIHKJUTWVQPSR]\_^YX[ZE',
'@': 	'RQPWVUT[ZYX_^]\CBA@GFEDKJIHONMLS',
'A': 	'psrutwvyx{z}|#~a`cbedgfihkjmlonq',
'B': 	'zyx#~}|srqpwvutkjihonmlcba`gfed{',
'C': 	'8;:=<?>10325476,(+*-,/.! \xA3"%$\'&9',
'D': 	',/.,(+*%$\'&! \xA3"=<?>98;:54761032-',
'E': 	'HKJMLONA@CBEDGFYX[Z]\_^QPSRUTWVI',
'F': 	'abcdefghijklmnopqrstuvwxyz{|}~#`',
'G': 	'mnohijkdefg`abc|}~#xyz{tuvwpqrsl',
'H': 	'BA@GFEDKJIHONMLSRQPWVUT[ZYX_^]\C',
'I': 	'nmlkjihgfedcba`#~}|{zyxwvutsrqpo',
'J': 	'qrstuvwxyz{|}~#`abcdefghijklmnop',
'K': 	'x{z}|#~qpsrutwvihkjmlona`cbedgfy',
'L': 	'spqvwtuz{xy~#|}bc`afgdejkhinolmr',
'M': 	'hkjmlona`cbedgfyx{z}|#~qpsrutwvi',
'N': 	'fedcba`onmlkjihwvutsrqp#~}|{zyxg',
'O': 	'ijklmno`abcdefgxyz{|}~#pqrstuvwh',
'P': 	'uvwpqrs|}~#xyz{defg`abclmnohijkt',
'Q': 	',*+,-./ !"\xA3$%&\'89:;<=>?01234567(',
'R': 	'ba`gfedkjihonmlsrqpwvut{zyx#~}|c',
'S': 	'(+*-,/.! \xA3"%$\'&98;:=<?>10325476,',
'T': 	'!"\xA3$%&\'(,*+,-./0123456789:;<=>? ',
'U': 	'C@AFGDEKJHINOLMRSPQVWTUZ[XY^_\]B',
'V': 	'GDEBC@ANOLMJKHIVWTURSPQ^_\]z[XYF',
'W': 	'LONIHKJEDGFA@CB]\_^YX[ZUTWVQPSRM',
'X': 	'\'$%"\xA3 !./,-*+(,67452301>?<=;:89&',
'Y': 	'lonihkjedgfa`cb,|?~yx(zutwvqpsrm',
'Z': 	'SPQVWTUZ[XY^_\]BC@AFGDEJKHINOLMR',
'[': 	'c`afgdejkhinolmrspqvwtuz{xy~#|}b',
'\\': 	'ZYX_^]\SRQPWVUTKJIHONMLCBA@GFED[',
']': 	'`cbedgfihkjmlonqpsrutwvyx{z}|#~a',
'^': 	'>=<;:9876543210/.-,+*,(\'&%$\xA3"! ?',
'_': 	'wturspq~#|}z{xyfgdebc`anolmjkhiv',
'`': 	'*,(/.-,\xA3"! \'&%$;:98?>=<32107654+',
'a': 	'%&\' !"\xA3,-./(,*+45670123<=>?89:;$',
'b': 	'vutsrqp?~}|{zyxgfedcba`onmlkjihw',
'c': 	'?<=:;8967452301./,-*+(,&\'$%"\xA3 !>',
'd': 	'yz{|}~?pqrstuvwhijklmno`abcdefgx',
'e': 	']^_XYZ[TUVWPQRSLMNOHIJKDEFG@ABC\\',
'f': 	'-./(,*+$%&\' !"\xA3<=>?89:;45670123,',
'g': 	':98?>=<32107654+*,(/.-,\xA3"! \'&%$;',
'h': 	'OLMJKHIFGDEBC@A^_\]Z[XYVWTURSPQN',
'i': 	'khinolmbc`afgdez{xy~?|}rspqvwtuj',
'j': 	'JIHONMLCBA@GFED[ZYX_^]\SRQPWVUTK',
'k': 	'VUTSRQP_^]\[ZYXGFEDCBA@ONMLKJIHW',
'l': 	'123456789:;<=>? !"\xA3$%&\'(,*+,-./0',
'm': 	'KHINOLMBC@AFGDEZ[XY^_\]RSPQVWTUJ',
'n': 	';89>?<=23016745*+(,./,-"\xA3 !&\'$%:',
'o': 	'EFG@ABCLMNOHIJKTUVWPQRS\]^_XYZ[D',
'p': 	'jihonmlcba`gfed{zyx?~}|srqpwvutk',
'q': 	'{xy~?|}rspqvwtujkhinolmbc`afgdez',
'r': 	'"! \'&%$+*,(/.-,32107654;:98?>=<\xA3',
's': 	'?|}z{xyvwturspqnolmjkhifgdebc`a~',
't': 	'$\'&! \xA3"-,/.,(+*54761032=<?>98;:%',
'u': 	'=>?89:;45670123,-./(,*+$%&\' !"\xA3<',
'v': 	'ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_@',
'w': 	'olmjkhifgdebc`a~#|}z{xyvwturspqn',
'x': 	'dgfa`cbmlonihkjutwvqpsr}|?~yx{ze',
'y': 	'@CBEDGFIHKJMLONQPSRUTWVYX[Z]\_^A',
'z': 	'gdebc`anolmjkhivwturspq~?|}z{xyf',
'{': 	'9:;<=>?01234567(,*+,-./ !"\xA3$%&\'8',
'|': 	'[XY^_\]RSPQVWTUJKHINOLMBC@AFGDEZ',
'}': 	'\xA3 !&\'$%*+(,./,-23016745:;89>?<="',
'~': 	'NMLKJIHGFEDCBA@_^]\[ZYXWVUTSRQPO',
'\x7f': 	'032547698;:=<?>! \xA3"%$\'&,(+*-,/.1',
'#': 	'IJKLMNO@ABCDEFGXYZ[\]^_PQRSTUVWH'
}
