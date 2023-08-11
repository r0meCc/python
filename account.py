class Account:
    def __init__(self, name: str):
        """Initialize an account with the given name and a balance of 0."""
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """Deposit the specified amount into the account balance.
        
        Args:
            amount (float): The amount to be deposited.
            
        Returns:
            bool: True if the deposit is successful, False 
        """
        
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw the specified amount from the account balance.
        Args:
            amount (float): The amount to be withdrawn.
            
        Returns:
            bool: True if the withdrawal is successful, False
        """
        
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        """Return the current account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Return the account name."""
        return self.__account_name
