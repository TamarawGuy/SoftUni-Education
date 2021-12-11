function rectangle(w, h, c) {
    return {
        width: w,
        height: h,
        color: c.charAt(0).toUpperCase() + c.slice(1),
        calcArea: () => w * h
    }
}