export let userDeposit = 40;
export let userEarning = parseFloat(Number(localStorage.getItem('userEarning')).toFixed(2)) || 0;
export function earn() {
  userEarning += userDeposit * 0.0006666667
  localStorage.setItem('userEarning', userEarning.toString());

  }
