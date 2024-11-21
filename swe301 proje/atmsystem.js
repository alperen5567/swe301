function withdrawCash() {
 
    let amount = document.getElementById("amount").value;
    let errorMessage = document.getElementById("error-message");
    let successMessage = document.getElementById("success-message");
    
    const accountBalance = 1000;
    
    errorMessage.textContent = "";
    successMessage.textContent = "";
     
    if (amount <= 0 || isNaN(amount)) {
        errorMessage.textContent = "The amount to withdraw should be valid";
        return;
 
    }
 
    if (amount > accountBalance) {
        errorMessage.textContent = "Amount exceeds account balance";
        return;
 
    }
 
    successMessage.textContent = "Transaction was successful. Cash worth $" + amount + " has been dispensed";
}

