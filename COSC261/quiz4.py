def cfg_str_to_dict(cfg_str):
    """Converts a multiline CFG string representation
    of the form used in COSC261 quiz questions
    into a dictionary represention, e.g.
    "S=ab|bA|BB|_" becomes {"S": ["ab", "bA", "BB", ""]}
    """
    nonterminals = {char for char in cfg_str if char.isupper()}.union({"S"})
    result = {nt: [] for nt in nonterminals}
    productions = cfg_str.splitlines()
    for production in productions:
        nt, rhs = production.split("=")
        rhs = rhs.replace("_", "")  # Use "" for epsilon
        rhs_list = rhs.split("|")
        result[nt] = result[nt] + rhs_list
    return result


# def reachable_nts(cfg_str):
#     """
#     cfg_str is a multi-line string representing a CFG
#     """
#     # print(cfg_str_to_dict(cfg_str))
#     cfg_dict = cfg_str_to_dict(cfg_str)
#     start_state = cfg_dict["S"]

#     # iterates start state and finds non_terminals reachable from S
#     non_terminals = set()
#     strings_in_start_state = [string for string in start_state]
#     # print(strings_in_start_state)
#     for state in strings_in_start_state:
#         for letter in state:
#             if letter.isupper() == True:
#                 if letter not in non_terminals:
#                     non_terminals.add(letter)

#     for non_terminal in non_terminals:
#         start_state = cfg_dict[non_terminal]
#         for string in start_state:
#             for letter in string:
#                 if letter.isupper() == True:
#                     if letter not in non_terminals:
#                         non_terminals.add(letter)

#     if "S" not in non_terminals:
#         non_terminals.add("S")
#     return non_terminals


def reachable_nts(cfg_str):
    cfg_dict = cfg_str_to_dict(cfg_str)
    reachable = set()  # Set to store reachable non-terminals
    stack = ["S"]  # Initialize stack with start symbol 'S'

    # Iterate until stack is empty
    while stack:
        current_nt = stack.pop()
        if current_nt not in reachable:
            reachable.add(current_nt)
            # Add non-terminals found in the productions of current_nt
            for production in cfg_dict[current_nt]:
                for symbol in production:
                    if symbol.isupper():
                        stack.append(symbol)

    return reachable


# A simple case to check that the function returns a set
# cfg = "S=done"
# reachable = reachable_nts(cfg)
# print(reachable)
# print(type(reachable) is set)


cfg = """S=aSa|bSb|_
A=aS|bAA
B=bS|aBB"""
# print(reachable_nts(cfg))


