from backend.services.media_service import MediaService

serv = MediaService()

print("\n🧩 TESTE 1 — Calcular média de um aluno que tem notas")
media = serv.calcularMedia(1)
print(f"✅ Média retornada: {media}\n")

print("\n🧩 TESTE 2 — Calcular média de um aluno que não tem notas (deve ficar 'EM ANDAMENTO')")
media = serv.calcularMedia(5)  
print(f"✅ Média retornada: {media}\n")

print("\n🧩 TESTE 3 — Calcular média de um aluno reprovado (notas < 6)")
media = serv.calcularMedia(2)  
print(f"✅ Média retornada: {media}\n")

print("\n🧩 TESTE 4 — Calcular média de um aluno aprovado (notas ≥ 6)")
media = serv.calcularMedia(1)  
print(f"✅ Média retornada: {media}\n")
