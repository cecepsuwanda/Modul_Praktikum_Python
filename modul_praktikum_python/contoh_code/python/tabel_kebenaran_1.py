# -*- coding: utf-8 -*-
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def konjungsi(p, q):
    return p and q

def disjungsi(p, q):
    return p or q

def negasi(p):
    return not p

def implikasi(p, q):
    return not p or q

def biimplikasi(p, q):
    return p == q


def _cetak_judul(nomor: str, ekspresi: str) -> None:
    print(f"Soal {nomor} :")
    print(ekspresi)


def soal_5_1() -> None:
    # ¬(¬p ∧ ¬q)
    _cetak_judul("5.1", "¬(¬p ∧ ¬q)")
    print(f"{'p':>5} {'q':>5} {'¬p':>7} {'¬q':>7} {'¬p∧¬q':>7} {'¬(¬p∧¬q)':>11}")
    print("-" * (5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 7 + 1 + 11))
    for p in (True, False):
        for q in (True, False):
            np = negasi(p)
            nq = negasi(q)
            notp_and_notq = konjungsi(np, nq)
            hasil = negasi(notp_and_notq)
            print(f"{p!s:>5} {q!s:>5} {np!s:>7} {nq!s:>7} {notp_and_notq!s:>7} {hasil!s:>11}")


def soal_5_2() -> None:
    # p ∧ (p ∨ q)
    _cetak_judul("5.2", "p ∧ (p ∨ q)")
    print(f"{'p':>5} {'q':>5} {'p∨q':>7} {'p∧(p∨q)':>11}")
    print("-" * (5 + 1 + 5 + 1 + 7 + 1 + 11))
    for p in (True, False):
        for q in (True, False):
            p_or_q = disjungsi(p, q)
            hasil = konjungsi(p, p_or_q)
            print(f"{p!s:>5} {q!s:>5} {p_or_q!s:>7} {hasil!s:>11}")


def soal_5_3() -> None:
    # ((¬p ∧ (¬q ∧ r)) ∨ (q ∧ r)) ∨ (p ∧ r)
    _cetak_judul("5.3", "((¬p ∧ (¬q ∧ r)) ∨ (q ∧ r)) ∨ (p ∧ r)")
    print(
        f"{'p':>5} {'q':>5} {'r':>5} {'¬p':>7} {'¬q':>7} {'¬q∧r':>9} "
        f"{'¬p∧(¬q∧r)':>13} {'q∧r':>7} {'p∧r':>7} {'hasil':>7}"
    )
    print("-" * (5 + 1 + 5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 9 + 1 + 13 + 1 + 7 + 1 + 7 + 1 + 7))
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                np = negasi(p)
                nq = negasi(q)
                notq_and_r = konjungsi(nq, r)
                notp_and_notq_and_r = konjungsi(np, notq_and_r)
                q_and_r = konjungsi(q, r)
                p_and_r = konjungsi(p, r)
                hasil = disjungsi(disjungsi(notp_and_notq_and_r, q_and_r), p_and_r)
                print(
                    f"{p!s:>5} {q!s:>5} {r!s:>5} {np!s:>7} {nq!s:>7} {notq_and_r!s:>9} "
                    f"{notp_and_notq_and_r!s:>13} {q_and_r!s:>7} {p_and_r!s:>7} {hasil!s:>7}"
                )


def soal_5_4() -> None:
    # (p ∧ q) ∨ (((¬p ∧ q) → p) ∧ ¬q)
    _cetak_judul("5.4", "(p ∧ q) ∨ (((¬p ∧ q) → p) ∧ ¬q)")
    print(
        f"{'p':>5} {'q':>5} {'p∧q':>7} {'¬p':>7} {'¬p∧q':>9} {'(¬p∧q)→p':>13} {'¬q':>7} {'hasil':>7}"
    )
    print("-" * (5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 9 + 1 + 13 + 1 + 7 + 1 + 7))
    for p in (True, False):
        for q in (True, False):
            p_and_q = konjungsi(p, q)
            np = negasi(p)
            notp_and_q = konjungsi(np, q)
            impl = implikasi(notp_and_q, p)
            nq = negasi(q)
            kanan = konjungsi(impl, nq)
            hasil = disjungsi(p_and_q, kanan)
            print(f"{p!s:>5} {q!s:>5} {p_and_q!s:>7} {np!s:>7} {notp_and_q!s:>9} {impl!s:>13} {nq!s:>7} {hasil!s:>7}")


def soal_5_5() -> None:
    # (p → q) ↔ (¬q → ¬p)
    _cetak_judul("5.5", "(p → q) ↔ (¬q → ¬p)")
    print(f"{'p':>5} {'q':>5} {'¬p':>7} {'¬q':>7} {'p→q':>8} {'¬q→¬p':>13} {'hasil':>7}")
    print("-" * (5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 8 + 1 + 13 + 1 + 7))
    for p in (True, False):
        for q in (True, False):
            np = negasi(p)
            nq = negasi(q)
            p_implies_q = implikasi(p, q)
            notq_implies_notp = implikasi(nq, np)
            hasil = biimplikasi(p_implies_q, notq_implies_notp)
            print(f"{p!s:>5} {q!s:>5} {np!s:>7} {nq!s:>7} {p_implies_q!s:>8} {notq_implies_notp!s:>13} {hasil!s:>7}")


def soal_5_6() -> None:
    # p ∧ ((r ∨ q) ↔ ¬r)
    _cetak_judul("5.6", "p ∧ ((r ∨ q) ↔ ¬r)")
    print(f"{'p':>5} {'q':>5} {'r':>5} {'¬r':>7} {'r∨q':>7} {'(r∨q)↔¬r':>11} {'hasil':>7}")
    print("-" * (5 + 1 + 5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 11 + 1 + 7))
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                nr = negasi(r)
                r_or_q = disjungsi(r, q)
                bicond = biimplikasi(r_or_q, nr)
                hasil = konjungsi(p, bicond)
                print(f"{p!s:>5} {q!s:>5} {r!s:>5} {nr!s:>7} {r_or_q!s:>7} {bicond!s:>11} {hasil!s:>7}")


def soal_5_7() -> None:
    # ¬((p ∧ q) → ¬r) ∨ p
    _cetak_judul("5.7", "¬((p ∧ q) → ¬r) ∨ p")
    print(f"{'p':>5} {'q':>5} {'r':>5} {'¬r':>7} {'p∧q':>7} {'(p∧q)→¬r':>11} {'¬((p∧q)→¬r)':>15} {'hasil':>7}")
    print("-" * (5 + 1 + 5 + 1 + 5 + 1 + 7 + 1 + 7 + 1 + 11 + 1 + 15 + 1 + 7))
    for p in (True, False):
        for q in (True, False):
            for r in (True, False):
                nr = negasi(r)
                p_and_q = konjungsi(p, q)
                impl = implikasi(p_and_q, nr)
                not_impl = negasi(impl)
                hasil = disjungsi(not_impl, p)
                print(f"{p!s:>5} {q!s:>5} {r!s:>5} {nr!s:>7} {p_and_q!s:>7} {impl!s:>11} {not_impl!s:>15} {hasil!s:>7}")


def main() -> None:
    soal_5_1()
    print()
    soal_5_2()
    print()
    soal_5_3()
    print()
    soal_5_4()
    print()
    soal_5_5()
    print()
    soal_5_6()
    print()
    soal_5_7()


if __name__ == "__main__":
    main()