cfg = """S=SGR|NS|C|X|PCX|CN|XN|QNR|R|SC|N|RRT|RU|STR|XXV|NN|US|CU|XS|NC|SNM|AUC|SQX
A=S|VVM|TDK|Q|K|IV|LV|PGI|VTQ|P|IVL|GD|TV|PG|MI|M|DDG|KGV|T|L
B=DP|DIs|Dzg|Qt|hAGafG|Tukfo|MkfMxs|A|kh|nkT|Dv|_|GVPp|bxnGm|dzQo|Dpcad|fsh|PwVP|QlIfV|djA|TuxdId|DbvGM|rdml
C=S|ULX|UR|U|XX|UPN|RQR|SS|UU|RKN|RKX|RU|RX|USG|NSA|NN|XS|VXU|NC|NU
D=TGK|AAQ|S|IL|A|GIA|Q|K|I|PQD|LV|TTQ|G|P|IP|M|TG|AA|AKD|DV|KDA
E=DT|eQtrQGr|xVdfD|wn|dge|ca|Gw|IPciLf|_|qIyP|lnLGI|oALnx|GQTn|r|wle|LpfMrp|bt|QzIrc|hI|D|LaLt
F=lz|wT|A|_|y|qdj|gdm|eI|Pmsvm|Irp|cAlKI|TAaVu|Vcqxz|PI|VLszkyG|zGTQu|M|PAD|KmApv|zoqVIj|GuuKLaj
G=S|AV|A|LDT|K|I|VQV|IA|PAT|IP|KL|M|QM|AQD|GQ|TQQ|PGT|T|DV|VLV|LT
H=NS|SX|S|C|X|DCC|SVX|CN|SC|R|SDR|N|KUR|LRC|CX|CUP|RC|ANS|STR|XR|NC|XDC
I=DPM|LA|S|GI|D|LP|IT|Q|K|GK|G|P|TV|PG|PL|KD|M|DG|KIL|IDP|T|QLD|V
J=CIX|S|C|X|ANR|UGX|RPS|SRQ|CN|SC|R|U|N|CR|XR|XKC|CU|LCU|UGC|NU|UIC
K=AAQ|S|LD|QG|QDV|MK|Q|I|AD|AP|KIM|KGP|L|LKL|IP|MTK|VI|T|KG|QAG|TMK|V|AIV
L=noG|Qw|mpbLDT|AMA|Tmb|GDT|AbiwM|qf|kc|sTTlD|kqdo|ykc|KAT|rAdqa|M|AA|VI|ffKM|gLxKs|IKV|lti
M=APT|KQ|VTG|S|MD|ML|LD|ADI|III|IV|K|I|ATV|G|P|AM|GD|GIL|GV|LII|V|LI
N=SX|NX|C|S|SR|RSL|R|XX|KNC|UQX|NR|XCA|TSC|XMN|CX|CLS|UAR|CU|XU|CPC|NU
O=SIX|VNX|S|SR|RAX|RVS|CC|RND|R|U|XAS|N|RKX|XC|RUM|XR|UIR|RTR|RIS|CUA|NCV|SN|UX|SRV|NU
P=GMQ|LvGA|mLz|t|DLhj|Al|zIsww|LG|aA|itA|As|_|vcc|ngf|mgPh|Tm|KD|zQkKj|KV|tMQ|T|LL|IjoTI|TyMDol|yma
Q=KK|VG|S|GG|TAK|VIG|MG|MMG|MV|TQ|VVL|TPM|KAP|G|TP|GVV|PI|M|VI|GL|QV|D
R=S|C|UXM|X|TUN|UC|UR|SC|N|XUM|SS|NR|RC|QSU|XR|RR|NTC|SPC|CU|TNN|NUL|NDS|XS|LNX|TRS
T=S|KVP|KI|LD|A|MLA|LVG|K|I|AP|LK|QL|IG|G|VV|P|PG|KP|VAL|L
U=UMX|SX|S|URP|UN|RSD|NMN|N|SU|RSA|MSX|ACN|XC|RX|RU|UKN|AUS|NCG|MXX|NUD
V=GPD|VIV|LA|S|DLL|KII|A|Q|K|LK|VPM|G|KA|IQL|PAT|TLL|DG|M|KV|T
W=NDX|NS|VUR|S|C|QXU|R|U|KSX|SC|N|SUV|CX|RC|XNP|ULU|XUG|SN|SNM|SVU|SMX
X=S|C|UN|RXD|XUD|KCR|VXR|R|U|N|SUK|NR|XC|RC|RU|RUM|NDN|XR|NCT|UNK
Y=UMS|NX|RAC|S|C|UNG|SAX|XSD|UN|UR|SSL|R|U|CCK|N|UPU|CR|URI|UU|SLC|RUK|CU|IXN|KUS|CNG
Z=MgjzPDo|LAndKu|ML|MMtI|IIG|brllD|PKK|jgkAy|IV|_|gePAx|Dr|dsa|zApwe|phvc|QoLauiL|Am|Gfu|xktPt|gs|VPu|l|Tw|V|LaVLb"""
# print(sorted(reachable_nts(cfg)))


cfg = """S=aB|bA|CC
A=aS|bAA
B=bS|aBB
C=abS|SC|_|D
D=DD
E=B"""
# print(sorted(reachable_nts(cfg)))


# The CFG G1 above, in which all NTs are reachable.
cfg = """S=BA
A=a|BA|BB
B=b|AA"""
# print(sorted(reachable_nts(cfg)))
# print(reachable_nts(cfg))

# C looks reachable at first but isn't. Can you see why?
cfg = """S=aB|bA
A=aS|bAA
B=bS|aBB|_
C=abC|SC"""
# print(reachable_nts(cfg))
# print(sorted(reachable_nts(cfg)))

# A tricky case: S is not in any productions but still reachable.
# By definition, S is reachable from S using 0 derivation steps
# (so no productions are needed).
cfg = "A=0A1"
# print(sorted(reachable_nts(cfg)))
