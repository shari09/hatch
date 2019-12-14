let hi = [1, 2, 3, 4];
hi = hi.map(n => {
  if (n > 2) {
    return n;
  }
}).filter(n => n);

console.log(hi);