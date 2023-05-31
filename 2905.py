from fpdf import FPDF

projeto = input('Digite a descrição do projeto: ')
horas_estimadas = int(input('Digite o total de horas estimadas: '))
valor_hora = int(input('Digite o valor da hora trabalhada: '))
prazo = input('Digite o prazo estimado: ')
valor_total = horas_estimadas * valor_hora

pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial')
pdf.image('template.png', x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, str(horas_estimadas))
pdf.text(115, 175, str(valor_hora))
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total))

pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso!')

