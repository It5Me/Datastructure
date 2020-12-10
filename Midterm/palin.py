def palin(str_):
    return True if len(str_) <= 1 else palin(str_[1:-1]) and str_[0] == str_[-1]
if palin("EPIMMIPE"):
    print("Ku Jum Dai I Sus")
