# Module 20 Challenge

![20-5-challenge-image](https://user-images.githubusercontent.com/25112189/185760900-e6ce125a-e50f-4525-8bdb-a0613a601682.png)

---

## Background
A fintech startup company has recently hired me. This company is disrupting the finance industry with its own cross-border, Ethereum-compatible blockchain that connects financial institutions. Currently, the team is building smart contracts to automate many of the institutions’ financial processes and features, such as hosting joint savings accounts.

To automate the creation of joint savings accounts, I've created a Solidity smart contract that accepts two user addresses. These addresses will be able to control a joint savings account. My smart contract uses ether management functions to implement a financial institution’s requirements for providing the features of the joint savings account. These features consist of the ability to deposit and withdraw funds from the account.

---

## Remix IDE 
1. Open [Remix IDE](https://remix.ethereum.org/)
2. Click "Load From GitHub"
3. Enter "https://raw.githubusercontent.com/travispeska/gwu_fintech/main/module_20_challenge/joint_savings.sol"
4. Click "Import"
5. Select Compiler Version 0.5.1.7+commit.d19bba13
6. Click "Compile joint_savings.sol"

---
## Transaction Demonstrations

### Transaction 1: Deposit 1 ether as wei
<img width="1215" alt="image" src="Execution_Results/transaction1.png">

### Transaction 2: Deposit 10 ether as wei
<img width="1215" alt="image" src="Execution_Results/transaction2.png">

### Transaction 3: Deposit 5 ether
<img width="1215" alt="image" src="Execution_Results/transaction3.png">

### Transaction 4: Withdraw 5 ether into accountOne
<img width="1430" alt="image" src="Execution_Results/transaction4.png">

### Transaction 5: Withdraw 10 ether into accountTwo
<img width="1430" alt="image" src="Execution_Results/transaction5.png">

---

## License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
