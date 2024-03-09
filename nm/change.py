
def change(now: float | int, prev: float | int):
    ch = now - prev
    pc_ch = (ch / prev) * 100
    out_str = f"""% Change: {pc_ch:.1f} %
Delta: {ch:.3f}"""
    return out_str

if __name__ == "__main__":
    print(change(5, 4.4))