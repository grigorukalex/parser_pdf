from parser_pdf.bboxes import parse

pdf_path = 'db/p1.pdf'
parse(pdf_path,
      skip_num_tables=4,    # Кол-во таблиц, которые нужно пропустить на первой странице
      padding=(1.0, 0.95)   # Отступ сверху и сниху от границ таблицы в % от ширины и высоты страницы
      )
