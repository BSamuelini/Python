#!/usr/bin/env python3
import os, time, random

RECORDS = os.path.join(os.path.dirname(__file__), "records.txt")

def log_record(nombre, juego, resultado):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(RECORDS, "a", encoding="utf-8") as f:
        f.write(f"{ts} | {nombre} | {juego} | {resultado}\n")

def ppt(nombre):
    print("PPT: p/a/t (s salir)")
    r = v = 0
    t0 = time.time()
    while True:
        j = input("Jugada: ").strip().lower()
        if j == "s": break
        if j not in ("p","a","t"): print("usa p/a/t/s"); continue
        b = random.choice(("p","a","t"))
        r += 1
        d = {"p":"Piedra", "a":"Papel", "t":"Tijera"}
        print(f"Tú: {d[j]} Bot: {d[b]}")
        if j == b: print("Empate")
        elif (j,b) in (("p","t"),("a","p"),("t","a")): v += 1; print("Ganaste")
        else: print("Perdiste")
    dur = time.time() - t0
    pts = int(1000*(v+1)/(r+dur+1)) if r else 0
    log_record(nombre, "PPT", f"Rondas:{r} Victorias:{v} Puntos:{pts}")
    print(f"Rondas:{r} Victorias:{v} Puntos:{pts}")

def adivina(nombre):
    niveles = {"1":(20,"normal"),"2":(50,"noob"),"3":(100,"pro"),"4":(1000000,"hacker")}
    print("Dificultades: 1)normal 2)noob 3)pro 4)hacker")
    d = ""
    while d not in niveles: d = input("Elige 1-4: ").strip()
    lim, etiq = niveles[d]
    n = random.randint(1, lim)
    print(f"{etiq}: adivina un número entre 1 y {lim} (0 rendirse)")
    t0 = time.time()
    intentos = 0
    while True:
        try:
            v = int(input("Intento: "))
        except ValueError:
            print("Debes introducir un número"); continue
        if v == 0: 
            log_record(nombre, f"Adivina({etiq})", f"Rendido")
            print("Rendido"); return
        if v < 1 or v > lim:
            print(f"El número debe estar entre 1 y {lim}"); continue
        intentos += 1
        if v < n: print("Bajo")
        elif v > n: print("Alto")
        else:
            dur = time.time() - t0
            pts = int(1000/(intentos + dur + 0.5))
            log_record(nombre, f"Adivina({etiq})", f"Acertó:{intentos} Puntos:{pts}")
            print(f"¡Acertaste! Intentos:{intentos} Puntos:{pts}"); return

def ahorcado(nombre):
    es = {"1":["gato","sol","casa"],"2":["programa","ordenador"]}
    va = {"3":["gos","sol","casa"],"4":["ordinador","programacio"]}
    niveles = {**{k:("ES Fácil",v) for k,v in es.items()}, 
               **{k:("VA Fácil",v) for k,v in va.items()}}
    print("Ahorcado: 1)ES Fácil 2)ES Difícil 3)VA Fácil 4)VA Difícil")
    lvl = ""
    while lvl not in niveles: lvl = input("Nivel 1-4: ").strip()
    etiq, lista = niveles[lvl]
    palabra = random.choice(lista).lower()
    por_adivinar = set(palabra)
    usadas = set()
    malas = set()
    intentos = 6
    t0 = time.time()
    while intentos > 0 and por_adivinar:
        mostrado = " ".join(c if c in usadas else "_" for c in palabra)
        inc = " ".join(sorted(malas)) if malas else "-"
        print(f"\n{mostrado}  Incorrectas: {inc}")
        letra = input("Letra: ").strip().lower()
        if not letra or len(letra) != 1: print("Una letra"); continue
        if letra in usadas: print("Usada"); continue
        usadas.add(letra)
        if letra in por_adivinar: 
            por_adivinar.discard(letra); print("Bien")
        else: 
            malas.add(letra); intentos -= 1; print(f"Mal. Restan {intentos}")
    dur = time.time() - t0
    if not por_adivinar:
        pts = int(1000/(1 + dur + (6-intentos)))
        log_record(nombre, f"Ahorcado({etiq})", f"Ganó Puntos:{pts}")
        print(f"¡Ganaste! Palabra:{palabra} Puntos:{pts}")
    else:
        log_record(nombre, f"Ahorcado({etiq})", "Perdió")
        print(f"Perdiste. Palabra:{palabra}")

def main():
    while True:
        print("=== MiniArcade ===\n1) PPT  2) Adivina  3) Ahorcado  4) Salir")
        o = input("Opción: ").strip()
        if o == "4": print("Adiós"); break
        if o in ("1","2","3"):
            nombre = input("Nombre: ").strip() or "Anon"
            if o == "1": ppt(nombre)
            elif o == "2": adivina(nombre)
            elif o == "3": ahorcado(nombre)
        else: print("Inválida")
        input("\nEnter para volver...")

if __name__ == "__main__":
    main()