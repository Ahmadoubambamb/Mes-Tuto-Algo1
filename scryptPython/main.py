from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)

W, H = A4

CREAM       = HexColor('#FDFAF5')
WARM_WHITE  = HexColor('#FFFFFF')
LIGHT_GRAY  = HexColor('#F2EEE8')
MID_GRAY    = HexColor('#E8E2D9')
TEXT_MAIN   = HexColor('#2C2420')
TEXT_DIM    = HexColor('#7A6E65')
GOLD        = HexColor('#C9913A')
BORDEAUX    = HexColor('#7B1F3A')
TEAL        = HexColor('#1A6B6B')
TEAL_LT     = HexColor('#D4ECEA')
SAND        = HexColor('#EDE5D8')
CODE_BG     = HexColor('#F5F0E8')
CODE_BORDER = HexColor('#D0C4A8')
INDIGO      = HexColor('#3D3580')
INDIGO_LT   = HexColor('#E8E6F5')
DARK_GRAY   = HexColor('#3A3530')
ORANGE      = HexColor('#C0541A')
ORANGE_LT   = HexColor('#FEF0E6')

def page_template(c, doc):
    c.saveState()
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(Color(0.79, 0.57, 0.23, alpha=0.035))
    for xi in range(0, int(W)+30, 24):
        for yi in range(0, int(H)+30, 24):
            c.circle(xi, yi, 0.7, fill=1, stroke=0)

    m = 14
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    c.rect(m, m, W-2*m, H-2*m, fill=0, stroke=1)
    c.setStrokeColor(BORDEAUX); c.setLineWidth(0.3)
    c.rect(m+4, m+4, W-2*(m+4), H-2*(m+4), fill=0, stroke=1)

    cs = 22
    for (cx, cy, sx, sy) in [(m,H-m,1,-1),(W-m,H-m,-1,-1),(m,m,1,1),(W-m,m,-1,1)]:
        c.setStrokeColor(BORDEAUX); c.setLineWidth(1.8)
        c.line(cx, cy, cx+sx*cs, cy)
        c.line(cx, cy, cx, cy+sy*cs)
        c.setFillColor(GOLD)
        c.circle(cx, cy, 2.5, fill=1, stroke=0)

    c.saveState()
    c.translate(W/2, H/2); c.rotate(38)
    c.setFont("Helvetica-Bold", 115)
    c.setFillColor(Color(0.79, 0.57, 0.23, alpha=0.15))
    c.drawCentredString(0, 10, "BAMBA")
    c.setFont("Helvetica-Bold", 48)
    c.setFillColor(Color(0.79, 0.57, 0.23, alpha=0.1))
    c.drawCentredString(0, 140, "BAMBA")
    c.drawCentredString(0, -130, "BAMBA")
    c.restoreState()

    c.setStrokeColor(GOLD); c.setLineWidth(1.5)
    c.line(2*cm, H-2*cm, W-2*cm, H-2*cm)
    c.setStrokeColor(BORDEAUX); c.setLineWidth(0.4)
    c.line(2*cm, H-2*cm-3, W-2*cm, H-2*cm-3)
    c.setFont("Helvetica-Bold", 7.5); c.setFillColor(BORDEAUX)
    c.drawString(2*cm, H-1.6*cm, "TD — ALGORITHMIQUE I — LICENCE 1")
    c.setFont("Helvetica", 7); c.setFillColor(TEXT_DIM)
    c.drawRightString(W-2*cm, H-1.6*cm, "AlgoI  ·  L1  ·  2026  ·  Bamba")

    c.setStrokeColor(GOLD); c.setLineWidth(1.5)
    c.line(2*cm, 1.8*cm, W-2*cm, 1.8*cm)
    c.setStrokeColor(BORDEAUX); c.setLineWidth(0.4)
    c.line(2*cm, 1.8*cm+3, W-2*cm, 1.8*cm+3)
    c.setFont("Helvetica", 7); c.setFillColor(TEXT_DIM)
    c.drawString(2*cm, 1.2*cm, "© Bamba — AlgoI L1 2026")
    c.setFillColor(GOLD)
    c.circle(W/2, 1.35*cm, 9, fill=1, stroke=0)
    c.setFillColor(WARM_WHITE); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W/2, 1.35*cm-3, str(doc.page))
    c.setFillColor(TEXT_DIM); c.setFont("Helvetica", 7)
    c.drawRightString(W-2*cm, 1.2*cm, "Suites & Chiffres — Sans corrigé")
    c.restoreStore() if False else c.restoreState()

