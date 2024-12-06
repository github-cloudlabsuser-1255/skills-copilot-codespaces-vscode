function calculateNumbers(var1, var2) {
  return var1 + var2;
}

function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}