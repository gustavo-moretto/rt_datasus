import camelot

# Extract tables from PDF
tables = camelot.read_pdf("C:\\Users\\175 MX\\Documents\\Gustavo\\datasus\\data_rt_states\\states\\arquivos_auxiliares\\pdfs\\tabelasus2025-1.pdf", pages="all")

# Convert the first table to a DataFrame and display
df = tables[0]
print(df)