def PS(name, **kw):
    return ParagraphStyle(name, **kw)

def sp(n=1):
    return Spacer(1, n*5)

def exo_header(letter, title, subtitle, FW):
    lp = Paragraph(f'<font color="#FFFFFF"><b>{letter}</b></font>',
                   PS('el', fontName='Helvetica-Bold', fontSize=22,
                      textColor=WARM_WHITE, alignment=TA_CENTER, leading=26))
    tp = Paragraph(title,
                   PS('et', fontName='Helvetica-Bold', fontSize=15,
                      textColor=BORDEAUX, leading=19))
    sp2 = Paragraph(subtitle,
                    PS('es', fontName='Helvetica-Oblique', fontSize=9.5,
                       textColor=GOLD, leading=13))
    t = Table([[lp, [tp, sp2]]], colWidths=[46, FW-50])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(0,-1), BORDEAUX),
        ('BACKGROUND',    (1,0),(1,-1), SAND),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0),(-1,-1), 12),
        ('BOTTOMPADDING', (0,0),(-1,-1), 12),
        ('LEFTPADDING',   (0,0),(0,-1),  6),
        ('LEFTPADDING',   (1,0),(1,-1),  14),
        ('RIGHTPADDING',  (0,0),(-1,-1), 8),
        ('LINEBELOW',     (0,0),(-1,-1), 2.5, GOLD),
        ('LINEABOVE',     (0,0),(-1,-1), 0.5, BORDEAUX),
    ]))
    return t

def section_bar(text, FW, color=TEAL):
    p = Paragraph(f'<font color="#FFFFFF"><b>{text}</b></font>',
                  PS('sb', fontName='Helvetica-Bold', fontSize=9,
                     textColor=WARM_WHITE, leading=13))
    t = Table([[p]], colWidths=[FW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), color),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('LEFTPADDING',   (0,0),(-1,-1), 12),
    ]))
    return t

def body(text, FW):
    return Paragraph(text, PS('b', fontName='Helvetica', fontSize=9.5,
                               textColor=TEXT_MAIN, leading=15, alignment=TA_JUSTIFY,
                               spaceAfter=5))

def bullet(text):
    return Paragraph(
        f'<font color="#C9913A"><b>&#x25B6;</b></font>  {text}',
        PS('bi', fontName='Helvetica', fontSize=9.5, textColor=TEXT_MAIN,
           leading=15, leftIndent=12, spaceAfter=4))

def example_box(title, lines, FW):
    """Encart d'exemple numéroté sans solution."""
    rows = [[Paragraph(title, PS('et', fontName='Helvetica-Bold', fontSize=8.5,
                                  textColor=TEAL, spaceAfter=2))]]
    for l in lines:
        rows.append([Paragraph(l, PS('el', fontName='Courier', fontSize=8.5,
                                      textColor=DARK_GRAY, leading=13))])
    t = Table(rows, colWidths=[FW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), TEAL_LT),
        ('BACKGROUND',    (0,0),(-1,0),  HexColor('#C5E4E0')),
        ('BOX',           (0,0),(-1,-1), 1, TEAL),
        ('LINELEFT',      (0,0),(0,-1),  3, TEAL),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('LEFTPADDING',   (0,0),(-1,-1), 10),
        ('RIGHTPADDING',  (0,0),(-1,-1), 10),
    ]))
    return t

def todo_box(items, FW):
    """Encart 'Travail demandé'."""
    rows = [[Paragraph('<b>Travail demande</b>',
                       PS('th', fontName='Helvetica-Bold', fontSize=9,
                          textColor=BORDEAUX, spaceAfter=2))]]
    for i, item in enumerate(items, 1):
        rows.append([Paragraph(
            f'<font color="{BORDEAUX.hexval()}"><b>{i}.</b></font>  {item}',
            PS('ti', fontName='Helvetica', fontSize=9.5, textColor=TEXT_MAIN,
               leading=15, leftIndent=8))])
    t = Table(rows, colWidths=[FW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), HexColor('#FEF4E4')),
        ('BACKGROUND',    (0,0),(-1,0),  HexColor('#F5E0C0')),
        ('BOX',           (0,0),(-1,-1), 1.5, GOLD),
        ('LINELEFT',      (0,0),(0,-1),  4, GOLD),
        ('TOPPADDING',    (0,0),(-1,-1), 6),
        ('BOTTOMPADDING', (0,0),(-1,-1), 6),
        ('LEFTPADDING',   (0,0),(-1,-1), 12),
        ('RIGHTPADDING',  (0,0),(-1,-1), 12),
    ]))
    return t

