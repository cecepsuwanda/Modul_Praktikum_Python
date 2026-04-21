"""Tabel Kebenaran"""


def konjungsi(p: bool, q: bool) -> bool:
    return p and q


def disjungsi(p: bool, q: bool) -> bool:
    return p or q


def negasi(p: bool) -> bool:
    return not p


def implikasi(p: bool, q: bool) -> bool:
    # p -> q  ekuivalen dengan (not p) or q
    return (not p) or q


def biimplikasi(p: bool, q: bool) -> bool:
    # p <-> q  ekuivalen dengan (p -> q) and (q -> p), atau p == q untuk boolean
    return p == q


def main() -> None:
    print("Soal 5.1 :")
    print(
        f"{'p':>5} {'q':>5} {'not p':>7} {'not q':>7}  "
        f"{'(not p) and (not q)':>20}  {'not((not p) and (not q))':>26}"
    )
    print("-" * 79)
    for p in (True, False):
        for q in (True, False):
            np, nq = negasi(p), negasi(q)
            k = konjungsi(np, nq)
            print(
                f"{p!s:>5} {q!s:>5} {np!s:>7} {nq!s:>7}  "
                f"{k!s:>20}  {negasi(k)!s:>26}"
            )

    print("Soal 5.2 :")
    print(
        f"{'p':>5} {'q':>5} {'p or q':>8} "
        f"{'p and (p or q)':>16}"
    )
    print("-" * 52)
    for p in (True, False):
        for q in (True, False):
            pq = disjungsi(p, q)
            absorb = konjungsi(p, pq)
            print(
                f"{p!s:>5} {q!s:>5} {pq!s:>8} "
                f"{absorb!s:>16}"
            )

    print("Soal 5.3 :")
    print(
        "Ekspresi: (((not p) and (not q) and r) or (q and r)) or (p and r)"
    )
    print(
        "t1 = (not p) and (not q) and r;  d1 = t1 or (q and r);  d2 = d1 or (p and r)"
    )
    print(
        f"{'p':>5} {'q':>5} {'r':>5} {'not p':>7} {'not q':>7} "
        f"{'q and r':>9} {'p and r':>9} {'(not q) and r':>14} "
        f"{'t1':>7} {'d1':>7} {'d2':>7}"
    )
    print("-" * 82)
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                negasi_p = negasi(p)
                negasi_q = negasi(q)
                konjungsi_qr = konjungsi(q, r)
                konjungsi_pr = konjungsi(p, r)
                konjungsi_negasi_qr = konjungsi(negasi_q, r)
                konjungsi_negasi_pqr = konjungsi(negasi_p, konjungsi_negasi_qr)
                disjungsi_pqr = disjungsi(konjungsi_negasi_pqr, konjungsi_qr)
                disjungsi_p_qr = disjungsi(disjungsi_pqr, konjungsi_pr)
                print(
                    f"{p!s:>5} {q!s:>5} {r!s:>5} {negasi_p!s:>7} {negasi_q!s:>7} "
                    f"{konjungsi_qr!s:>9} {konjungsi_pr!s:>9} "
                    f"{konjungsi_negasi_qr!s:>14} "
                    f"{konjungsi_negasi_pqr!s:>7} {disjungsi_pqr!s:>7} "
                    f"{disjungsi_p_qr!s:>7}"
                )

    print("Soal 5.4 :")
    print(
        "Ekspresi: (p and q) or ((((not p) and q) -> p) and (not q))"
    )
    print(
        "t1 = (not p) and q;  t2 = t1 -> p;  t3 = t2 and (not q);  "
        "hasil = (p and q) or t3"
    )
    print(
        f"{'p':>5} {'q':>5} {'not p':>7} {'not q':>7} "
        f"{'p and q':>9} {'t1':>7} {'t2':>7} {'t3':>7} {'hasil':>7}"
    )
    print("-" * 79)
    for p in (True, False):
        for q in (True, False):
            negasi_p = negasi(p)
            negasi_q = negasi(q)
            konjungsi_pq = konjungsi(p, q)
            t1 = konjungsi(negasi_p, q)
            t2 = implikasi(t1, p)
            t3 = konjungsi(t2, negasi_q)
            hasil = disjungsi(konjungsi_pq, t3)
            print(
                f"{p!s:>5} {q!s:>5} {negasi_p!s:>7} {negasi_q!s:>7} "
                f"{konjungsi_pq!s:>9} {t1!s:>7} {t2!s:>7} {t3!s:>7} {hasil!s:>7}"
            )

    print("Soal 5.5 :")
    print(
        "Ekuivalensi kontrapositif: (p -> q) <-> ((not q) -> (not p))."
    )
    print(
        f"{'p':>5} {'q':>5} {'not p':>7} {'not q':>7} "
        f"{'p -> q':>8} {'(not q) -> (not p)':>19} {'<->':>6}"
    )
    print("-" * 72)
    for p in (True, False):
        for q in (True, False):
            negasi_p = negasi(p)
            negasi_q = negasi(q)
            implikasi_pq = implikasi(p, q)
            implikasi_nq_np = implikasi(negasi_q, negasi_p)
            biimplikasi_pq = biimplikasi(implikasi_pq, implikasi_nq_np)
            print(
                f"{p!s:>5} {q!s:>5} {negasi_p!s:>7} {negasi_q!s:>7} "
                f"{implikasi_pq!s:>8} {implikasi_nq_np!s:>19} "
                f"{biimplikasi_pq!s:>6}"
            )

if __name__ == "__main__":
    main()
