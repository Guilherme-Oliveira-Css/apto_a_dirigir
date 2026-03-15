age = int(input("Digite sua idade: "))
if age < 18:
    print("Ah não! Você não pode dirigir pois é menor de idade logo não tem CNH!")
else:
    has_license = input("Você tem CNH? (Sim/Não): ").lower() == "sim", "s"
    if not has_license:
        print("Ah não! Você tem a idade mínima para dirigir, mas não tem CNH! ")
    else:
        print("Parabéns! Você tem permissão para dirigir, tenha um bom dia!")
 