def note_box(text, FW):
    """Petite note/rappel."""
    t = Table([[Paragraph(
        f'<font color="{INDIGO.hexval()}"><b>[Rappel]</b></font>  {text}',
        PS('nb', fontName='Helvetica', fontSize=9, textColor=INDIGO, leading=14)
    )]], colWidths=[FW])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), INDIGO_LT),
        ('BOX',           (0,0),(-1,-1), 1, INDIGO),
        ('LINELEFT',      (0,0),(0,-1),  3, INDIGO),
        ('TOPPADDING',    (0,0),(-1,-1), 7),
        ('BOTTOMPADDING', (0,0),(-1,-1), 7),
        ('LEFTPADDING',   (0,0),(-1,-1), 12),
        ('RIGHTPADDING',  (0,0),(-1,-1), 12),
    ]))
    return t

def blank_lines(n, FW):
    """Lignes vides pour que l'étudiant écrive."""
    rows = []
    for _ in range(n):
        rows.append([Paragraph('', PS('_')),
                     HRFlowable(width=FW*0.85, thickness=0.4,
                                color=HexColor('#CCCCCC'))])
    t = Table([[Paragraph(
        '<font color="#CCCCCC"><i>...................................................................'
        '...................................................................'
        '...................................................................</i></font>',
        PS('bl', fontName='Helvetica', fontSize=8, textColor=HexColor('#CCCCCC'),
           leading=18)
    )]] * n, colWidths=[FW])
    t.setStyle(TableStyle([
        ('TOPPADDING',    (0,0),(-1,-1), 1),
        ('BOTTOMPADDING', (0,0),(-1,-1), 1),
        ('LEFTPADDING',   (0,0),(-1,-1), 4),
    ]))
    return t


