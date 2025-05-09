cursoa = {("Ana", 101), ("Carlos", 102), ("João", 103)}
cursob = {("João", 103), ("Marina", 104), ("Carlos", 102)}

exclua = cursoa - cursob

exclub = cursob - cursoa

ambos = cursoa & cursob
 
print ("Exclusivos do curso A:",exclua)
print ("Exclusivos do curso B:",exclub)
print ("Matriculados nos dois cursos:",ambos)