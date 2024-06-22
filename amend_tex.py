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
    [[r"\Gamma"], ["T", "7", r"\text{T}"]],
    [[r"\pi z"], [r"\pi^z"]],
    [
        [r"\psi", r"\phi", r"\Phi", r"\varPhi", r"\Psi"],
        [r"\varphi"]
    ]
]


def amend_tex(tex: str):
    for pattern in patterns:
        for query in pattern[0]:
            tex = tex.replace(query, choice(pattern[1]))
    return tex


if __name__ == "__main__":
    tex = r"\sum_{k=1}^{+\infty}=\dot z + \Gamma\left(\pi z\right) \Psi"
    print(amend_tex(tex))
