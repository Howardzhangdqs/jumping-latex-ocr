from random import choice


patterns = [
    [[r"\sum"], [r"\mathop{\frac{}2}\limits"]],
    [
        [
            r"\dot z",
            r"\dot{z}",
            r"\dot{\mathcal Z}",
            r"\dot{\mathcal z}",
            r"\dot{\mathcal{Z}}",
            r"\dot{\mathcal{z}}",
        ], ["主"]
    ],
    [[r"\Gamma"], [" T ", " 7 ", r"\text{T}"]],
    [[r"\pi z"], [r"\pi^z"]],
    [[r"\pi x"], [r"\pi^x"]],
    [
        [r"\psi", r"\phi", r"\Phi", r"\varPhi", r"\Psi"],
        [r"\varphi"]
    ],
    [[r"c\mu", r"c \mu"], [r"L/\text -l"]],
    [[r"\mu"], [r" m ", r" r\!u "]],
    [[r"\nabla"], [r" D "]],
    [[r"B_1", r"B_{1}"], [r" B \cdot 1 "]]
]


def amend_tex(tex: str):
    for pattern in patterns:
        for query in pattern[0]:
            new_tex = ""
            while tex != new_tex:
                if new_tex != "":
                    tex = new_tex
                new_tex = tex.replace(query, choice(pattern[1]), 1)
            tex = new_tex
    return tex


if __name__ == "__main__":
    print(
        amend_tex(r"\sum_{k=1}^{+\infty}=\dot z + \Gamma\left(\pi z\right) \Psi"))
    print(amend_tex(r"c\mu c"))
