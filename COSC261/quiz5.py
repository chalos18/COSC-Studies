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


def generating_nts(cfg_str):
    cfg_dict = cfg_str_to_dict(cfg_str)
    generating = set()  # Set to store reachable non-terminals

    # Keep track of changes in generating set to check for stabilization
    prev_generating = set()

    while True:
        prev_generating.update(generating)

        for non_terminal, productions in cfg_dict.items():
            # If all symbols in the production are generating or terminals, mark the non-terminal as generating
            for production in productions:
                # Updated condition to consider lowercase letters, numbers, and epsilon as terminals
                if all(
                    symbol in generating
                    or (symbol.islower() or symbol.isdigit() or symbol == "_")
                    for symbol in production
                ):
                    generating.add(non_terminal)
                    break

        # Check if generating set has stabilized
        if prev_generating == generating:
            break

    return generating


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
print(sorted(generating_nts(cfg)))

# a CFG where some non-terminals have only an epsilon-production
cfg = """S=X|Y
W=_
X=Z1|0Z|1Y|Y0
Y=1|0|X
Z=_"""
# print(sorted(generating_nts(cfg)))


# The CFG G1 above, in which all NTs are generating.
cfg = """S=BA
A=a|BA|BB
B=b|AA"""
# print(sorted(generating_nts(cfg)))
# print(generating_nts(cfg))


# A and C are not generating. Can you see why?
cfg = """S=aAa|bBb
A=aC|bAA
B=b|aBB
C=Ab|bA"""
# print(sorted(generating_nts(cfg)))


# None of these are generating!
cfg = """S=aAa|bBb
A=aS|bAA
B=bS|aBB"""
# print(generating_nts(cfg))