# ══════════════════════════════════════════════════════
def build(out):
    doc = SimpleDocTemplate(
        out, pagesize=A4,
        leftMargin=2.2*cm, rightMargin=2.2*cm,
        topMargin=2.5*cm, bottomMargin=2.3*cm,
        title="TD AlgoI L1 — Bamba",
        author="Bamba",
        subject="TD Algorithmique I — Licence 1",
    )
    FW = doc.width
    story = []

    # ─────────────────────────────────────
    # PAGE DE COUVERTURE
    # ─────────────────────────────────────
    story.append(sp(5))
    story.append(Paragraph("ALGORITHMIQUE I — LICENCE 1",
        PS('i', fontName='Helvetica', fontSize=9, textColor=TEXT_DIM,
           alignment=TA_CENTER, spaceAfter=6)))
    story.append(HRFlowable(width=FW*0.5, thickness=0.8, color=GOLD,
                             hAlign='CENTER', spaceAfter=6))
    story.append(Paragraph("Travaux Diriges",
        PS('mt', fontName='Helvetica-Bold', fontSize=34, textColor=BORDEAUX,
           alignment=TA_CENTER, leading=40, spaceAfter=4)))
    story.append(Paragraph("Suites, Chiffres & Boucles",
        PS('st', fontName='Helvetica-Oblique', fontSize=13, textColor=GOLD,
           alignment=TA_CENTER, spaceAfter=18)))
    story.append(HRFlowable(width=FW*0.55, thickness=2, color=BORDEAUX,
                             hAlign='CENTER', spaceAfter=4))
    story.append(HRFlowable(width=FW*0.35, thickness=0.6, color=GOLD,
                             hAlign='CENTER', spaceAfter=22))

    # Tableau des exercices
    exos = [
        ['Exo', 'Titre',                      'Concepts cles'],
        ['B',   'Suite Miroir',               'Boucle, miroir, palindrome'],
        ['D',   'Persistance Additive',        'Somme chiffres, compteur'],
        ['E',   'Suite de Collatz',            'Boucle, parite, conjecture'],
        ['F',   'Nombre parfait',              'Diviseurs, somme, boucle'],
        ['G',   'Decomposition en chiffres',   'Chiffres, puissance, identite'],
    ]
    t = Table(exos, colWidths=[FW*0.1, FW*0.34, FW*0.56])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,0),  BORDEAUX),
        ('TEXTCOLOR',     (0,0),(-1,0),  WARM_WHITE),
        ('FONTNAME',      (0,0),(-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0),(-1,-1), 9),
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [WARM_WHITE, SAND]),
        ('TEXTCOLOR',     (0,1),(0,-1),  GOLD),
        ('FONTNAME',      (0,1),(0,-1),  'Helvetica-Bold'),
        ('TEXTCOLOR',     (1,1),(-1,-1), TEXT_MAIN),
        ('FONTNAME',      (1,1),(-1,-1), 'Helvetica'),
        ('BOX',           (0,0),(-1,-1), 1.5, BORDEAUX),
        ('INNERGRID',     (0,0),(-1,-1), 0.3, MID_GRAY),
        ('TOPPADDING',    (0,0),(-1,-1), 7),
        ('BOTTOMPADDING', (0,0),(-1,-1), 7),
        ('LEFTPADDING',   (0,0),(-1,-1), 10),
        ('LINEBELOW',     (0,0),(-1,0),  1.5, GOLD),
    ]))
    story.append(t)
    story.append(sp(3))

    # Infos pratiques
    info = Table([
        [Paragraph('<b>Nom &amp; Prenom :</b>', PS('_', fontName='Helvetica-Bold',
                    fontSize=9, textColor=TEXT_MAIN)),
         Paragraph('_______________________________',
                   PS('_', fontName='Helvetica', fontSize=9, textColor=MID_GRAY))],
        [Paragraph('<b>Numero etudiant :</b>', PS('_', fontName='Helvetica-Bold',
                    fontSize=9, textColor=TEXT_MAIN)),
         Paragraph('_______________________________',
                   PS('_', fontName='Helvetica', fontSize=9, textColor=MID_GRAY))],
        [Paragraph('<b>Date :</b>', PS('_', fontName='Helvetica-Bold',
                    fontSize=9, textColor=TEXT_MAIN)),
         Paragraph('_______________________________',
                   PS('_', fontName='Helvetica', fontSize=9, textColor=MID_GRAY))],
    ], colWidths=[FW*0.35, FW*0.65])
    info.setStyle(TableStyle([
        ('BOX',           (0,0),(-1,-1), 1, CODE_BORDER),
        ('INNERGRID',     (0,0),(-1,-1), 0.3, MID_GRAY),
        ('TOPPADDING',    (0,0),(-1,-1), 7),
        ('BOTTOMPADDING', (0,0),(-1,-1), 7),
        ('LEFTPADDING',   (0,0),(-1,-1), 10),
        ('BACKGROUND',    (0,0),(-1,-1), LIGHT_GRAY),
    ]))
    story.append(info)
    story.append(sp(2))
    story.append(Paragraph("Bamba  —  2026  —  AlgoI Licence 1",
        PS('a', fontName='Helvetica-Bold', fontSize=10, textColor=GOLD,
           alignment=TA_CENTER)))
    story.append(PageBreak())

    # ═════════════════════════════════════
    # EXERCICE B — SUITE MIROIR
    # ═════════════════════════════════════
    story.append(sp(2))
    story.append(exo_header('B', 'Suite Miroir',
        "Construire une suite en additionnant un nombre a son miroir", FW))
    story.append(sp(2))

    story.append(section_bar('  Enonce', FW, BORDEAUX))
    story.append(sp())
    story.append(body(
        "On part d'un entier positif <b>N</b>. On construit une suite ainsi :", FW))
    story.append(bullet("On calcule <b>R</b>, le miroir (inverse) de N   "
                        "(exemple : 427 &rarr; 724)"))
    story.append(bullet("Le terme suivant est <b>N + R</b>"))
    story.append(bullet("On repete l'operation sur ce nouveau terme, jusqu'a obtenir "
                        "un <b>palindrome</b>"))
    story.append(sp())
    story.append(example_box("Exemple :", [
        "N = 57",
        "57  ->  57 + 75 = 132",
        "132 ->  132 + 231 = 363   (363 est un palindrome -> arret)",
    ], FW))
    story.append(sp(2))
    story.append(todo_box([
        "Ecrire un <b>algorithme et un programme C</b> qui saisit un entier N &gt; 0, affiche tous "
        "les termes de la suite jusqu'a l'obtention d'un palindrome, "
        "puis affiche ce palindrome final.",
    ], FW))
    story.append(PageBreak())

    # ═════════════════════════════════════
    # EXERCICE D — PERSISTANCE ADDITIVE
    # ═════════════════════════════════════
    story.append(sp(2))
    story.append(exo_header('D', 'Persistance Additive',
        "Compter les etapes pour reduire un entier a un seul chiffre", FW))
    story.append(sp(2))

    story.append(section_bar('  Enonce', FW, BORDEAUX))
    story.append(sp())
    story.append(body(
        "On appelle <b>persistance additive</b> d'un entier <b>N</b> le nombre "
        "d'etapes necessaires pour obtenir un nombre a un seul chiffre en repetant "
        "l'operation : <i>remplacer le nombre par la somme de ses chiffres</i>.", FW))
    story.append(sp())
    story.append(example_box("Exemple :", [
        "N = 199",
        "199  ->  1 + 9 + 9 = 19",
        "19   ->  1 + 9     = 10",
        "10   ->  1 + 0     = 1    (1 seul chiffre -> arret)",
        "Nombre d'etapes = 3",
    ], FW))
    story.append(sp(2))
    story.append(todo_box([
        "Ecrire un <b>algorithme</b> et un <b>programme C</b> qui calcule "
        "la persistance additive d'un entier saisi par l'utilisateur.",
        "Le programme affichera chaque etape intermediaire ainsi que "
        "le nombre total d'etapes.",
    ], FW))
    story.append(PageBreak())

    # ═════════════════════════════════════
    # EXERCICE E — SUITE DE COLLATZ
    # ═════════════════════════════════════
    story.append(sp(2))
    story.append(exo_header('E', 'Suite de Collatz',
        "Etudier une conjecture mathematique celebre sur les suites entieres", FW))
    story.append(sp(2))

    story.append(section_bar('  Enonce', FW, BORDEAUX))
    story.append(sp())
    story.append(body(
        "La <b>suite de Collatz</b> (ou suite de Syracuse) est definie a partir "
        "d'un entier positif <b>N</b> par la regle suivante :", FW))
    story.append(sp())
    story.append(bullet(
        "Si N est <b>pair</b> : le terme suivant est <b>N / 2</b>"))
    story.append(bullet(
        "Si N est <b>impair</b> : le terme suivant est <b>3 * N + 1</b>"))
    story.append(bullet(
        "On s'arrete quand <b>N = 1</b>"))
    story.append(sp())
    story.append(note_box(
        "La conjecture de Collatz affirme que, quel que soit l'entier de depart, "
        "la suite atteint toujours 1. Elle n'est pas encore demontree a ce jour.", FW))
    story.append(sp())
    story.append(example_box("Exemple : N = 6", [
        "6  -> 6/2      = 3   (pair)",
        "3  -> 3*3+1    = 10  (impair)",
        "10 -> 10/2     = 5   (pair)",
        "5  -> 5*3+1    = 16  (impair)",
        "16 -> 16/2     = 8   (pair)",
        "8  -> 8/2      = 4   (pair)",
        "4  -> 4/2      = 2   (pair)",
        "2  -> 2/2      = 1   (pair)  -> arret",
        "Nombre de termes (hors 1er) = 8",
    ], FW))
    story.append(sp(2))
    story.append(todo_box([
        "Ecrire un <b>algorithme</b> qui saisit un entier N &gt; 0 et affiche "
        "tous les termes de la suite de Collatz jusqu'a atteindre 1.",
        "Ecrire le <b>programme C</b> correspondant.",
        "<b>Extension :</b> Compter et afficher le nombre de termes de la suite "
        "(appele 'temps de vol' de N). Trouver quel entier entre 1 et 100 "
        "a le plus grand temps de vol.",
    ], FW))
    story.append(PageBreak())

    # ═════════════════════════════════════
    # EXERCICE F — NOMBRE PARFAIT
    # ═════════════════════════════════════
    story.append(sp(2))
    story.append(exo_header('F', 'Nombre Parfait',
        "Verifier si un entier est egal a la somme de ses diviseurs propres", FW))
    story.append(sp(2))

    story.append(section_bar('  Enonce', FW, BORDEAUX))
    story.append(sp())
    story.append(body(
        "Un entier positif <b>N</b> est dit <b>parfait</b> s'il est egal a la "
        "somme de tous ses diviseurs stricts (c'est-a-dire tous ses diviseurs "
        "sauf lui-meme).", FW))
    story.append(sp())
    story.append(note_box(
        "Un diviseur strict de N est un entier d compris entre 1 et N-1 "
        "tel que N mod d = 0.  "
        "Les 4 premiers nombres parfaits sont : 6, 28, 496, 8128.", FW))
    story.append(sp())
    story.append(example_box("Exemple : N = 28", [
        "Diviseurs stricts de 28 : 1, 2, 4, 7, 14",
        "Somme = 1 + 2 + 4 + 7 + 14 = 28",
        "28 = 28  ->  28 est un nombre parfait",
    ], FW))
    story.append(sp())
    story.append(example_box("Contre-exemple : N = 12", [
        "Diviseurs stricts de 12 : 1, 2, 3, 4, 6",
        "Somme = 1 + 2 + 3 + 4 + 6 = 16",
        "16 ≠ 12  ->  12 n'est pas parfait",
    ], FW))
    story.append(sp(2))
    story.append(todo_box([
        "Ecrire un <b>programme C et un algorithme</b> qui saisit un entier N et indique "
        "s'il est parfait ou non, en affichant la liste de ses diviseurs "
        "stricts et leur somme.",
         "<b>Extension :</b> Afficher tous les nombres parfaits compris entre 1 et 10000.",
    ], FW))
    story.append(PageBreak())

    # ═════════════════════════════════════
    # EXERCICE G — DÉCOMPOSITION EN CHIFFRES
    # ═════════════════════════════════════
    story.append(sp(2))
    story.append(exo_header('G', 'Decomposition en Chiffres',
        "Tester si un nombre est egal a la somme des puissances de ses chiffres", FW))
    story.append(sp(2))

    story.append(section_bar('  Enonce', FW, BORDEAUX))
    story.append(sp())
    story.append(body(
        "Un entier <b>N</b> a <b>k chiffres</b> est appele <b>nombre de Armstrong</b> "
        "(ou narcissique) s'il est egal a la somme de chacun de ses chiffres "
        "eleve a la puissance <b>k</b> (le nombre de chiffres de N).", FW))
    story.append(sp())
    story.append(note_box(
        "Nombre de chiffres k de N : compter combien de fois on peut diviser "
        "N par 10 avant d'atteindre 0.  "
        "Pour calculer d<super>k</super>, utiliser une boucle ou la fonction "
        "pow() de math.h.", FW))
    story.append(sp())
    story.append(example_box("Exemple 1 : N = 153  (3 chiffres  ->  k = 3)", [
        "Chiffres : 1, 5, 3",
        "1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153",
        "153 = 153  ->  153 est un nombre de Armstrong",
    ], FW))
    story.append(sp())
    story.append(example_box("Exemple 2 : N = 9474  (4 chiffres  ->  k = 4)", [
        "Chiffres : 9, 4, 7, 4",
        "9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474",
        "9474 = 9474  ->  9474 est un nombre de Armstrong",
    ], FW))
    story.append(sp())
    story.append(example_box("Contre-exemple : N = 100  (3 chiffres  ->  k = 3)", [
        "Chiffres : 1, 0, 0",
        "1^3 + 0^3 + 0^3 = 1 + 0 + 0 = 1",
        "1 ≠ 100  ->  100 n'est pas un nombre de Armstrong",
    ], FW))
    story.append(sp(2))
    story.append(todo_box([
        "Ecrire un <b>algorithme et un programme C</b> qui saisit un entier N et indique "
        "s'il est un nombre de Armstrong, en affichant les étapes du calcul.",
        "<b>Extension :</b> Afficher tous les nombres de Armstrong "
        "compris entre 1 et 9999.",
    ], FW))

    story.append(sp(4))
    story.append(HRFlowable(width=FW*0.6, thickness=1.5, color=BORDEAUX,
                             hAlign='CENTER', spaceAfter=6))
    story.append(HRFlowable(width=FW*0.35, thickness=0.5, color=GOLD,
                             hAlign='CENTER', spaceAfter=10))
    story.append(Paragraph("Bon courage !",
        PS('fc', fontName='Helvetica-Bold', fontSize=11,
           textColor=BORDEAUX, alignment=TA_CENTER, spaceAfter=3)))
    story.append(Paragraph("Bamba  —  Algo1 Licence 1  —  2026",
        PS('fa', fontName='Helvetica-Oblique', fontSize=9,
           textColor=GOLD, alignment=TA_CENTER)))

    doc.build(story, onFirstPage=page_template, onLaterPages=page_template)
    print(f"PDF genere : {out}")

build('C:\\Users\\dell\\Documents\\codesRenfAlgo1\\Mes-Tuto-Algo1\\scryptPython\\TDs\\TD1_Suites_Chiffres.pdf')