from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Preformatted
)

W, H = A4

# Couleurs simples
NOIR = HexColor('#000000')
GRIS = HexColor('#333333')
BLEU = HexColor('#1a5276')

def PS(name, **kw):
    return ParagraphStyle(name, **kw)

def get_styles():
    return {
        'titre': PS('titre', fontName='Helvetica-Bold', fontSize=18, textColor=NOIR, alignment=TA_CENTER, spaceAfter=20, leading=22),
        'soustitre': PS('soustitre', fontName='Helvetica', fontSize=12, textColor=GRIS, alignment=TA_CENTER, spaceAfter=25),
        'exo_titre': PS('exo_titre', fontName='Helvetica-Bold', fontSize=13, textColor=BLEU, spaceAfter=8, spaceBefore=15),
        'corps': PS('corps', fontName='Helvetica', fontSize=11, textColor=NOIR, alignment=TA_JUSTIFY, leading=15, spaceAfter=6),
        'qcm_titre': PS('qcm_titre', fontName='Helvetica-Bold', fontSize=10, textColor=NOIR, spaceAfter=4, spaceBefore=8),
        'qcm_texte': PS('qcm_texte', fontName='Helvetica', fontSize=9, textColor=NOIR, leading=11, spaceAfter=2),
        'qcm_code': PS('qcm_code', fontName='Courier', fontSize=9, textColor=NOIR, leading=11, spaceAfter=3),
        'qcm_pre': PS('qcm_pre', fontName='Courier', fontSize=9, textColor=NOIR, leading=11, leftIndent=0, rightIndent=0, spaceAfter=3),
        'entete': PS('entete', fontName='Helvetica-Bold', fontSize=10, textColor=GRIS, alignment=TA_CENTER, spaceAfter=5),
    }

def draw_filigrane(c):
    c.saveState()
    c.setFillColor(HexColor('#DDDDDD'))
    c.setFont("Helvetica-Bold", 80)
    c.translate(W/2, H/2)
    c.rotate(45)
    c.drawCentredString(0, 0, "BAMBA")
    c.restoreState()


def en_tete_premiere_page(c, doc):
    draw_filigrane(c)
    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColor(GRIS)
    c.drawString(1.5*cm, H-1.8*cm, "Université Gaston Berger - Saint-Louis")
    c.drawRightString(W-1.5*cm, H-1.8*cm, "Année universitaire 2025-2026 | 07-06-2026")
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(W/2, H-2.3*cm, "Épreuve d'Algorithme et Programmation I")
    c.setFont("Helvetica", 8)
    c.drawCentredString(W/2, H-2.8*cm, "Durée : 2h - Aucun document autorisé")
    
    c.setStrokeColor(GRIS)
    c.setLineWidth(0.5)
    c.line(1.5*cm, H-3.1*cm, W-1.5*cm, H-3.1*cm)
    
    c.setFont("Helvetica", 8)
    c.drawString(1.5*cm, 1.5*cm, f"Page {doc.page}")
    c.restoreState()


def en_tete_autres_pages(c, doc):
    draw_filigrane(c)
    c.saveState()
    c.setFont("Helvetica", 8)
    c.setFillColor(GRIS)
    c.drawString(1.5*cm, 1.5*cm, f"Page {doc.page}")
    c.restoreState()


def build_pdf():
    doc = SimpleDocTemplate(
        "epreuve_algo1.pdf",
        pagesize=A4,
        leftMargin=1.5*cm,
        rightMargin=1.5*cm,
        topMargin=2.2*cm,
        bottomMargin=1.6*cm
    )
    styles = get_styles()
    story = []

    # ========== EN-TÊTE DE L'ÉPREUVE ==========
    story.append(Spacer(1, 14))
    story.append(Paragraph("LICENCE 1 - RENFORCEMENT INFORMATIQUE", styles['titre']))
    story.append(Paragraph("Algorithme et Programmation I", styles['soustitre']))
    story.append(Spacer(1, 5))
    
    # ========== EXERCICE 1 ==========
    story.append(Paragraph("Exercice 1 – Nombre « tout terrain » (5 points)", styles['exo_titre']))
    story.append(Paragraph(
        "Un entier naturel N est dit <b>tout terrain</b> s'il vérifie simultanément les trois propriétés suivantes :",
        styles['corps']
    ))
    story.append(Paragraph("1) Il est premier.", styles['corps']))
    story.append(Paragraph("2) La somme de ses chiffres est un nombre premier.", styles['corps']))
    story.append(Paragraph("3) Son inverse (c'est-à-dire le nombre lu de droite à gauche) est aussi un nombre premier.", styles['corps']))
    story.append(Spacer(1, 5))
    story.append(Paragraph("<b>Exemples :</b>", styles['corps']))
    story.append(Paragraph("• 13 : premier, somme 1+3=4 non premier → NON", styles['corps']))
    story.append(Paragraph("• 113 : premier, somme 1+1+3=5 premier, inverse 311 premier → OUI", styles['corps']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Travail demandé :</b>", styles['corps']))
    story.append(Paragraph(
        "Écrire un algorithme qui trouve et affiche "
        "tous les nombres « tout terrain » compris dans l'intervalle [100, 1000].",
        styles['corps']
    ))
    story.append(Spacer(1, 3))
    
    
    # ========== EXERCICE 2 ==========
    story.append(Spacer(1, 10))
    story.append(Paragraph("Exercice 2 – Nombre « alternant » (5 points)", styles['exo_titre']))
    story.append(Paragraph(
        "Un entier naturel est dit <b>alternant</b> si ses chiffres, lus de gauche à droite, "
        "alternent strictement entre pair et impair.",
        styles['corps']
    ))
    story.append(Spacer(1, 5))
    story.append(Paragraph("<b>Exemples :</b>", styles['corps']))
    story.append(Paragraph("• 1234 est alternant (1 impair → 2 pair → 3 impair → 4 pair)", styles['corps']))
    story.append(Paragraph("• 1212 est alternant", styles['corps']))
    story.append(Paragraph("• 135 n'est pas alternant (3 impair puis 5 impair → consécutifs non alternés)", styles['corps']))
    story.append(Paragraph("• 208 n'est pas alternant (2 pair puis 0 pair → consécutifs non alternés)", styles['corps']))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Travail demandé :</b>", styles['corps']))
    story.append(Paragraph(
        "Écrire un algorithme qui saisit un entier N>0 "
        "et affiche si N est alternant ou non.",
        styles['corps']
    ))
    
    story.append(PageBreak())
    
    # ========== QCM ==========
    story.append(Paragraph("QCM – Programmation en C (10 points)", styles['exo_titre']))
    story.append(Paragraph("<i>Pour chaque question, une seule réponse est correcte.</i>", styles['corps']))
    story.append(Spacer(1, 6))
    
    qcms = [
        {
            "code": "int x = 5, y = 1; int z = (y++) ? 2 : y == 1 && x || y; printf(\"%d\", --z);",
            "options": ["0", "1", "2", "3"]
        },
         {
            "code": "void main(){ int a= 1 , b = 2 , c = 3 , d; d = (a = c, b+=a , c = a + b + c); printf(\"%d %d %d %d\",d, a, b , c); }",
            "options": ["11 3 5 11", "11 1 5 11", "11 3 2 11", "11 3 3 11"]
        },
        {
            "code": " int main(){ int t[8]={1,2,3,4,5,6,7}; t[7] = 8 ;int i; for(i=2;i<6;i++) t[t[i]] = t[i]; for(i=0;i<8;i++) printf(\"%d \", t[i]); return 0; }",
            "options": ["1 2 3 3 5 5 7 8", "1 2 3 4 5 6 7 8", "8 7 6 5 4 3 2 1", "1 2 3 5 4 6 7 8"]
        },
         {
            "code": "#include<stdio.h> int main(){ int a = 5; if (a == 6); a = 0; if (a == 5) a++; else a += 2; printf(\"%d\", a); return 0; }",
            "options": ["5", "6", "8", "2"]
        },
        {
            "code": "void main () { while (1) { int i = 0; while (i < 10) { ++i; for (;;) { if (++i < 5) continue; break; } } printf(\"%d\", i); break; } }",
            "options": ["10", "9", "11", "le programme s'exécute a l'infini"]
        },
        {
            "code": "int main(){ int x = 6 , y =3   , z = 2 ; int m = x & z | y ; printf(\"m = %d\",m);}",
            "options": ["6", "0", "3", "1"]
        },
        {
            "code": "int main(){ int a = 6 , b =3   , z = 0 ; int m = a & (z | b) ; printf(\"m = %d\",m);}",
            "options": ["1", "0", "2", "6"]
        },
        {
            "code": "int main(){ int i = 1; do{ while(i) i--; for(i++;0;i++); break; }while(1); printf(\"%d\", i); return 0; }",
            "options": ["0", "2", "1", "Boucle infinie"]
        },
        {
            "code": "for(int i = 0; i < 5; i++) { for(int j = 0; j < 2; j++) { if(i > 2) break; printf(\"*\"); } }",
            "options": ["******", "********", "****", "**********"]
        },
        {
            "code": "int main(){ int i = 0 ; switch(i){case 0 : i++ ; case 1 : i+++2 ; case 2 : ++i ; }  printf(\"%d\",i++); return 0; }",
            "options": ["1", "2", "3", "4"]
        },
    ]
    
    def format_code(code):
        # If the code string already contains explicit new lines, preserve it exactly.
        if '\n' in code or '\r' in code:
            return code.replace('\r\n', '\n').replace('\t', '    ').rstrip()

        formatted_lines = []
        indent = 0
        current = ''
        paren_depth = 0
        in_for = False

        def flush_line():
            nonlocal current
            line = current.strip()
            if line:
                formatted_lines.append('    ' * indent + line)
            current = ''

        i = 0
        while i < len(code):
            ch = code[i]
            if ch == '(':
                stripped = current.rstrip()
                if stripped.endswith('for'):
                    in_for = True
                paren_depth += 1
                current += ch
            elif ch == ')':
                current += ch
                paren_depth -= 1
                if in_for and paren_depth == 0:
                    in_for = False
            elif ch == '{':
                # Preserve inline initializers like int t[8] = {1,2,3,4,5,6,7,8};
                current_stripped = current.strip()
                if '=' in current_stripped:
                    depth = 1
                    j = i + 1
                    while j < len(code) and depth > 0:
                        if code[j] == '{':
                            depth += 1
                        elif code[j] == '}':
                            depth -= 1
                        j += 1
                    if depth == 0:
                        rest = code[j:].lstrip()
                        if rest.startswith(';'):
                            current += code[i:j]
                            i = j
                            if i < len(code) and code[i] == ';':
                                current += ';'
                                i += 1
                            flush_line()
                            continue
                current = current_stripped
                if current:
                    formatted_lines.append('    ' * indent + current)
                formatted_lines.append('    ' * indent + '{')
                indent += 1
                current = ''
            elif ch == '}':
                current = current.strip()
                if current:
                    formatted_lines.append('    ' * indent + current)
                indent = max(indent - 1, 0)
                formatted_lines.append('    ' * indent + '}')
                current = ''
            elif ch == ';':
                current += ';'
                if not in_for:
                    flush_line()
            else:
                current += ch
            i += 1

        if current.strip():
            formatted_lines.append('    ' * indent + current.strip())

        return '\n'.join(formatted_lines)

    for i, q in enumerate(qcms, 1):
        story.append(Paragraph(f"<b>Question {i}</b>", styles['qcm_titre']))
        formatted_code = format_code(q['code'])
        
        # Créer un tableau pour les options en disposition verticale
        opts = q['options']
        opt_table = Table(
            [[f"A) {opts[0]}"],
             [f"B) {opts[1]}"],
             [f"C) {opts[2]}"],
             [f"D) {opts[3]}"]],
            colWidths=[W*0.45-2.5*cm]
        )
        opt_table.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('TEXTCOLOR', (0,0), (-1,-1), NOIR),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))

        q_row = Table(
            [[Preformatted(formatted_code, styles['qcm_pre']), opt_table]],
            colWidths=[W*0.55-2.5*cm, W*0.45-2.5*cm]
        )
        q_row.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))

        story.append(q_row)
        story.append(Spacer(1, 6))
    
    # ========== BARÈME ==========
   
    
    doc.build(story, onFirstPage=en_tete_premiere_page, onLaterPages=en_tete_autres_pages)
    print("✅ PDF généré : epreuve_algo1.pdf")

if __name__ == "__main__":
    build_pdf()